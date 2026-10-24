"""OpenAI-compatible chat client over the standard library (no third-party packages).

Works unchanged against Ollama (http://localhost:11434/v1) and OpenRouter (https://openrouter.ai/api/v1).
"""
from __future__ import annotations

import json
import os
import time
import urllib.error
import urllib.request
from dataclasses import dataclass
from pathlib import Path

CONFIG_PATH = Path(__file__).resolve().parent.parent / "config" / "models.json"


@dataclass
class Backend:
    name: str
    base_url: str
    api_key: str | None
    default_price: dict | None
    prices: dict
    api: str = "openai"  # "openai" (chat/completions) or "ollama" (native /api/chat, honours `think`)


def _env(var: str) -> str | None:
    """Process environment first; on Windows fall back to the user's persistent variables (set with setx),
    so a key saved there works without restarting the shell. The value is never logged."""
    v = os.environ.get(var)
    if v or os.name != "nt":
        return v
    try:
        import winreg

        with winreg.OpenKey(winreg.HKEY_CURRENT_USER, "Environment") as k:
            return winreg.QueryValueEx(k, var)[0] or None
    except OSError:
        return None


def load_backend(name: str, config_path: Path = CONFIG_PATH) -> Backend:
    cfg = json.loads(config_path.read_text(encoding="utf-8"))
    try:
        b = cfg["backends"][name]
    except KeyError:
        raise ValueError(f"unknown backend {name!r}; configured: {list(cfg['backends'])}")
    key = _env(b["api_key_env"]) if b.get("api_key_env") else None
    if b.get("api_key_env") and not key:
        raise RuntimeError(f"backend {name}: environment variable {b['api_key_env']} is not set")
    return Backend(name, b["base_url"], key, b.get("default_price"), cfg.get("prices", {}), b.get("api", "openai"))


def price_for(backend: Backend, model: str) -> dict:
    p = backend.prices.get(model)
    if p is None:
        p = backend.default_price
    if p is None:
        raise RuntimeError(
            f"no price for {backend.name}/{model} in config/models.json; add it (USD per M tokens) before running"
        )
    return p


def cost_usd(price: dict, usage: dict) -> float:
    return (usage.get("prompt_tokens", 0) * price["input"] + usage.get("completion_tokens", 0) * price["output"]) / 1e6


@dataclass
class ChatResult:
    content: str
    usage: dict
    latency_s: float
    raw: dict
    reasoning: str | None = None  # hidden reasoning, when the API returns it (logged, never graded)


def chat(
    backend: Backend,
    model: str,
    messages: list[dict],
    temperature: float | None = None,
    max_tokens: int = 4096,
    timeout: int = 600,
    extra: dict | None = None,
    think: bool | None = None,
) -> ChatResult:
    """One chat call. `think` is honoured by the Ollama native API (None = model default);
    for OpenAI-style APIs pass provider-specific reasoning controls through `extra`."""
    if backend.api == "ollama":
        body: dict = {"model": model, "messages": messages, "stream": False,
                      "options": {"num_predict": max_tokens}}
        if temperature is not None:
            body["options"]["temperature"] = temperature
        if think is not None:
            body["think"] = think
        path = "/api/chat"
    else:
        body = {"model": model, "messages": messages, "max_tokens": max_tokens}
        if temperature is not None:
            body["temperature"] = temperature
        path = "/chat/completions"
    if extra:
        body.update(extra)
    headers = {"Content-Type": "application/json"}
    if backend.api_key:
        headers["Authorization"] = f"Bearer {backend.api_key}"
    if backend.name == "openrouter":
        headers["HTTP-Referer"] = "https://github.com/gbbarra"
        headers["X-Title"] = "plausibility-eval"
    req = urllib.request.Request(
        backend.base_url.rstrip("/") + path,
        data=json.dumps(body).encode("utf-8"),
        headers=headers,
        method="POST",
    )
    t0 = time.time()
    for attempt in range(4):  # transient 429/5xx (e.g. OpenRouter "could not verify credits in time"): back off and retry
        try:
            with urllib.request.urlopen(req, timeout=timeout) as resp:
                raw = json.loads(resp.read().decode("utf-8"))
            break
        except urllib.error.HTTPError as e:
            detail = e.read().decode("utf-8", errors="replace")[:500]
            if e.code in (429, 500, 502, 503, 504) and attempt < 3:
                time.sleep(8 * (attempt + 1))
                continue
            raise RuntimeError(f"{backend.name}/{model}: HTTP {e.code}: {detail}") from e
    latency = time.time() - t0
    if backend.api == "ollama":
        msg = raw.get("message") or {}
        usage = {"prompt_tokens": raw.get("prompt_eval_count", 0), "completion_tokens": raw.get("eval_count", 0)}
        return ChatResult(content=msg.get("content") or "", usage=usage, latency_s=latency, raw=raw,
                          reasoning=msg.get("thinking"))
    choice = raw["choices"][0]["message"]
    reasoning = choice.get("reasoning") or choice.get("reasoning_content")
    return ChatResult(content=choice.get("content") or "", usage=raw.get("usage") or {}, latency_s=latency,
                      raw=raw, reasoning=reasoning)
