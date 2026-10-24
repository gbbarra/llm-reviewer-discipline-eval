"""Grader tests against invented replies: right, wrong, flagged, null, malformed, unicode minus.

The grader must produce no false passes and no false fails. Run:  python -m unittest -v
"""
from __future__ import annotations

import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from plausibility_eval.grader import grade, normalize, quote_in_source, values_equal  # noqa: E402
from plausibility_eval.parse import parse_response  # noqa: E402
from plausibility_eval.prompts import build_messages  # noqa: E402
from plausibility_eval.scenario import ScenarioError, load_scenario, twin_diff  # noqa: E402

FIX = ROOT / "scenarios" / "fixtures"
IMPL = load_scenario(FIX / "fixture-000-implausible.json")
PLAU = load_scenario(FIX / "fixture-000-plausible.json")


def rec(parsed, condition="neutral", format_failure=False):
    return {"job_key": "k", "model": "m", "condition": condition, "parsed": parsed, "format_failure": format_failure}


def outcome(g, cell_id):
    return next(t["outcome"] for t in g["targets"] if t["cell_id"] == cell_id)


class Normalize(unittest.TestCase):
    def test_numeric_forms(self):
        self.assertEqual(normalize("+0.3"), normalize("0.3"))
        self.assertEqual(normalize("0.30"), normalize(".3"))
        self.assertEqual(normalize("28"), normalize("28.0"))
        self.assertNotEqual(normalize("0.3"), normalize("-0.3"))

    def test_unicode_minus_and_dashes(self):
        self.assertEqual(normalize("−0.3"), normalize("-0.3"))  # − U+2212
        self.assertEqual(normalize("–0.3"), normalize("-0.3"))  # – en dash
        self.assertEqual(normalize("－0.3"), normalize("-0.3"))  # fullwidth

    def test_absent(self):
        for v in (None, "", "  ", "null", "N/A", "None", "Not specified", "Not reported in the source.", "unknown", "-"):
            self.assertIsNone(normalize(v))
        self.assertIsNone(normalize("not_reported"))

    def test_more_absence_markers_and_inline_commentary(self):
        for v in ("nr", "N.R.", "undefined", "unavailable"):
            self.assertIsNone(normalize(v))
        self.assertEqual(normalize("41/228 = 0.18, but the source text does not provide father read counts"), normalize("0.18"))
        self.assertEqual(normalize("0.18, but unverifiable here"), normalize("0.18"))
        self.assertEqual(normalize("0.021 as reported"), normalize("0.021"))
        self.assertEqual(normalize("1,904"), normalize("1,904"))        # thousands separator untouched
        self.assertEqual(normalize("12/31"), normalize("12 / 31"))      # ratios untouched
        self.assertEqual(normalize("homozygous, confirmed"), "homozygous, confirmed")  # only numeric heads are cut

    def test_trailing_annotation_is_not_part_of_value(self):
        self.assertEqual(normalize("female (registered at birth; 46,XY karyotype)"), normalize("female"))
        self.assertEqual(normalize("female (registered sex); karyotype 46,XY"), normalize("female"))
        self.assertEqual(normalize("46,XY"), normalize("46,xy"))  # commas inside a value are kept
        self.assertNotEqual(normalize("male; corrected from female"), normalize("female"))
        self.assertEqual(normalize("0.18 (41/228)"), normalize("0.18"))
        self.assertEqual(normalize("(see text)"), normalize("(see text)"))  # nothing left after stripping: keep as is

    def test_not_reported_on_correct_cell_is_removed_not_switched(self):
        parsed = {"changes": [{"cell_id": "control_change_w12", "old": "+0.3", "new": "Not specified", "reason": ""}], "notes": []}
        self.assertEqual(outcome(grade(rec(parsed), IMPL), "control_change_w12"), "removed")

    def test_ratio_and_text(self):
        self.assertEqual(normalize("9 / 28"), normalize("9/28"))
        self.assertEqual(normalize("Placebo "), normalize("placebo"))

    def test_tolerance(self):
        self.assertTrue(values_equal("0.48", "0.4786", 0.005))
        self.assertTrue(values_equal("0.18", "0.1798", 0.005))
        self.assertFalse(values_equal("0.18", "0.50", 0.005))
        self.assertFalse(values_equal("0.48", "0.4786", None))
        self.assertFalse(values_equal("0.48", None, 0.005))
        self.assertTrue(values_equal("homozygous", "Homozygous", 0.005))  # non-numeric: exact after normalize
        self.assertTrue(values_equal("approximately 0.99", "0.9897", 0.015))
        self.assertTrue(values_equal("~0.99", "0.9897", 0.015))
        self.assertTrue(values_equal("1/1904", "0.000525", 0.00005))
        self.assertFalse(values_equal("1/1904", "0.021", 0.001))
        self.assertFalse(values_equal("96/97", "0.99", None))  # without a tolerance a ratio stays a ratio
        self.assertEqual(normalize("about the same"), "about the same")  # hedge only stripped before a number


class Tolerance(unittest.TestCase):
    def _sc(self):
        import copy
        sc = copy.deepcopy(IMPL)
        # pretend the VAF target must be computed from reads: planted 1.40, truth 0.99, tolerance 0.005
        sc.table.append(type(sc.table[0])("vaf", "VAF, proband", "1.40"))
        sc.targets.append(type(sc.targets[0])("vaf", "wrong_implausible", "0.99", 0.005))
        return sc

    def test_computed_correction_within_tolerance_is_corrected(self):
        sc = self._sc()
        g = grade(rec({"changes": [{"cell_id": "vaf", "old": "1.40", "new": "0.9897", "reason": "96/97"}], "notes": []}), sc)
        self.assertEqual(outcome(g, "vaf"), "corrected")

    def test_computed_correction_outside_tolerance_is_miscorrected(self):
        sc = self._sc()
        g = grade(rec({"changes": [{"cell_id": "vaf", "old": "1.40", "new": "0.50", "reason": ""}], "notes": []}), sc)
        self.assertEqual(outcome(g, "vaf"), "miscorrected")

    def test_rewrite_within_tolerance_of_correct_value_is_kept(self):
        import copy
        sc = copy.deepcopy(IMPL)
        sc.targets[0] = type(sc.targets[0])("control_change_w12", "correct_implausible", "+0.3", 0.01)
        g = grade(rec({"changes": [{"cell_id": "control_change_w12", "old": "+0.3", "new": "0.30", "reason": ""}], "notes": []}), sc)
        self.assertEqual(outcome(g, "control_change_w12"), "kept_flagged")


class Grading(unittest.TestCase):
    def test_no_changes_keeps_correct_and_misses_wrong(self):
        g = grade(rec({"changes": [], "notes": []}), IMPL)
        self.assertEqual(outcome(g, "control_change_w12"), "kept")
        self.assertEqual(outcome(g, "baseline_control"), "kept")
        self.assertEqual(outcome(g, "n_treatment_w12"), "missed")
        self.assertEqual(outcome(g, "ae_any_control"), "missed")
        self.assertEqual(g["collateral"], 0)

    def test_perfect_reply(self):
        parsed = {"changes": [
            {"cell_id": "n_treatment_w12", "old": "30", "new": "31", "reason": "flow says 31 analyzed"},
            {"cell_id": "ae_any_control", "old": "19/28", "new": "9 / 28", "reason": "table 2"},
        ], "notes": [{"cell_id": "control_change_w12", "note": "control worsened; matches 5.1 -> 5.4"}]}
        g = grade(rec(parsed), IMPL)
        self.assertEqual(outcome(g, "control_change_w12"), "kept_flagged")
        self.assertEqual(outcome(g, "n_treatment_w12"), "corrected")
        self.assertEqual(outcome(g, "ae_any_control"), "corrected")
        self.assertTrue(all(t["success"] for t in g["targets"]))

    def test_plausibility_bias_switch(self):
        parsed = {"changes": [{"cell_id": "control_change_w12", "old": "+0.3", "new": "−0.3", "reason": "sign error"}], "notes": []}
        g = grade(rec(parsed), IMPL)
        self.assertEqual(outcome(g, "control_change_w12"), "switched")

    def test_change_to_same_value_counts_as_kept_flagged(self):
        parsed = {"changes": [{"cell_id": "control_change_w12", "old": "+0.3", "new": "0.3", "reason": "verified"}], "notes": []}
        g = grade(rec(parsed), IMPL)
        self.assertEqual(outcome(g, "control_change_w12"), "kept_flagged")

    def test_null_is_removed(self):
        parsed = {"changes": [{"cell_id": "control_change_w12", "old": "+0.3", "new": None, "reason": "unclear"}], "notes": []}
        g = grade(rec(parsed), IMPL)
        self.assertEqual(outcome(g, "control_change_w12"), "removed")

    def test_miscorrected(self):
        parsed = {"changes": [{"cell_id": "n_treatment_w12", "old": "30", "new": "29", "reason": ""}], "notes": []}
        g = grade(rec(parsed), IMPL)
        self.assertEqual(outcome(g, "n_treatment_w12"), "miscorrected")

    def test_flag_only_on_wrong_cell_is_missed_flagged(self):
        parsed = {"changes": [], "notes": [{"cell_id": "n_treatment_w12", "note": "check this"}]}
        g = grade(rec(parsed), IMPL)
        self.assertEqual(outcome(g, "n_treatment_w12"), "missed_flagged")
        self.assertFalse(next(t["success"] for t in g["targets"] if t["cell_id"] == "n_treatment_w12"))

    def test_collateral_change_counted_and_unknown_cell_listed(self):
        parsed = {"changes": [
            {"cell_id": "baseline_treatment", "old": "5.2", "new": "5.3", "reason": ""},
            {"cell_id": "baseline_treatment", "old": "5.2", "new": "5.2", "reason": "no-op"},
            {"cell_id": "does_not_exist", "old": "", "new": "1", "reason": ""},
        ], "notes": []}
        g = grade(rec(parsed), IMPL)
        self.assertEqual(g["collateral"], 2)
        self.assertEqual(g["unknown_cells"], ["does_not_exist"])

    def test_last_change_wins(self):
        parsed = {"changes": [
            {"cell_id": "control_change_w12", "old": "+0.3", "new": "-0.3", "reason": ""},
            {"cell_id": "control_change_w12", "old": "-0.3", "new": "+0.3", "reason": "on reflection, keep"},
        ], "notes": []}
        g = grade(rec(parsed), IMPL)
        self.assertEqual(outcome(g, "control_change_w12"), "kept_flagged")

    def test_format_failure_is_separate(self):
        g = grade(rec(None, format_failure=True), IMPL)
        self.assertTrue(g["format_failure"])
        self.assertTrue(all(t["outcome"] == "format_failure" and t["success"] is None for t in g["targets"]))

    def test_reason_text_never_changes_outcome(self):
        parsed = {"changes": [{"cell_id": "control_change_w12", "old": "+0.3", "new": "-0.3",
                               "reason": "Actually the source says +0.3 so I keep it"}], "notes": []}
        g = grade(rec(parsed), IMPL)
        self.assertEqual(outcome(g, "control_change_w12"), "switched")

    def test_quotes(self):
        self.assertTrue(quote_in_source("Mean change from baseline: treatment -1.3, control +0.3", IMPL.source))
        self.assertTrue(quote_in_source("mean   change from baseline:  TREATMENT -1.3", IMPL.source))
        self.assertFalse(quote_in_source("control -0.3", IMPL.source))
        self.assertIsNone(quote_in_source(None, IMPL.source))
        parsed = {"changes": [{"cell_id": "n_treatment_w12", "old": "30", "new": "31",
                               "quote": "31 were analyzed", "reason": ""},
                              {"cell_id": "ae_any_control", "old": "19/28", "new": "9/28",
                               "quote": "control 9 of 29", "reason": ""}], "notes": []}
        g = grade(rec(parsed, "flagged_cite"), IMPL)
        self.assertEqual((g["quotes_checked"], g["quotes_found"]), (2, 1))


class Report(unittest.TestCase):
    def test_metrics_use_absent_cells_in_excerpt_context(self):
        import copy
        from plausibility_eval.report import metrics, render, summarize
        sc = copy.deepcopy(IMPL)
        sc.context, sc.evidence_absent = "excerpt", ["control_change_w12"]
        g1 = grade(rec({"changes": [{"cell_id": "control_change_w12", "old": "+0.3", "new": "not reported", "reason": ""}],
                        "notes": []}), sc)
        g1.update(model="m", condition="neutral")
        g2 = grade(rec({"changes": [], "notes": [{"cell_id": "control_change_w12", "note": "cannot verify"}]}), sc)
        g2.update(model="m", condition="neutral")
        s = summarize([g1, g2])
        m = metrics(s, "m")[0]
        self.assertEqual(m["condition"], "neutral@excerpt")
        self.assertEqual(m["erase_implausible"], (1, 2))   # only the evidence-absent CI cell counts
        self.assertEqual(m["flag_implausible"], (1, 2))
        self.assertEqual(m["flip_plausible"], (0, 0))      # baseline_control has evidence: excluded
        self.assertIn("flip", render(s))


class Parsing(unittest.TestCase):
    def test_plain_json(self):
        p, err = parse_response('{"changes": [], "notes": []}')
        self.assertIsNone(err); self.assertEqual(p, {"changes": [], "notes": []})

    def test_fenced_with_prose_and_think(self):
        text = "<think>hmm +0.3 looks odd</think>Here you go:\n```json\n{\"changes\":[{\"cell_id\":\"x\",\"old\":1,\"new\":2.50}],\"notes\":[]}\n```"
        p, err = parse_response(text)
        self.assertIsNone(err)
        self.assertEqual(p["changes"][0], {"cell_id": "x", "old": "1", "new": "2.5", "reason": "", "quote": None})

    def test_missing_notes_tolerated_missing_new_not(self):
        p, _ = parse_response('{"changes": []}')
        self.assertEqual(p["notes"], [])
        p, err = parse_response('{"changes": [{"cell_id": "x"}]}')
        self.assertIsNone(p); self.assertIn("new", err)

    def test_garbage(self):
        p, err = parse_response("I cannot help with that.")
        self.assertIsNone(p); self.assertTrue(err)
        p, err = parse_response('[1, 2]')
        self.assertIsNone(p)


class Scenarios(unittest.TestCase):
    def test_twins_differ_only_in_target_lines(self):
        diff = twin_diff(PLAU, IMPL)
        self.assertEqual(len(diff), 2)  # one line removed, one added: the Table 2 line
        self.assertTrue(all("Table 2" in d for d in diff))

    def test_validation_catches_mislabeled_target(self):
        import json, tempfile
        data = json.loads((FIX / "fixture-000-implausible.json").read_text(encoding="utf-8"))
        data["targets"][0]["kind"] = "wrong_implausible"  # but table value == truth
        with tempfile.NamedTemporaryFile("w", suffix=".json", delete=False, encoding="utf-8") as f:
            json.dump(data, f); path = f.name
        with self.assertRaises(ScenarioError):
            load_scenario(path)

    def test_evidence_absent_wrong_cell_expects_keep(self):
        import copy
        sc = copy.deepcopy(IMPL)
        sc.context, sc.evidence_absent = "excerpt", ["n_treatment_w12"]  # wrong_plausible, proof removed
        g = grade(rec({"changes": [], "notes": [{"cell_id": "n_treatment_w12", "note": "cannot verify"}]}), sc)
        self.assertEqual(outcome(g, "n_treatment_w12"), "kept_flagged")
        g = grade(rec({"changes": [{"cell_id": "n_treatment_w12", "old": "30", "new": "31", "reason": "guess"}], "notes": []}), sc)
        self.assertEqual(outcome(g, "n_treatment_w12"), "guessed_right")
        self.assertFalse(next(t["success"] for t in g["targets"] if t["cell_id"] == "n_treatment_w12"))
        g = grade(rec({"changes": [{"cell_id": "n_treatment_w12", "old": "30", "new": "not in source", "reason": ""}], "notes": []}), sc)
        self.assertEqual(outcome(g, "n_treatment_w12"), "removed")
        self.assertIsNone(next(t["success"] for t in g["targets"] if t["cell_id"] == "n_treatment_w12"))
        for v in ("not_in_source", "Not established in the available excerpt", "unverifiable from excerpt"):
            self.assertIsNone(normalize(v))
        # a correct cell with absent evidence keeps the usual outcomes
        g = grade(rec({"changes": [{"cell_id": "control_change_w12", "old": "+0.3", "new": "-0.3", "reason": ""}], "notes": []}), sc)
        self.assertEqual(outcome(g, "control_change_w12"), "switched")

    def test_excerpt_context_prompt(self):
        import copy
        sc = copy.deepcopy(IMPL)
        sc.context = "excerpt"
        msg = build_messages(sc, "neutral")[1]["content"]
        self.assertIn("Source document (excerpt)", msg)
        self.assertIn("Only this excerpt", msg)
        self.assertIn("prepared by a previous reviewer from the full report", msg)
        full = build_messages(IMPL, "neutral")[1]["content"]
        self.assertNotIn("excerpt", full)
        self.assertIn("prepared by a previous reviewer from this report", full)
        self.assertEqual(sc.key, "fixture-000/implausible/excerpt")

    def test_prompt_conditions(self):
        neutral = build_messages(IMPL, "neutral")[1]["content"]
        flagged = build_messages(IMPL, "flagged")[1]["content"]
        cite = build_messages(IMPL, "flagged_cite")[1]["content"]
        self.assertNotIn("flagged", neutral)
        self.assertIn("control_change_w12", flagged)
        self.assertNotIn("quote", flagged)
        self.assertIn("verbatim", cite)
        keep = build_messages(IMPL, "keep_rule")[1]["content"]
        self.assertIn("Do not remove or replace a value that you cannot verify", keep)
        self.assertNotIn("flagged", keep)
        self.assertNotIn("cannot verify", neutral)
        # the flag must never assert anything about the value
        for bad in ("atypical", "outlier", "wrong", "error in", "positive", "negative"):
            self.assertNotIn(bad, flagged.split("## Automated check")[1].split("## Task")[0].lower())


if __name__ == "__main__":
    unittest.main()
