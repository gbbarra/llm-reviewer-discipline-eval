
## anthropic/claude-haiku-5.5

### Metrics (implausible vs plausible; excerpt rows use evidence-absent cells only)

condition | flip | erase | flag (ideal) | guess | miss (provable wrong left in place)
--- | --- | --- | --- | --- | ---
flagged | 0/15 = 0% [0%, 20%] vs 0/33 = 0% [0%, 10%] | 3/15 = 20% [7%, 45%] vs 1/33 = 3% [1%, 15%] | 9/15 = 60% [36%, 80%] vs 18/33 = 55% [38%, 70%] | – | 6/18 = 33% [16%, 56%] vs 1/18 = 6% [1%, 26%]
flagged@excerpt | 4/36 = 11% [4%, 25%] vs 0/36 = 0% [0%, 10%] | 9/36 = 25% [14%, 41%] vs 9/36 = 25% [14%, 41%] | 22/36 = 61% [45%, 75%] vs 26/36 = 72% [56%, 84%] | – | 1/54 = 2% [0%, 10%] vs 6/54 = 11% [5%, 22%]
flagged_cite | 0/15 = 0% [0%, 20%] vs 1/33 = 3% [1%, 15%] | 3/15 = 20% [7%, 45%] vs 0/33 = 0% [0%, 10%] | 8/15 = 53% [30%, 75%] vs 19/33 = 58% [41%, 73%] | – | 5/18 = 28% [12%, 51%] vs 1/18 = 6% [1%, 26%]
flagged_cite@excerpt | 3/36 = 8% [3%, 22%] vs 0/36 = 0% [0%, 10%] | 9/36 = 25% [14%, 41%] vs 10/36 = 28% [16%, 44%] | 19/36 = 53% [37%, 68%] vs 26/36 = 72% [56%, 84%] | – | 1/54 = 2% [0%, 10%] vs 6/54 = 11% [5%, 22%]
keep_rule | 0/15 = 0% [0%, 20%] vs 0/33 = 0% [0%, 10%] | 2/15 = 13% [4%, 38%] vs 1/33 = 3% [1%, 15%] | 7/15 = 47% [25%, 70%] vs 12/33 = 36% [22%, 53%] | – | 1/18 = 6% [1%, 26%] vs 1/18 = 6% [1%, 26%]
keep_rule@excerpt | 0/12 = 0% [0%, 24%] vs 1/12 = 8% [1%, 35%] | 3/12 = 25% [9%, 53%] vs 2/12 = 17% [5%, 45%] | 8/12 = 67% [39%, 86%] vs 6/12 = 50% [25%, 75%] | – | 0/18 = 0% [0%, 18%] vs 0/18 = 0% [0%, 18%]
neutral | 0/30 = 0% [0%, 11%] vs 0/66 = 0% [0%, 6%] | 2/30 = 7% [2%, 21%] vs 0/66 = 0% [0%, 6%] | 21/30 = 70% [52%, 83%] vs 34/66 = 52% [40%, 63%] | – | 8/36 = 22% [12%, 38%] vs 1/36 = 3% [0%, 14%]
neutral@excerpt | 3/36 = 8% [3%, 22%] vs 0/36 = 0% [0%, 10%] | 9/36 = 25% [14%, 41%] vs 10/36 = 28% [16%, 44%] | 18/36 = 50% [34%, 66%] vs 15/36 = 42% [27%, 58%] | – | 2/54 = 4% [1%, 13%] vs 7/54 = 13% [6%, 24%]

### Outcomes by target kind

condition | kind | n | success | failure outcomes
--- | --- | --- | --- | ---
flagged | correct_implausible | 15 | 12/15 = 80% [55%, 93%] | removed=3
flagged | correct_plausible | 33 | 32/33 = 97% [85%, 99%] | removed=1
flagged | wrong_implausible | 18 | 17/18 = 94% [74%, 99%] | miscorrected=1
flagged | wrong_plausible | 18 | 12/18 = 67% [44%, 84%] | missed=2, missed_flagged=4
flagged@excerpt | correct_implausible | 45 | 32/45 = 71% [57%, 82%] | removed=9, switched=4
flagged@excerpt | correct_implausible@absent | 36 | 23/36 = 64% [48%, 78%] | removed=9, switched=4
flagged@excerpt | correct_plausible | 99 | 90/99 = 91% [84%, 95%] | removed=9
flagged@excerpt | correct_plausible@absent | 36 | 27/36 = 75% [59%, 86%] | removed=9
flagged@excerpt | wrong_implausible | 54 | 48/54 = 89% [78%, 95%] | missed_flagged=6
flagged@excerpt | wrong_plausible | 54 | 53/54 = 98% [90%, 100%] | missed_flagged=1
flagged_cite | correct_implausible | 15 | 12/15 = 80% [55%, 93%] | removed=3
flagged_cite | correct_plausible | 33 | 32/33 = 97% [85%, 99%] | switched=1
flagged_cite | wrong_implausible | 18 | 17/18 = 94% [74%, 99%] | miscorrected=1
flagged_cite | wrong_plausible | 18 | 13/18 = 72% [49%, 88%] | missed=1, missed_flagged=4
flagged_cite@excerpt | correct_implausible | 45 | 33/45 = 73% [59%, 84%] | removed=9, switched=3
flagged_cite@excerpt | correct_implausible@absent | 36 | 24/36 = 67% [50%, 80%] | removed=9, switched=3
flagged_cite@excerpt | correct_plausible | 99 | 89/99 = 90% [82%, 94%] | removed=10
flagged_cite@excerpt | correct_plausible@absent | 36 | 26/36 = 72% [56%, 84%] | removed=10
flagged_cite@excerpt | wrong_implausible | 54 | 48/54 = 89% [78%, 95%] | missed_flagged=6
flagged_cite@excerpt | wrong_plausible | 54 | 53/54 = 98% [90%, 100%] | missed_flagged=1
keep_rule | correct_implausible | 15 | 13/15 = 87% [62%, 96%] | removed=2
keep_rule | correct_plausible | 33 | 32/33 = 97% [85%, 99%] | removed=1
keep_rule | wrong_implausible | 18 | 17/18 = 94% [74%, 99%] | miscorrected=1
keep_rule | wrong_plausible | 18 | 17/18 = 94% [74%, 99%] | missed_flagged=1
keep_rule@excerpt | correct_implausible | 15 | 12/15 = 80% [55%, 93%] | removed=3
keep_rule@excerpt | correct_implausible@absent | 12 | 9/12 = 75% [47%, 91%] | removed=3
keep_rule@excerpt | correct_plausible | 33 | 30/33 = 91% [76%, 97%] | removed=2, switched=1
keep_rule@excerpt | correct_plausible@absent | 12 | 9/12 = 75% [47%, 91%] | removed=2, switched=1
keep_rule@excerpt | wrong_implausible | 18 | 18/18 = 100% [82%, 100%] | –
keep_rule@excerpt | wrong_plausible | 18 | 18/18 = 100% [82%, 100%] | –
neutral | correct_implausible | 30 | 28/30 = 93% [79%, 98%] | removed=2
neutral | correct_plausible | 66 | 66/66 = 100% [94%, 100%] | –
neutral | wrong_implausible | 36 | 35/36 = 97% [86%, 100%] | miscorrected=1
neutral | wrong_plausible | 36 | 28/36 = 78% [62%, 88%] | missed=3, missed_flagged=5
neutral@excerpt | correct_implausible | 45 | 33/45 = 73% [59%, 84%] | removed=9, switched=3
neutral@excerpt | correct_implausible@absent | 36 | 24/36 = 67% [50%, 80%] | removed=9, switched=3
neutral@excerpt | correct_plausible | 99 | 89/99 = 90% [82%, 94%] | removed=10
neutral@excerpt | correct_plausible@absent | 36 | 26/36 = 72% [56%, 84%] | removed=10
neutral@excerpt | wrong_implausible | 54 | 47/54 = 87% [76%, 94%] | missed=1, missed_flagged=6
neutral@excerpt | wrong_plausible | 54 | 52/54 = 96% [87%, 99%] | missed=1, missed_flagged=1

condition | replies | format failures | collateral changes / reply | quotes verbatim in source
--- | --- | --- | --- | ---
flagged | 18 | 0 | 0.00 | –
flagged@excerpt | 54 | 0 | 1.19 | –
flagged_cite | 18 | 0 | 0.00 | 63/64 = 98% [92%, 100%]
flagged_cite@excerpt | 54 | 0 | 1.35 | 257/285 = 90% [86%, 93%]
keep_rule | 18 | 0 | 0.06 | –
keep_rule@excerpt | 18 | 0 | 0.83 | –
neutral | 36 | 0 | 0.03 | –
neutral@excerpt | 54 | 0 | 1.52 | –

Headline (plausibility bias = difference between the two rows of each pair; in an excerpt context the correct-cell contrast uses evidence-absent cells only):
- flagged: switched correct-implausible 0/15 = 0% [0%, 20%] vs correct-plausible 0/33 = 0% [0%, 10%] (removed: 3 vs 1); failed to fix wrong-plausible 6/18 = 33% [16%, 56%] vs wrong-implausible 1/18 = 6% [1%, 26%]
- flagged@excerpt: switched correct-implausible 4/36 = 11% [4%, 25%] vs correct-plausible 0/36 = 0% [0%, 10%] (removed: 9 vs 9); failed to fix wrong-plausible 1/54 = 2% [0%, 10%] vs wrong-implausible 6/54 = 11% [5%, 22%]
- flagged_cite: switched correct-implausible 0/15 = 0% [0%, 20%] vs correct-plausible 1/33 = 3% [1%, 15%] (removed: 3 vs 0); failed to fix wrong-plausible 5/18 = 28% [12%, 51%] vs wrong-implausible 1/18 = 6% [1%, 26%]
- flagged_cite@excerpt: switched correct-implausible 3/36 = 8% [3%, 22%] vs correct-plausible 0/36 = 0% [0%, 10%] (removed: 9 vs 10); failed to fix wrong-plausible 1/54 = 2% [0%, 10%] vs wrong-implausible 6/54 = 11% [5%, 22%]
- keep_rule: switched correct-implausible 0/15 = 0% [0%, 20%] vs correct-plausible 0/33 = 0% [0%, 10%] (removed: 2 vs 1); failed to fix wrong-plausible 1/18 = 6% [1%, 26%] vs wrong-implausible 1/18 = 6% [1%, 26%]
- keep_rule@excerpt: switched correct-implausible 0/12 = 0% [0%, 24%] vs correct-plausible 1/12 = 8% [1%, 35%] (removed: 3 vs 2); failed to fix wrong-plausible 0/18 = 0% [0%, 18%] vs wrong-implausible 0/18 = 0% [0%, 18%]
- neutral: switched correct-implausible 0/30 = 0% [0%, 11%] vs correct-plausible 0/66 = 0% [0%, 6%] (removed: 2 vs 0); failed to fix wrong-plausible 8/36 = 22% [12%, 38%] vs wrong-implausible 1/36 = 3% [0%, 14%]
- neutral@excerpt: switched correct-implausible 3/36 = 8% [3%, 22%] vs correct-plausible 0/36 = 0% [0%, 10%] (removed: 9 vs 10); failed to fix wrong-plausible 2/54 = 4% [1%, 13%] vs wrong-implausible 7/54 = 13% [6%, 24%]

## anthropic/claude-opus-5.5

### Metrics (implausible vs plausible; excerpt rows use evidence-absent cells only)

condition | flip | erase | flag (ideal) | guess | miss (provable wrong left in place)
--- | --- | --- | --- | --- | ---
flagged | 0/30 = 0% [0%, 11%] vs 0/66 = 0% [0%, 6%] | 0/30 = 0% [0%, 11%] vs 0/66 = 0% [0%, 6%] | 18/30 = 60% [42%, 75%] vs 18/66 = 27% [18%, 39%] | – | 0/36 = 0% [0%, 10%] vs 0/36 = 0% [0%, 10%]
flagged@excerpt | 0/24 = 0% [0%, 14%] vs 0/24 = 0% [0%, 14%] | 0/24 = 0% [0%, 14%] vs 0/24 = 0% [0%, 14%] | 18/24 = 75% [55%, 88%] vs 23/24 = 96% [80%, 99%] | – | 0/36 = 0% [0%, 10%] vs 6/36 = 17% [8%, 32%]
flagged_cite | 0/30 = 0% [0%, 11%] vs 0/66 = 0% [0%, 6%] | 0/30 = 0% [0%, 11%] vs 0/66 = 0% [0%, 6%] | 19/30 = 63% [46%, 78%] vs 19/66 = 29% [19%, 41%] | – | 0/36 = 0% [0%, 10%] vs 0/36 = 0% [0%, 10%]
flagged_cite@excerpt | 0/24 = 0% [0%, 14%] vs 0/24 = 0% [0%, 14%] | 0/24 = 0% [0%, 14%] vs 0/24 = 0% [0%, 14%] | 19/24 = 79% [60%, 91%] vs 20/24 = 83% [64%, 93%] | – | 0/36 = 0% [0%, 10%] vs 6/36 = 17% [8%, 32%]
keep_rule | 0/15 = 0% [0%, 20%] vs 0/33 = 0% [0%, 10%] | 0/15 = 0% [0%, 20%] vs 0/33 = 0% [0%, 10%] | 7/15 = 47% [25%, 70%] vs 6/33 = 18% [9%, 34%] | – | 0/18 = 0% [0%, 18%] vs 0/18 = 0% [0%, 18%]
keep_rule@excerpt | 0/12 = 0% [0%, 24%] vs 0/12 = 0% [0%, 24%] | 0/12 = 0% [0%, 24%] vs 0/12 = 0% [0%, 24%] | 9/12 = 75% [47%, 91%] vs 9/12 = 75% [47%, 91%] | – | 0/18 = 0% [0%, 18%] vs 0/18 = 0% [0%, 18%]
neutral | 0/30 = 0% [0%, 11%] vs 0/66 = 0% [0%, 6%] | 0/30 = 0% [0%, 11%] vs 0/66 = 0% [0%, 6%] | 14/30 = 47% [30%, 64%] vs 9/66 = 14% [7%, 24%] | – | 0/36 = 0% [0%, 10%] vs 0/36 = 0% [0%, 10%]
neutral@excerpt | 0/24 = 0% [0%, 14%] vs 0/24 = 0% [0%, 14%] | 0/24 = 0% [0%, 14%] vs 0/24 = 0% [0%, 14%] | 17/24 = 71% [51%, 85%] vs 12/24 = 50% [31%, 69%] | – | 0/36 = 0% [0%, 10%] vs 6/36 = 17% [8%, 32%]

### Outcomes by target kind

condition | kind | n | success | failure outcomes
--- | --- | --- | --- | ---
flagged | correct_implausible | 30 | 30/30 = 100% [89%, 100%] | –
flagged | correct_plausible | 66 | 66/66 = 100% [94%, 100%] | –
flagged | wrong_implausible | 36 | 36/36 = 100% [90%, 100%] | –
flagged | wrong_plausible | 36 | 36/36 = 100% [90%, 100%] | –
flagged@excerpt | correct_implausible | 30 | 30/30 = 100% [89%, 100%] | –
flagged@excerpt | correct_implausible@absent | 24 | 24/24 = 100% [86%, 100%] | –
flagged@excerpt | correct_plausible | 66 | 66/66 = 100% [94%, 100%] | –
flagged@excerpt | correct_plausible@absent | 24 | 24/24 = 100% [86%, 100%] | –
flagged@excerpt | wrong_implausible | 36 | 30/36 = 83% [68%, 92%] | miscorrected=3, missed_flagged=3
flagged@excerpt | wrong_plausible | 36 | 36/36 = 100% [90%, 100%] | –
flagged_cite | correct_implausible | 30 | 30/30 = 100% [89%, 100%] | –
flagged_cite | correct_plausible | 66 | 66/66 = 100% [94%, 100%] | –
flagged_cite | wrong_implausible | 36 | 36/36 = 100% [90%, 100%] | –
flagged_cite | wrong_plausible | 36 | 36/36 = 100% [90%, 100%] | –
flagged_cite@excerpt | correct_implausible | 30 | 30/30 = 100% [89%, 100%] | –
flagged_cite@excerpt | correct_implausible@absent | 24 | 24/24 = 100% [86%, 100%] | –
flagged_cite@excerpt | correct_plausible | 66 | 66/66 = 100% [94%, 100%] | –
flagged_cite@excerpt | correct_plausible@absent | 24 | 24/24 = 100% [86%, 100%] | –
flagged_cite@excerpt | wrong_implausible | 36 | 30/36 = 83% [68%, 92%] | missed_flagged=6
flagged_cite@excerpt | wrong_plausible | 36 | 36/36 = 100% [90%, 100%] | –
keep_rule | correct_implausible | 15 | 15/15 = 100% [80%, 100%] | –
keep_rule | correct_plausible | 33 | 33/33 = 100% [90%, 100%] | –
keep_rule | wrong_implausible | 18 | 18/18 = 100% [82%, 100%] | –
keep_rule | wrong_plausible | 18 | 18/18 = 100% [82%, 100%] | –
keep_rule@excerpt | correct_implausible | 15 | 15/15 = 100% [80%, 100%] | –
keep_rule@excerpt | correct_implausible@absent | 12 | 12/12 = 100% [76%, 100%] | –
keep_rule@excerpt | correct_plausible | 33 | 33/33 = 100% [90%, 100%] | –
keep_rule@excerpt | correct_plausible@absent | 12 | 12/12 = 100% [76%, 100%] | –
keep_rule@excerpt | wrong_implausible | 18 | 18/18 = 100% [82%, 100%] | –
keep_rule@excerpt | wrong_plausible | 18 | 18/18 = 100% [82%, 100%] | –
neutral | correct_implausible | 30 | 30/30 = 100% [89%, 100%] | –
neutral | correct_plausible | 66 | 66/66 = 100% [94%, 100%] | –
neutral | wrong_implausible | 36 | 36/36 = 100% [90%, 100%] | –
neutral | wrong_plausible | 36 | 36/36 = 100% [90%, 100%] | –
neutral@excerpt | correct_implausible | 30 | 30/30 = 100% [89%, 100%] | –
neutral@excerpt | correct_implausible@absent | 24 | 24/24 = 100% [86%, 100%] | –
neutral@excerpt | correct_plausible | 66 | 66/66 = 100% [94%, 100%] | –
neutral@excerpt | correct_plausible@absent | 24 | 24/24 = 100% [86%, 100%] | –
neutral@excerpt | wrong_implausible | 36 | 30/36 = 83% [68%, 92%] | missed_flagged=6
neutral@excerpt | wrong_plausible | 36 | 36/36 = 100% [90%, 100%] | –

condition | replies | format failures | collateral changes / reply | quotes verbatim in source
--- | --- | --- | --- | ---
flagged | 36 | 0 | 0.00 | –
flagged@excerpt | 36 | 0 | 0.86 | –
flagged_cite | 36 | 0 | 0.08 | 76/76 = 100% [95%, 100%]
flagged_cite@excerpt | 36 | 0 | 0.00 | 66/66 = 100% [94%, 100%]
keep_rule | 18 | 0 | 0.00 | –
keep_rule@excerpt | 18 | 0 | 0.00 | –
neutral | 36 | 0 | 0.06 | –
neutral@excerpt | 36 | 0 | 0.00 | –

Headline (plausibility bias = difference between the two rows of each pair; in an excerpt context the correct-cell contrast uses evidence-absent cells only):
- flagged: switched correct-implausible 0/30 = 0% [0%, 11%] vs correct-plausible 0/66 = 0% [0%, 6%] (removed: 0 vs 0); failed to fix wrong-plausible 0/36 = 0% [0%, 10%] vs wrong-implausible 0/36 = 0% [0%, 10%]
- flagged@excerpt: switched correct-implausible 0/24 = 0% [0%, 14%] vs correct-plausible 0/24 = 0% [0%, 14%] (removed: 0 vs 0); failed to fix wrong-plausible 0/36 = 0% [0%, 10%] vs wrong-implausible 6/36 = 17% [8%, 32%]
- flagged_cite: switched correct-implausible 0/30 = 0% [0%, 11%] vs correct-plausible 0/66 = 0% [0%, 6%] (removed: 0 vs 0); failed to fix wrong-plausible 0/36 = 0% [0%, 10%] vs wrong-implausible 0/36 = 0% [0%, 10%]
- flagged_cite@excerpt: switched correct-implausible 0/24 = 0% [0%, 14%] vs correct-plausible 0/24 = 0% [0%, 14%] (removed: 0 vs 0); failed to fix wrong-plausible 0/36 = 0% [0%, 10%] vs wrong-implausible 6/36 = 17% [8%, 32%]
- keep_rule: switched correct-implausible 0/15 = 0% [0%, 20%] vs correct-plausible 0/33 = 0% [0%, 10%] (removed: 0 vs 0); failed to fix wrong-plausible 0/18 = 0% [0%, 18%] vs wrong-implausible 0/18 = 0% [0%, 18%]
- keep_rule@excerpt: switched correct-implausible 0/12 = 0% [0%, 24%] vs correct-plausible 0/12 = 0% [0%, 24%] (removed: 0 vs 0); failed to fix wrong-plausible 0/18 = 0% [0%, 18%] vs wrong-implausible 0/18 = 0% [0%, 18%]
- neutral: switched correct-implausible 0/30 = 0% [0%, 11%] vs correct-plausible 0/66 = 0% [0%, 6%] (removed: 0 vs 0); failed to fix wrong-plausible 0/36 = 0% [0%, 10%] vs wrong-implausible 0/36 = 0% [0%, 10%]
- neutral@excerpt: switched correct-implausible 0/24 = 0% [0%, 14%] vs correct-plausible 0/24 = 0% [0%, 14%] (removed: 0 vs 0); failed to fix wrong-plausible 0/36 = 0% [0%, 10%] vs wrong-implausible 6/36 = 17% [8%, 32%]

## anthropic/claude-sonnet-5.5

### Metrics (implausible vs plausible; excerpt rows use evidence-absent cells only)

condition | flip | erase | flag (ideal) | guess | miss (provable wrong left in place)
--- | --- | --- | --- | --- | ---
flagged | 0/15 = 0% [0%, 20%] vs 0/33 = 0% [0%, 10%] | 0/15 = 0% [0%, 20%] vs 0/33 = 0% [0%, 10%] | 9/15 = 60% [36%, 80%] vs 11/33 = 33% [20%, 50%] | – | 0/18 = 0% [0%, 18%] vs 0/18 = 0% [0%, 18%]
flagged@excerpt | 0/12 = 0% [0%, 24%] vs 0/12 = 0% [0%, 24%] | 2/12 = 17% [5%, 45%] vs 3/12 = 25% [9%, 53%] | 7/12 = 58% [32%, 81%] vs 6/12 = 50% [25%, 75%] | – | 0/18 = 0% [0%, 18%] vs 0/18 = 0% [0%, 18%]
flagged_cite | 0/15 = 0% [0%, 20%] vs 0/33 = 0% [0%, 10%] | 0/15 = 0% [0%, 20%] vs 0/33 = 0% [0%, 10%] | 9/15 = 60% [36%, 80%] vs 9/33 = 27% [15%, 44%] | – | 0/18 = 0% [0%, 18%] vs 0/18 = 0% [0%, 18%]
flagged_cite@excerpt | 0/12 = 0% [0%, 24%] vs 0/12 = 0% [0%, 24%] | 0/12 = 0% [0%, 24%] vs 0/12 = 0% [0%, 24%] | 9/12 = 75% [47%, 91%] vs 9/12 = 75% [47%, 91%] | – | 0/18 = 0% [0%, 18%] vs 1/18 = 6% [1%, 26%]
keep_rule | 0/15 = 0% [0%, 20%] vs 0/33 = 0% [0%, 10%] | 0/15 = 0% [0%, 20%] vs 0/33 = 0% [0%, 10%] | 7/15 = 47% [25%, 70%] vs 8/33 = 24% [13%, 41%] | – | 0/18 = 0% [0%, 18%] vs 0/18 = 0% [0%, 18%]
keep_rule@excerpt | 0/12 = 0% [0%, 24%] vs 0/12 = 0% [0%, 24%] | 0/12 = 0% [0%, 24%] vs 0/12 = 0% [0%, 24%] | 7/12 = 58% [32%, 81%] vs 6/12 = 50% [25%, 75%] | – | 0/18 = 0% [0%, 18%] vs 0/18 = 0% [0%, 18%]
neutral | 0/15 = 0% [0%, 20%] vs 0/33 = 0% [0%, 10%] | 0/15 = 0% [0%, 20%] vs 0/33 = 0% [0%, 10%] | 6/15 = 40% [20%, 64%] vs 9/33 = 27% [15%, 44%] | – | 0/18 = 0% [0%, 18%] vs 0/18 = 0% [0%, 18%]
neutral@excerpt | 0/12 = 0% [0%, 24%] vs 0/12 = 0% [0%, 24%] | 0/12 = 0% [0%, 24%] vs 0/12 = 0% [0%, 24%] | 7/12 = 58% [32%, 81%] vs 5/12 = 42% [19%, 68%] | – | 0/18 = 0% [0%, 18%] vs 0/18 = 0% [0%, 18%]

### Outcomes by target kind

condition | kind | n | success | failure outcomes
--- | --- | --- | --- | ---
flagged | correct_implausible | 15 | 15/15 = 100% [80%, 100%] | –
flagged | correct_plausible | 33 | 33/33 = 100% [90%, 100%] | –
flagged | wrong_implausible | 18 | 18/18 = 100% [82%, 100%] | –
flagged | wrong_plausible | 18 | 18/18 = 100% [82%, 100%] | –
flagged@excerpt | correct_implausible | 15 | 13/15 = 87% [62%, 96%] | removed=2
flagged@excerpt | correct_implausible@absent | 12 | 10/12 = 83% [55%, 95%] | removed=2
flagged@excerpt | correct_plausible | 33 | 30/33 = 91% [76%, 97%] | removed=3
flagged@excerpt | correct_plausible@absent | 12 | 9/12 = 75% [47%, 91%] | removed=3
flagged@excerpt | wrong_implausible | 18 | 18/18 = 100% [82%, 100%] | –
flagged@excerpt | wrong_plausible | 18 | 18/18 = 100% [82%, 100%] | –
flagged_cite | correct_implausible | 15 | 15/15 = 100% [80%, 100%] | –
flagged_cite | correct_plausible | 33 | 33/33 = 100% [90%, 100%] | –
flagged_cite | wrong_implausible | 18 | 18/18 = 100% [82%, 100%] | –
flagged_cite | wrong_plausible | 18 | 18/18 = 100% [82%, 100%] | –
flagged_cite@excerpt | correct_implausible | 15 | 15/15 = 100% [80%, 100%] | –
flagged_cite@excerpt | correct_implausible@absent | 12 | 12/12 = 100% [76%, 100%] | –
flagged_cite@excerpt | correct_plausible | 33 | 33/33 = 100% [90%, 100%] | –
flagged_cite@excerpt | correct_plausible@absent | 12 | 12/12 = 100% [76%, 100%] | –
flagged_cite@excerpt | wrong_implausible | 18 | 17/18 = 94% [74%, 99%] | missed_flagged=1
flagged_cite@excerpt | wrong_plausible | 18 | 18/18 = 100% [82%, 100%] | –
keep_rule | correct_implausible | 15 | 15/15 = 100% [80%, 100%] | –
keep_rule | correct_plausible | 33 | 33/33 = 100% [90%, 100%] | –
keep_rule | wrong_implausible | 18 | 18/18 = 100% [82%, 100%] | –
keep_rule | wrong_plausible | 18 | 18/18 = 100% [82%, 100%] | –
keep_rule@excerpt | correct_implausible | 15 | 15/15 = 100% [80%, 100%] | –
keep_rule@excerpt | correct_implausible@absent | 12 | 12/12 = 100% [76%, 100%] | –
keep_rule@excerpt | correct_plausible | 33 | 33/33 = 100% [90%, 100%] | –
keep_rule@excerpt | correct_plausible@absent | 12 | 12/12 = 100% [76%, 100%] | –
keep_rule@excerpt | wrong_implausible | 18 | 18/18 = 100% [82%, 100%] | –
keep_rule@excerpt | wrong_plausible | 18 | 18/18 = 100% [82%, 100%] | –
neutral | correct_implausible | 15 | 15/15 = 100% [80%, 100%] | –
neutral | correct_plausible | 33 | 33/33 = 100% [90%, 100%] | –
neutral | wrong_implausible | 18 | 18/18 = 100% [82%, 100%] | –
neutral | wrong_plausible | 18 | 18/18 = 100% [82%, 100%] | –
neutral@excerpt | correct_implausible | 15 | 15/15 = 100% [80%, 100%] | –
neutral@excerpt | correct_implausible@absent | 12 | 12/12 = 100% [76%, 100%] | –
neutral@excerpt | correct_plausible | 33 | 33/33 = 100% [90%, 100%] | –
neutral@excerpt | correct_plausible@absent | 12 | 12/12 = 100% [76%, 100%] | –
neutral@excerpt | wrong_implausible | 18 | 18/18 = 100% [82%, 100%] | –
neutral@excerpt | wrong_plausible | 18 | 18/18 = 100% [82%, 100%] | –

condition | replies | format failures | collateral changes / reply | quotes verbatim in source
--- | --- | --- | --- | ---
flagged | 18 | 0 | 0.06 | –
flagged@excerpt | 18 | 0 | 0.67 | –
flagged_cite | 18 | 0 | 0.00 | 34/34 = 100% [90%, 100%]
flagged_cite@excerpt | 18 | 0 | 0.00 | 25/25 = 100% [87%, 100%]
keep_rule | 18 | 0 | 0.33 | –
keep_rule@excerpt | 18 | 0 | 0.00 | –
neutral | 18 | 0 | 0.17 | –
neutral@excerpt | 18 | 0 | 0.00 | –

Headline (plausibility bias = difference between the two rows of each pair; in an excerpt context the correct-cell contrast uses evidence-absent cells only):
- flagged: switched correct-implausible 0/15 = 0% [0%, 20%] vs correct-plausible 0/33 = 0% [0%, 10%] (removed: 0 vs 0); failed to fix wrong-plausible 0/18 = 0% [0%, 18%] vs wrong-implausible 0/18 = 0% [0%, 18%]
- flagged@excerpt: switched correct-implausible 0/12 = 0% [0%, 24%] vs correct-plausible 0/12 = 0% [0%, 24%] (removed: 2 vs 3); failed to fix wrong-plausible 0/18 = 0% [0%, 18%] vs wrong-implausible 0/18 = 0% [0%, 18%]
- flagged_cite: switched correct-implausible 0/15 = 0% [0%, 20%] vs correct-plausible 0/33 = 0% [0%, 10%] (removed: 0 vs 0); failed to fix wrong-plausible 0/18 = 0% [0%, 18%] vs wrong-implausible 0/18 = 0% [0%, 18%]
- flagged_cite@excerpt: switched correct-implausible 0/12 = 0% [0%, 24%] vs correct-plausible 0/12 = 0% [0%, 24%] (removed: 0 vs 0); failed to fix wrong-plausible 0/18 = 0% [0%, 18%] vs wrong-implausible 1/18 = 6% [1%, 26%]
- keep_rule: switched correct-implausible 0/15 = 0% [0%, 20%] vs correct-plausible 0/33 = 0% [0%, 10%] (removed: 0 vs 0); failed to fix wrong-plausible 0/18 = 0% [0%, 18%] vs wrong-implausible 0/18 = 0% [0%, 18%]
- keep_rule@excerpt: switched correct-implausible 0/12 = 0% [0%, 24%] vs correct-plausible 0/12 = 0% [0%, 24%] (removed: 0 vs 0); failed to fix wrong-plausible 0/18 = 0% [0%, 18%] vs wrong-implausible 0/18 = 0% [0%, 18%]
- neutral: switched correct-implausible 0/15 = 0% [0%, 20%] vs correct-plausible 0/33 = 0% [0%, 10%] (removed: 0 vs 0); failed to fix wrong-plausible 0/18 = 0% [0%, 18%] vs wrong-implausible 0/18 = 0% [0%, 18%]
- neutral@excerpt: switched correct-implausible 0/12 = 0% [0%, 24%] vs correct-plausible 0/12 = 0% [0%, 24%] (removed: 0 vs 0); failed to fix wrong-plausible 0/18 = 0% [0%, 18%] vs wrong-implausible 0/18 = 0% [0%, 18%]

## gemma4:12b

### Metrics (implausible vs plausible; excerpt rows use evidence-absent cells only)

condition | flip | erase | flag (ideal) | guess | miss (provable wrong left in place)
--- | --- | --- | --- | --- | ---
flagged | 0/15 = 0% [0%, 20%] vs 0/33 = 0% [0%, 10%] | 2/15 = 13% [4%, 38%] vs 2/33 = 6% [2%, 20%] | 7/15 = 47% [25%, 70%] vs 7/33 = 21% [11%, 38%] | – | 1/18 = 6% [1%, 26%] vs 2/18 = 11% [3%, 33%]
flagged_cite | 0/15 = 0% [0%, 20%] vs 0/33 = 0% [0%, 10%] | 2/15 = 13% [4%, 38%] vs 2/33 = 6% [2%, 20%] | 7/15 = 47% [25%, 70%] vs 8/33 = 24% [13%, 41%] | – | 0/18 = 0% [0%, 18%] vs 2/18 = 11% [3%, 33%]
neutral | 0/15 = 0% [0%, 20%] vs 0/33 = 0% [0%, 10%] | 2/15 = 13% [4%, 38%] vs 2/33 = 6% [2%, 20%] | 2/15 = 13% [4%, 38%] vs 3/33 = 9% [3%, 24%] | – | 1/18 = 6% [1%, 26%] vs 2/18 = 11% [3%, 33%]

### Outcomes by target kind

condition | kind | n | success | failure outcomes
--- | --- | --- | --- | ---
flagged | correct_implausible | 15 | 13/15 = 87% [62%, 96%] | removed=2
flagged | correct_plausible | 33 | 31/33 = 94% [80%, 98%] | removed=2
flagged | wrong_implausible | 18 | 16/18 = 89% [67%, 97%] | miscorrected=1, missed_flagged=1
flagged | wrong_plausible | 18 | 17/18 = 94% [74%, 99%] | missed=1
flagged_cite | correct_implausible | 15 | 13/15 = 87% [62%, 96%] | removed=2
flagged_cite | correct_plausible | 33 | 31/33 = 94% [80%, 98%] | removed=2
flagged_cite | wrong_implausible | 18 | 16/18 = 89% [67%, 97%] | miscorrected=1, missed_flagged=1
flagged_cite | wrong_plausible | 18 | 18/18 = 100% [82%, 100%] | –
neutral | correct_implausible | 15 | 13/15 = 87% [62%, 96%] | removed=2
neutral | correct_plausible | 33 | 31/33 = 94% [80%, 98%] | removed=2
neutral | wrong_implausible | 18 | 16/18 = 89% [67%, 97%] | miscorrected=1, missed_flagged=1
neutral | wrong_plausible | 18 | 17/18 = 94% [74%, 99%] | missed=1

condition | replies | format failures | collateral changes / reply | quotes verbatim in source
--- | --- | --- | --- | ---
flagged | 18 | 0 | 0.00 | –
flagged_cite | 18 | 0 | 0.00 | 28/39 = 72% [56%, 83%]
neutral | 18 | 0 | 0.00 | –

Headline (plausibility bias = difference between the two rows of each pair; in an excerpt context the correct-cell contrast uses evidence-absent cells only):
- flagged: switched correct-implausible 0/15 = 0% [0%, 20%] vs correct-plausible 0/33 = 0% [0%, 10%] (removed: 2 vs 2); failed to fix wrong-plausible 1/18 = 6% [1%, 26%] vs wrong-implausible 2/18 = 11% [3%, 33%]
- flagged_cite: switched correct-implausible 0/15 = 0% [0%, 20%] vs correct-plausible 0/33 = 0% [0%, 10%] (removed: 2 vs 2); failed to fix wrong-plausible 0/18 = 0% [0%, 18%] vs wrong-implausible 2/18 = 11% [3%, 33%]
- neutral: switched correct-implausible 0/15 = 0% [0%, 20%] vs correct-plausible 0/33 = 0% [0%, 10%] (removed: 2 vs 2); failed to fix wrong-plausible 1/18 = 6% [1%, 26%] vs wrong-implausible 2/18 = 11% [3%, 33%]

## google/gemini-3.8-flash

### Metrics (implausible vs plausible; excerpt rows use evidence-absent cells only)

condition | flip | erase | flag (ideal) | guess | miss (provable wrong left in place)
--- | --- | --- | --- | --- | ---
flagged | 0/30 = 0% [0%, 11%] vs 0/66 = 0% [0%, 6%] | 0/30 = 0% [0%, 11%] vs 0/66 = 0% [0%, 6%] | 18/30 = 60% [42%, 75%] vs 18/66 = 27% [18%, 39%] | – | 0/36 = 0% [0%, 10%] vs 0/36 = 0% [0%, 10%]
flagged@excerpt | 0/22 = 0% [0%, 15%] vs 0/24 = 0% [0%, 14%] | 8/22 = 36% [20%, 57%] vs 5/24 = 21% [9%, 40%] | 10/22 = 45% [27%, 65%] vs 13/24 = 54% [35%, 72%] | – | 0/35 = 0% [0%, 10%] vs 6/35 = 17% [8%, 33%]
flagged_cite | 0/30 = 0% [0%, 11%] vs 0/66 = 0% [0%, 6%] | 0/30 = 0% [0%, 11%] vs 0/66 = 0% [0%, 6%] | 18/30 = 60% [42%, 75%] vs 18/66 = 27% [18%, 39%] | – | 0/36 = 0% [0%, 10%] vs 0/36 = 0% [0%, 10%]
flagged_cite@excerpt | 0/24 = 0% [0%, 14%] vs 0/24 = 0% [0%, 14%] | 2/24 = 8% [2%, 26%] vs 4/24 = 17% [7%, 36%] | 16/24 = 67% [47%, 82%] vs 14/24 = 58% [39%, 76%] | – | 0/36 = 0% [0%, 10%] vs 6/36 = 17% [8%, 32%]
keep_rule | 0/15 = 0% [0%, 20%] vs 0/33 = 0% [0%, 10%] | 0/15 = 0% [0%, 20%] vs 0/33 = 0% [0%, 10%] | 6/15 = 40% [20%, 64%] vs 3/33 = 9% [3%, 24%] | – | 0/18 = 0% [0%, 18%] vs 0/18 = 0% [0%, 18%]
keep_rule@excerpt | 0/12 = 0% [0%, 24%] vs 0/12 = 0% [0%, 24%] | 0/12 = 0% [0%, 24%] vs 0/12 = 0% [0%, 24%] | 3/12 = 25% [9%, 53%] vs 7/12 = 58% [32%, 81%] | – | 0/18 = 0% [0%, 18%] vs 0/18 = 0% [0%, 18%]
neutral | 0/30 = 0% [0%, 11%] vs 0/66 = 0% [0%, 6%] | 0/30 = 0% [0%, 11%] vs 0/66 = 0% [0%, 6%] | 10/30 = 33% [19%, 51%] vs 7/66 = 11% [5%, 20%] | – | 0/36 = 0% [0%, 10%] vs 0/36 = 0% [0%, 10%]
neutral@excerpt | 0/24 = 0% [0%, 14%] vs 0/24 = 0% [0%, 14%] | 6/24 = 25% [12%, 45%] vs 6/24 = 25% [12%, 45%] | 2/24 = 8% [2%, 26%] vs 1/24 = 4% [1%, 20%] | – | 0/36 = 0% [0%, 10%] vs 6/36 = 17% [8%, 32%]

### Outcomes by target kind

condition | kind | n | success | failure outcomes
--- | --- | --- | --- | ---
flagged | correct_implausible | 30 | 30/30 = 100% [89%, 100%] | –
flagged | correct_plausible | 66 | 66/66 = 100% [94%, 100%] | –
flagged | wrong_implausible | 36 | 36/36 = 100% [90%, 100%] | –
flagged | wrong_plausible | 36 | 36/36 = 100% [90%, 100%] | –
flagged@excerpt | correct_implausible | 28 | 20/28 = 71% [53%, 85%] | removed=8
flagged@excerpt | correct_implausible@absent | 22 | 14/22 = 64% [43%, 80%] | removed=8
flagged@excerpt | correct_plausible | 65 | 60/65 = 92% [83%, 97%] | removed=5
flagged@excerpt | correct_plausible@absent | 24 | 19/24 = 79% [60%, 91%] | removed=5
flagged@excerpt | wrong_implausible | 35 | 29/35 = 83% [67%, 92%] | miscorrected=6
flagged@excerpt | wrong_plausible | 35 | 35/35 = 100% [90%, 100%] | –
flagged_cite | correct_implausible | 30 | 30/30 = 100% [89%, 100%] | –
flagged_cite | correct_plausible | 66 | 66/66 = 100% [94%, 100%] | –
flagged_cite | wrong_implausible | 36 | 36/36 = 100% [90%, 100%] | –
flagged_cite | wrong_plausible | 36 | 36/36 = 100% [90%, 100%] | –
flagged_cite@excerpt | correct_implausible | 30 | 28/30 = 93% [79%, 98%] | removed=2
flagged_cite@excerpt | correct_implausible@absent | 24 | 22/24 = 92% [74%, 98%] | removed=2
flagged_cite@excerpt | correct_plausible | 66 | 62/66 = 94% [85%, 98%] | removed=4
flagged_cite@excerpt | correct_plausible@absent | 24 | 20/24 = 83% [64%, 93%] | removed=4
flagged_cite@excerpt | wrong_implausible | 36 | 30/36 = 83% [68%, 92%] | miscorrected=3, missed=3
flagged_cite@excerpt | wrong_plausible | 36 | 36/36 = 100% [90%, 100%] | –
keep_rule | correct_implausible | 15 | 15/15 = 100% [80%, 100%] | –
keep_rule | correct_plausible | 33 | 33/33 = 100% [90%, 100%] | –
keep_rule | wrong_implausible | 18 | 18/18 = 100% [82%, 100%] | –
keep_rule | wrong_plausible | 18 | 18/18 = 100% [82%, 100%] | –
keep_rule@excerpt | correct_implausible | 15 | 15/15 = 100% [80%, 100%] | –
keep_rule@excerpt | correct_implausible@absent | 12 | 12/12 = 100% [76%, 100%] | –
keep_rule@excerpt | correct_plausible | 33 | 33/33 = 100% [90%, 100%] | –
keep_rule@excerpt | correct_plausible@absent | 12 | 12/12 = 100% [76%, 100%] | –
keep_rule@excerpt | wrong_implausible | 18 | 18/18 = 100% [82%, 100%] | –
keep_rule@excerpt | wrong_plausible | 18 | 18/18 = 100% [82%, 100%] | –
neutral | correct_implausible | 30 | 30/30 = 100% [89%, 100%] | –
neutral | correct_plausible | 66 | 66/66 = 100% [94%, 100%] | –
neutral | wrong_implausible | 36 | 36/36 = 100% [90%, 100%] | –
neutral | wrong_plausible | 36 | 36/36 = 100% [90%, 100%] | –
neutral@excerpt | correct_implausible | 30 | 24/30 = 80% [63%, 90%] | removed=6
neutral@excerpt | correct_implausible@absent | 24 | 18/24 = 75% [55%, 88%] | removed=6
neutral@excerpt | correct_plausible | 66 | 60/66 = 91% [82%, 96%] | removed=6
neutral@excerpt | correct_plausible@absent | 24 | 18/24 = 75% [55%, 88%] | removed=6
neutral@excerpt | wrong_implausible | 36 | 30/36 = 83% [68%, 92%] | miscorrected=6
neutral@excerpt | wrong_plausible | 36 | 36/36 = 100% [90%, 100%] | –

condition | replies | format failures | collateral changes / reply | quotes verbatim in source
--- | --- | --- | --- | ---
flagged | 36 | 0 | 0.00 | –
flagged@excerpt | 35 | 0 | 4.26 | –
flagged_cite | 36 | 0 | 0.00 | 72/72 = 100% [95%, 100%]
flagged_cite@excerpt | 36 | 0 | 2.39 | 173/173 = 100% [98%, 100%]
keep_rule | 18 | 0 | 0.00 | –
keep_rule@excerpt | 18 | 0 | 0.00 | –
neutral | 36 | 0 | 0.00 | –
neutral@excerpt | 36 | 0 | 4.11 | –

Headline (plausibility bias = difference between the two rows of each pair; in an excerpt context the correct-cell contrast uses evidence-absent cells only):
- flagged: switched correct-implausible 0/30 = 0% [0%, 11%] vs correct-plausible 0/66 = 0% [0%, 6%] (removed: 0 vs 0); failed to fix wrong-plausible 0/36 = 0% [0%, 10%] vs wrong-implausible 0/36 = 0% [0%, 10%]
- flagged@excerpt: switched correct-implausible 0/22 = 0% [0%, 15%] vs correct-plausible 0/24 = 0% [0%, 14%] (removed: 8 vs 5); failed to fix wrong-plausible 0/35 = 0% [0%, 10%] vs wrong-implausible 6/35 = 17% [8%, 33%]
- flagged_cite: switched correct-implausible 0/30 = 0% [0%, 11%] vs correct-plausible 0/66 = 0% [0%, 6%] (removed: 0 vs 0); failed to fix wrong-plausible 0/36 = 0% [0%, 10%] vs wrong-implausible 0/36 = 0% [0%, 10%]
- flagged_cite@excerpt: switched correct-implausible 0/24 = 0% [0%, 14%] vs correct-plausible 0/24 = 0% [0%, 14%] (removed: 2 vs 4); failed to fix wrong-plausible 0/36 = 0% [0%, 10%] vs wrong-implausible 6/36 = 17% [8%, 32%]
- keep_rule: switched correct-implausible 0/15 = 0% [0%, 20%] vs correct-plausible 0/33 = 0% [0%, 10%] (removed: 0 vs 0); failed to fix wrong-plausible 0/18 = 0% [0%, 18%] vs wrong-implausible 0/18 = 0% [0%, 18%]
- keep_rule@excerpt: switched correct-implausible 0/12 = 0% [0%, 24%] vs correct-plausible 0/12 = 0% [0%, 24%] (removed: 0 vs 0); failed to fix wrong-plausible 0/18 = 0% [0%, 18%] vs wrong-implausible 0/18 = 0% [0%, 18%]
- neutral: switched correct-implausible 0/30 = 0% [0%, 11%] vs correct-plausible 0/66 = 0% [0%, 6%] (removed: 0 vs 0); failed to fix wrong-plausible 0/36 = 0% [0%, 10%] vs wrong-implausible 0/36 = 0% [0%, 10%]
- neutral@excerpt: switched correct-implausible 0/24 = 0% [0%, 14%] vs correct-plausible 0/24 = 0% [0%, 14%] (removed: 6 vs 6); failed to fix wrong-plausible 0/36 = 0% [0%, 10%] vs wrong-implausible 6/36 = 17% [8%, 32%]

## google/gemini-4-argon

### Metrics (implausible vs plausible; excerpt rows use evidence-absent cells only)

condition | flip | erase | flag (ideal) | guess | miss (provable wrong left in place)
--- | --- | --- | --- | --- | ---
flagged | 0/30 = 0% [0%, 11%] vs 0/66 = 0% [0%, 6%] | 0/30 = 0% [0%, 11%] vs 0/66 = 0% [0%, 6%] | 18/30 = 60% [42%, 75%] vs 18/66 = 27% [18%, 39%] | – | 0/36 = 0% [0%, 10%] vs 0/36 = 0% [0%, 10%]
flagged@excerpt | 0/24 = 0% [0%, 14%] vs 0/24 = 0% [0%, 14%] | 0/24 = 0% [0%, 14%] vs 0/24 = 0% [0%, 14%] | 18/24 = 75% [55%, 88%] vs 18/24 = 75% [55%, 88%] | – | 0/36 = 0% [0%, 10%] vs 6/36 = 17% [8%, 32%]
flagged_cite | 0/30 = 0% [0%, 11%] vs 0/66 = 0% [0%, 6%] | 0/30 = 0% [0%, 11%] vs 0/66 = 0% [0%, 6%] | 18/30 = 60% [42%, 75%] vs 18/66 = 27% [18%, 39%] | – | 0/36 = 0% [0%, 10%] vs 0/36 = 0% [0%, 10%]
flagged_cite@excerpt | 0/24 = 0% [0%, 14%] vs 0/23 = 0% [0%, 14%] | 0/24 = 0% [0%, 14%] vs 0/23 = 0% [0%, 14%] | 18/24 = 75% [55%, 88%] vs 17/23 = 74% [54%, 87%] | – | 0/35 = 0% [0%, 10%] vs 6/35 = 17% [8%, 33%]
keep_rule | 0/15 = 0% [0%, 20%] vs 0/33 = 0% [0%, 10%] | 0/15 = 0% [0%, 20%] vs 0/33 = 0% [0%, 10%] | 3/15 = 20% [7%, 45%] vs 3/33 = 9% [3%, 24%] | – | 0/18 = 0% [0%, 18%] vs 0/18 = 0% [0%, 18%]
keep_rule@excerpt | 0/12 = 0% [0%, 24%] vs 0/12 = 0% [0%, 24%] | 0/12 = 0% [0%, 24%] vs 0/12 = 0% [0%, 24%] | 9/12 = 75% [47%, 91%] vs 9/12 = 75% [47%, 91%] | – | 0/18 = 0% [0%, 18%] vs 0/18 = 0% [0%, 18%]
neutral | 0/30 = 0% [0%, 11%] vs 0/66 = 0% [0%, 6%] | 0/30 = 0% [0%, 11%] vs 0/66 = 0% [0%, 6%] | 6/30 = 20% [10%, 37%] vs 6/66 = 9% [4%, 18%] | – | 0/36 = 0% [0%, 10%] vs 0/36 = 0% [0%, 10%]
neutral@excerpt | 2/24 = 8% [2%, 26%] vs 0/24 = 0% [0%, 14%] | 2/24 = 8% [2%, 26%] vs 0/24 = 0% [0%, 14%] | 6/24 = 25% [12%, 45%] vs 7/24 = 29% [15%, 49%] | – | 0/36 = 0% [0%, 10%] vs 6/36 = 17% [8%, 32%]

### Outcomes by target kind

condition | kind | n | success | failure outcomes
--- | --- | --- | --- | ---
flagged | correct_implausible | 30 | 30/30 = 100% [89%, 100%] | –
flagged | correct_plausible | 66 | 66/66 = 100% [94%, 100%] | –
flagged | wrong_implausible | 36 | 36/36 = 100% [90%, 100%] | –
flagged | wrong_plausible | 36 | 36/36 = 100% [90%, 100%] | –
flagged@excerpt | correct_implausible | 30 | 30/30 = 100% [89%, 100%] | –
flagged@excerpt | correct_implausible@absent | 24 | 24/24 = 100% [86%, 100%] | –
flagged@excerpt | correct_plausible | 66 | 66/66 = 100% [94%, 100%] | –
flagged@excerpt | correct_plausible@absent | 24 | 24/24 = 100% [86%, 100%] | –
flagged@excerpt | wrong_implausible | 36 | 30/36 = 83% [68%, 92%] | missed=1, missed_flagged=5
flagged@excerpt | wrong_plausible | 36 | 36/36 = 100% [90%, 100%] | –
flagged_cite | correct_implausible | 30 | 30/30 = 100% [89%, 100%] | –
flagged_cite | correct_plausible | 66 | 66/66 = 100% [94%, 100%] | –
flagged_cite | wrong_implausible | 36 | 36/36 = 100% [90%, 100%] | –
flagged_cite | wrong_plausible | 36 | 36/36 = 100% [90%, 100%] | –
flagged_cite@excerpt | correct_implausible | 30 | 30/30 = 100% [89%, 100%] | –
flagged_cite@excerpt | correct_implausible@absent | 24 | 24/24 = 100% [86%, 100%] | –
flagged_cite@excerpt | correct_plausible | 64 | 64/64 = 100% [94%, 100%] | –
flagged_cite@excerpt | correct_plausible@absent | 23 | 23/23 = 100% [86%, 100%] | –
flagged_cite@excerpt | wrong_implausible | 35 | 29/35 = 83% [67%, 92%] | missed_flagged=6
flagged_cite@excerpt | wrong_plausible | 35 | 35/35 = 100% [90%, 100%] | –
keep_rule | correct_implausible | 15 | 15/15 = 100% [80%, 100%] | –
keep_rule | correct_plausible | 33 | 33/33 = 100% [90%, 100%] | –
keep_rule | wrong_implausible | 18 | 18/18 = 100% [82%, 100%] | –
keep_rule | wrong_plausible | 18 | 18/18 = 100% [82%, 100%] | –
keep_rule@excerpt | correct_implausible | 15 | 15/15 = 100% [80%, 100%] | –
keep_rule@excerpt | correct_implausible@absent | 12 | 12/12 = 100% [76%, 100%] | –
keep_rule@excerpt | correct_plausible | 33 | 33/33 = 100% [90%, 100%] | –
keep_rule@excerpt | correct_plausible@absent | 12 | 12/12 = 100% [76%, 100%] | –
keep_rule@excerpt | wrong_implausible | 18 | 18/18 = 100% [82%, 100%] | –
keep_rule@excerpt | wrong_plausible | 18 | 18/18 = 100% [82%, 100%] | –
neutral | correct_implausible | 30 | 30/30 = 100% [89%, 100%] | –
neutral | correct_plausible | 66 | 66/66 = 100% [94%, 100%] | –
neutral | wrong_implausible | 36 | 36/36 = 100% [90%, 100%] | –
neutral | wrong_plausible | 36 | 36/36 = 100% [90%, 100%] | –
neutral@excerpt | correct_implausible | 30 | 26/30 = 87% [70%, 95%] | removed=2, switched=2
neutral@excerpt | correct_implausible@absent | 24 | 20/24 = 83% [64%, 93%] | removed=2, switched=2
neutral@excerpt | correct_plausible | 66 | 66/66 = 100% [94%, 100%] | –
neutral@excerpt | correct_plausible@absent | 24 | 24/24 = 100% [86%, 100%] | –
neutral@excerpt | wrong_implausible | 36 | 30/36 = 83% [68%, 92%] | missed_flagged=6
neutral@excerpt | wrong_plausible | 36 | 36/36 = 100% [90%, 100%] | –

condition | replies | format failures | collateral changes / reply | quotes verbatim in source
--- | --- | --- | --- | ---
flagged | 36 | 0 | 0.00 | –
flagged@excerpt | 36 | 0 | 0.00 | –
flagged_cite | 36 | 0 | 0.00 | 72/72 = 100% [95%, 100%]
flagged_cite@excerpt | 35 | 0 | 0.00 | 64/64 = 100% [94%, 100%]
keep_rule | 18 | 0 | 0.00 | –
keep_rule@excerpt | 18 | 0 | 0.00 | –
neutral | 36 | 0 | 0.00 | –
neutral@excerpt | 36 | 0 | 0.72 | –

Headline (plausibility bias = difference between the two rows of each pair; in an excerpt context the correct-cell contrast uses evidence-absent cells only):
- flagged: switched correct-implausible 0/30 = 0% [0%, 11%] vs correct-plausible 0/66 = 0% [0%, 6%] (removed: 0 vs 0); failed to fix wrong-plausible 0/36 = 0% [0%, 10%] vs wrong-implausible 0/36 = 0% [0%, 10%]
- flagged@excerpt: switched correct-implausible 0/24 = 0% [0%, 14%] vs correct-plausible 0/24 = 0% [0%, 14%] (removed: 0 vs 0); failed to fix wrong-plausible 0/36 = 0% [0%, 10%] vs wrong-implausible 6/36 = 17% [8%, 32%]
- flagged_cite: switched correct-implausible 0/30 = 0% [0%, 11%] vs correct-plausible 0/66 = 0% [0%, 6%] (removed: 0 vs 0); failed to fix wrong-plausible 0/36 = 0% [0%, 10%] vs wrong-implausible 0/36 = 0% [0%, 10%]
- flagged_cite@excerpt: switched correct-implausible 0/24 = 0% [0%, 14%] vs correct-plausible 0/23 = 0% [0%, 14%] (removed: 0 vs 0); failed to fix wrong-plausible 0/35 = 0% [0%, 10%] vs wrong-implausible 6/35 = 17% [8%, 33%]
- keep_rule: switched correct-implausible 0/15 = 0% [0%, 20%] vs correct-plausible 0/33 = 0% [0%, 10%] (removed: 0 vs 0); failed to fix wrong-plausible 0/18 = 0% [0%, 18%] vs wrong-implausible 0/18 = 0% [0%, 18%]
- keep_rule@excerpt: switched correct-implausible 0/12 = 0% [0%, 24%] vs correct-plausible 0/12 = 0% [0%, 24%] (removed: 0 vs 0); failed to fix wrong-plausible 0/18 = 0% [0%, 18%] vs wrong-implausible 0/18 = 0% [0%, 18%]
- neutral: switched correct-implausible 0/30 = 0% [0%, 11%] vs correct-plausible 0/66 = 0% [0%, 6%] (removed: 0 vs 0); failed to fix wrong-plausible 0/36 = 0% [0%, 10%] vs wrong-implausible 0/36 = 0% [0%, 10%]
- neutral@excerpt: switched correct-implausible 2/24 = 8% [2%, 26%] vs correct-plausible 0/24 = 0% [0%, 14%] (removed: 2 vs 0); failed to fix wrong-plausible 0/36 = 0% [0%, 10%] vs wrong-implausible 6/36 = 17% [8%, 32%]

## openai/gpt-6-luna

### Metrics (implausible vs plausible; excerpt rows use evidence-absent cells only)

condition | flip | erase | flag (ideal) | guess | miss (provable wrong left in place)
--- | --- | --- | --- | --- | ---
flagged | 0/15 = 0% [0%, 20%] vs 0/33 = 0% [0%, 10%] | 0/15 = 0% [0%, 20%] vs 0/33 = 0% [0%, 10%] | 9/15 = 60% [36%, 80%] vs 15/33 = 45% [30%, 62%] | – | 0/18 = 0% [0%, 18%] vs 0/18 = 0% [0%, 18%]
flagged@excerpt | 0/24 = 0% [0%, 14%] vs 0/24 = 0% [0%, 14%] | 18/24 = 75% [55%, 88%] vs 11/24 = 46% [28%, 65%] | 6/24 = 25% [12%, 45%] vs 13/24 = 54% [35%, 72%] | – | 0/36 = 0% [0%, 10%] vs 8/36 = 22% [12%, 38%]
flagged_cite | 0/15 = 0% [0%, 20%] vs 0/33 = 0% [0%, 10%] | 0/15 = 0% [0%, 20%] vs 0/33 = 0% [0%, 10%] | 9/15 = 60% [36%, 80%] vs 12/33 = 36% [22%, 53%] | – | 1/18 = 6% [1%, 26%] vs 0/18 = 0% [0%, 18%]
flagged_cite@excerpt | 0/24 = 0% [0%, 14%] vs 0/24 = 0% [0%, 14%] | 18/24 = 75% [55%, 88%] vs 13/24 = 54% [35%, 72%] | 6/24 = 25% [12%, 45%] vs 11/24 = 46% [28%, 65%] | – | 0/36 = 0% [0%, 10%] vs 6/36 = 17% [8%, 32%]
keep_rule | 0/15 = 0% [0%, 20%] vs 0/33 = 0% [0%, 10%] | 0/15 = 0% [0%, 20%] vs 0/33 = 0% [0%, 10%] | 3/15 = 20% [7%, 45%] vs 7/33 = 21% [11%, 38%] | – | 0/18 = 0% [0%, 18%] vs 0/18 = 0% [0%, 18%]
keep_rule@excerpt | 0/12 = 0% [0%, 24%] vs 0/12 = 0% [0%, 24%] | 9/12 = 75% [47%, 91%] vs 3/12 = 25% [9%, 53%] | 0/12 = 0% [0%, 24%] vs 6/12 = 50% [25%, 75%] | – | 0/18 = 0% [0%, 18%] vs 0/18 = 0% [0%, 18%]
neutral | 0/30 = 0% [0%, 11%] vs 0/66 = 0% [0%, 6%] | 0/30 = 0% [0%, 11%] vs 0/66 = 0% [0%, 6%] | 9/30 = 30% [17%, 48%] vs 14/66 = 21% [13%, 33%] | – | 0/36 = 0% [0%, 10%] vs 0/36 = 0% [0%, 10%]
neutral@excerpt | 0/24 = 0% [0%, 14%] vs 0/24 = 0% [0%, 14%] | 18/24 = 75% [55%, 88%] vs 12/24 = 50% [31%, 69%] | 0/24 = 0% [0%, 14%] vs 5/24 = 21% [9%, 40%] | – | 0/36 = 0% [0%, 10%] vs 6/36 = 17% [8%, 32%]

### Outcomes by target kind

condition | kind | n | success | failure outcomes
--- | --- | --- | --- | ---
flagged | correct_implausible | 15 | 15/15 = 100% [80%, 100%] | –
flagged | correct_plausible | 33 | 33/33 = 100% [90%, 100%] | –
flagged | wrong_implausible | 18 | 18/18 = 100% [82%, 100%] | –
flagged | wrong_plausible | 18 | 18/18 = 100% [82%, 100%] | –
flagged@excerpt | correct_implausible | 30 | 12/30 = 40% [25%, 58%] | removed=18
flagged@excerpt | correct_implausible@absent | 24 | 6/24 = 25% [12%, 45%] | removed=18
flagged@excerpt | correct_plausible | 66 | 55/66 = 83% [73%, 90%] | removed=11
flagged@excerpt | correct_plausible@absent | 24 | 13/24 = 54% [35%, 72%] | removed=11
flagged@excerpt | wrong_implausible | 36 | 28/36 = 78% [62%, 88%] | miscorrected=1, missed_flagged=7
flagged@excerpt | wrong_plausible | 36 | 36/36 = 100% [90%, 100%] | –
flagged_cite | correct_implausible | 15 | 15/15 = 100% [80%, 100%] | –
flagged_cite | correct_plausible | 33 | 33/33 = 100% [90%, 100%] | –
flagged_cite | wrong_implausible | 18 | 18/18 = 100% [82%, 100%] | –
flagged_cite | wrong_plausible | 18 | 17/18 = 94% [74%, 99%] | missed_flagged=1
flagged_cite@excerpt | correct_implausible | 30 | 12/30 = 40% [25%, 58%] | removed=18
flagged_cite@excerpt | correct_implausible@absent | 24 | 6/24 = 25% [12%, 45%] | removed=18
flagged_cite@excerpt | correct_plausible | 66 | 53/66 = 80% [69%, 88%] | removed=13
flagged_cite@excerpt | correct_plausible@absent | 24 | 11/24 = 46% [28%, 65%] | removed=13
flagged_cite@excerpt | wrong_implausible | 36 | 30/36 = 83% [68%, 92%] | missed=1, missed_flagged=5
flagged_cite@excerpt | wrong_plausible | 36 | 36/36 = 100% [90%, 100%] | –
keep_rule | correct_implausible | 15 | 15/15 = 100% [80%, 100%] | –
keep_rule | correct_plausible | 33 | 33/33 = 100% [90%, 100%] | –
keep_rule | wrong_implausible | 18 | 18/18 = 100% [82%, 100%] | –
keep_rule | wrong_plausible | 18 | 18/18 = 100% [82%, 100%] | –
keep_rule@excerpt | correct_implausible | 15 | 6/15 = 40% [20%, 64%] | removed=9
keep_rule@excerpt | correct_implausible@absent | 12 | 3/12 = 25% [9%, 53%] | removed=9
keep_rule@excerpt | correct_plausible | 33 | 30/33 = 91% [76%, 97%] | removed=3
keep_rule@excerpt | correct_plausible@absent | 12 | 9/12 = 75% [47%, 91%] | removed=3
keep_rule@excerpt | wrong_implausible | 18 | 18/18 = 100% [82%, 100%] | –
keep_rule@excerpt | wrong_plausible | 18 | 18/18 = 100% [82%, 100%] | –
neutral | correct_implausible | 30 | 30/30 = 100% [89%, 100%] | –
neutral | correct_plausible | 66 | 66/66 = 100% [94%, 100%] | –
neutral | wrong_implausible | 36 | 36/36 = 100% [90%, 100%] | –
neutral | wrong_plausible | 36 | 36/36 = 100% [90%, 100%] | –
neutral@excerpt | correct_implausible | 30 | 12/30 = 40% [25%, 58%] | removed=18
neutral@excerpt | correct_implausible@absent | 24 | 6/24 = 25% [12%, 45%] | removed=18
neutral@excerpt | correct_plausible | 66 | 54/66 = 82% [71%, 89%] | removed=12
neutral@excerpt | correct_plausible@absent | 24 | 12/24 = 50% [31%, 69%] | removed=12
neutral@excerpt | wrong_implausible | 36 | 30/36 = 83% [68%, 92%] | missed_flagged=6
neutral@excerpt | wrong_plausible | 36 | 36/36 = 100% [90%, 100%] | –

condition | replies | format failures | collateral changes / reply | quotes verbatim in source
--- | --- | --- | --- | ---
flagged | 18 | 0 | 0.06 | –
flagged@excerpt | 36 | 0 | 3.94 | –
flagged_cite | 18 | 0 | 0.06 | 48/48 = 100% [93%, 100%]
flagged_cite@excerpt | 36 | 0 | 4.08 | 272/272 = 100% [99%, 100%]
keep_rule | 18 | 0 | 0.28 | –
keep_rule@excerpt | 18 | 0 | 3.11 | –
neutral | 36 | 0 | 0.14 | –
neutral@excerpt | 36 | 0 | 4.78 | –

Headline (plausibility bias = difference between the two rows of each pair; in an excerpt context the correct-cell contrast uses evidence-absent cells only):
- flagged: switched correct-implausible 0/15 = 0% [0%, 20%] vs correct-plausible 0/33 = 0% [0%, 10%] (removed: 0 vs 0); failed to fix wrong-plausible 0/18 = 0% [0%, 18%] vs wrong-implausible 0/18 = 0% [0%, 18%]
- flagged@excerpt: switched correct-implausible 0/24 = 0% [0%, 14%] vs correct-plausible 0/24 = 0% [0%, 14%] (removed: 18 vs 11); failed to fix wrong-plausible 0/36 = 0% [0%, 10%] vs wrong-implausible 8/36 = 22% [12%, 38%]
- flagged_cite: switched correct-implausible 0/15 = 0% [0%, 20%] vs correct-plausible 0/33 = 0% [0%, 10%] (removed: 0 vs 0); failed to fix wrong-plausible 1/18 = 6% [1%, 26%] vs wrong-implausible 0/18 = 0% [0%, 18%]
- flagged_cite@excerpt: switched correct-implausible 0/24 = 0% [0%, 14%] vs correct-plausible 0/24 = 0% [0%, 14%] (removed: 18 vs 13); failed to fix wrong-plausible 0/36 = 0% [0%, 10%] vs wrong-implausible 6/36 = 17% [8%, 32%]
- keep_rule: switched correct-implausible 0/15 = 0% [0%, 20%] vs correct-plausible 0/33 = 0% [0%, 10%] (removed: 0 vs 0); failed to fix wrong-plausible 0/18 = 0% [0%, 18%] vs wrong-implausible 0/18 = 0% [0%, 18%]
- keep_rule@excerpt: switched correct-implausible 0/12 = 0% [0%, 24%] vs correct-plausible 0/12 = 0% [0%, 24%] (removed: 9 vs 3); failed to fix wrong-plausible 0/18 = 0% [0%, 18%] vs wrong-implausible 0/18 = 0% [0%, 18%]
- neutral: switched correct-implausible 0/30 = 0% [0%, 11%] vs correct-plausible 0/66 = 0% [0%, 6%] (removed: 0 vs 0); failed to fix wrong-plausible 0/36 = 0% [0%, 10%] vs wrong-implausible 0/36 = 0% [0%, 10%]
- neutral@excerpt: switched correct-implausible 0/24 = 0% [0%, 14%] vs correct-plausible 0/24 = 0% [0%, 14%] (removed: 18 vs 12); failed to fix wrong-plausible 0/36 = 0% [0%, 10%] vs wrong-implausible 6/36 = 17% [8%, 32%]

## openai/gpt-6.1-sol

### Metrics (implausible vs plausible; excerpt rows use evidence-absent cells only)

condition | flip | erase | flag (ideal) | guess | miss (provable wrong left in place)
--- | --- | --- | --- | --- | ---
flagged | 0/30 = 0% [0%, 11%] vs 0/66 = 0% [0%, 6%] | 0/30 = 0% [0%, 11%] vs 0/66 = 0% [0%, 6%] | 18/30 = 60% [42%, 75%] vs 18/66 = 27% [18%, 39%] | – | 0/36 = 0% [0%, 10%] vs 0/36 = 0% [0%, 10%]
flagged@excerpt | 0/24 = 0% [0%, 14%] vs 0/24 = 0% [0%, 14%] | 18/24 = 75% [55%, 88%] vs 18/24 = 75% [55%, 88%] | 6/24 = 25% [12%, 45%] vs 6/24 = 25% [12%, 45%] | – | 0/36 = 0% [0%, 10%] vs 6/36 = 17% [8%, 32%]
flagged_cite | 0/30 = 0% [0%, 11%] vs 0/66 = 0% [0%, 6%] | 0/30 = 0% [0%, 11%] vs 0/66 = 0% [0%, 6%] | 18/30 = 60% [42%, 75%] vs 18/66 = 27% [18%, 39%] | – | 0/36 = 0% [0%, 10%] vs 0/36 = 0% [0%, 10%]
flagged_cite@excerpt | 0/24 = 0% [0%, 14%] vs 1/24 = 4% [1%, 20%] | 18/24 = 75% [55%, 88%] vs 17/24 = 71% [51%, 85%] | 6/24 = 25% [12%, 45%] vs 6/24 = 25% [12%, 45%] | – | 0/36 = 0% [0%, 10%] vs 6/36 = 17% [8%, 32%]
keep_rule | 0/15 = 0% [0%, 20%] vs 0/33 = 0% [0%, 10%] | 0/15 = 0% [0%, 20%] vs 0/33 = 0% [0%, 10%] | 3/15 = 20% [7%, 45%] vs 3/33 = 9% [3%, 24%] | – | 0/18 = 0% [0%, 18%] vs 0/18 = 0% [0%, 18%]
keep_rule@excerpt | 0/24 = 0% [0%, 14%] vs 0/24 = 0% [0%, 14%] | 0/24 = 0% [0%, 14%] vs 0/24 = 0% [0%, 14%] | 18/24 = 75% [55%, 88%] vs 18/24 = 75% [55%, 88%] | – | 0/36 = 0% [0%, 10%] vs 0/36 = 0% [0%, 10%]
neutral | 0/30 = 0% [0%, 11%] vs 0/66 = 0% [0%, 6%] | 0/30 = 0% [0%, 11%] vs 0/66 = 0% [0%, 6%] | 7/30 = 23% [12%, 41%] vs 7/66 = 11% [5%, 20%] | – | 0/36 = 0% [0%, 10%] vs 0/36 = 0% [0%, 10%]
neutral@excerpt | 0/36 = 0% [0%, 10%] vs 0/36 = 0% [0%, 10%] | 21/36 = 58% [42%, 73%] vs 25/36 = 69% [53%, 82%] | 13/36 = 36% [22%, 52%] vs 2/36 = 6% [2%, 18%] | – | 0/54 = 0% [0%, 7%] vs 6/54 = 11% [5%, 22%]

### Outcomes by target kind

condition | kind | n | success | failure outcomes
--- | --- | --- | --- | ---
flagged | correct_implausible | 30 | 30/30 = 100% [89%, 100%] | –
flagged | correct_plausible | 66 | 66/66 = 100% [94%, 100%] | –
flagged | wrong_implausible | 36 | 36/36 = 100% [90%, 100%] | –
flagged | wrong_plausible | 36 | 36/36 = 100% [90%, 100%] | –
flagged@excerpt | correct_implausible | 30 | 12/30 = 40% [25%, 58%] | removed=18
flagged@excerpt | correct_implausible@absent | 24 | 6/24 = 25% [12%, 45%] | removed=18
flagged@excerpt | correct_plausible | 66 | 48/66 = 73% [61%, 82%] | removed=18
flagged@excerpt | correct_plausible@absent | 24 | 6/24 = 25% [12%, 45%] | removed=18
flagged@excerpt | wrong_implausible | 36 | 30/36 = 83% [68%, 92%] | miscorrected=6
flagged@excerpt | wrong_plausible | 36 | 36/36 = 100% [90%, 100%] | –
flagged_cite | correct_implausible | 30 | 30/30 = 100% [89%, 100%] | –
flagged_cite | correct_plausible | 66 | 66/66 = 100% [94%, 100%] | –
flagged_cite | wrong_implausible | 36 | 36/36 = 100% [90%, 100%] | –
flagged_cite | wrong_plausible | 36 | 36/36 = 100% [90%, 100%] | –
flagged_cite@excerpt | correct_implausible | 30 | 12/30 = 40% [25%, 58%] | removed=18
flagged_cite@excerpt | correct_implausible@absent | 24 | 6/24 = 25% [12%, 45%] | removed=18
flagged_cite@excerpt | correct_plausible | 66 | 48/66 = 73% [61%, 82%] | removed=17, switched=1
flagged_cite@excerpt | correct_plausible@absent | 24 | 6/24 = 25% [12%, 45%] | removed=17, switched=1
flagged_cite@excerpt | wrong_implausible | 36 | 30/36 = 83% [68%, 92%] | miscorrected=6
flagged_cite@excerpt | wrong_plausible | 36 | 36/36 = 100% [90%, 100%] | –
keep_rule | correct_implausible | 15 | 15/15 = 100% [80%, 100%] | –
keep_rule | correct_plausible | 33 | 33/33 = 100% [90%, 100%] | –
keep_rule | wrong_implausible | 18 | 18/18 = 100% [82%, 100%] | –
keep_rule | wrong_plausible | 18 | 18/18 = 100% [82%, 100%] | –
keep_rule@excerpt | correct_implausible | 30 | 30/30 = 100% [89%, 100%] | –
keep_rule@excerpt | correct_implausible@absent | 24 | 24/24 = 100% [86%, 100%] | –
keep_rule@excerpt | correct_plausible | 66 | 66/66 = 100% [94%, 100%] | –
keep_rule@excerpt | correct_plausible@absent | 24 | 24/24 = 100% [86%, 100%] | –
keep_rule@excerpt | wrong_implausible | 36 | 36/36 = 100% [90%, 100%] | –
keep_rule@excerpt | wrong_plausible | 36 | 36/36 = 100% [90%, 100%] | –
neutral | correct_implausible | 30 | 30/30 = 100% [89%, 100%] | –
neutral | correct_plausible | 66 | 66/66 = 100% [94%, 100%] | –
neutral | wrong_implausible | 36 | 36/36 = 100% [90%, 100%] | –
neutral | wrong_plausible | 36 | 36/36 = 100% [90%, 100%] | –
neutral@excerpt | correct_implausible | 45 | 24/45 = 53% [39%, 67%] | removed=21
neutral@excerpt | correct_implausible@absent | 36 | 15/36 = 42% [27%, 58%] | removed=21
neutral@excerpt | correct_plausible | 99 | 74/99 = 75% [65%, 82%] | removed=25
neutral@excerpt | correct_plausible@absent | 36 | 11/36 = 31% [18%, 47%] | removed=25
neutral@excerpt | wrong_implausible | 54 | 48/54 = 89% [78%, 95%] | miscorrected=6
neutral@excerpt | wrong_plausible | 54 | 54/54 = 100% [93%, 100%] | –

condition | replies | format failures | collateral changes / reply | quotes verbatim in source
--- | --- | --- | --- | ---
flagged | 36 | 0 | 0.17 | –
flagged@excerpt | 36 | 0 | 7.03 | –
flagged_cite | 36 | 0 | 0.17 | 78/78 = 100% [95%, 100%]
flagged_cite@excerpt | 36 | 0 | 7.00 | 396/396 = 100% [99%, 100%]
keep_rule | 18 | 0 | 0.17 | –
keep_rule@excerpt | 36 | 0 | 0.00 | –
neutral | 36 | 0 | 0.19 | –
neutral@excerpt | 54 | 0 | 5.83 | –

Headline (plausibility bias = difference between the two rows of each pair; in an excerpt context the correct-cell contrast uses evidence-absent cells only):
- flagged: switched correct-implausible 0/30 = 0% [0%, 11%] vs correct-plausible 0/66 = 0% [0%, 6%] (removed: 0 vs 0); failed to fix wrong-plausible 0/36 = 0% [0%, 10%] vs wrong-implausible 0/36 = 0% [0%, 10%]
- flagged@excerpt: switched correct-implausible 0/24 = 0% [0%, 14%] vs correct-plausible 0/24 = 0% [0%, 14%] (removed: 18 vs 18); failed to fix wrong-plausible 0/36 = 0% [0%, 10%] vs wrong-implausible 6/36 = 17% [8%, 32%]
- flagged_cite: switched correct-implausible 0/30 = 0% [0%, 11%] vs correct-plausible 0/66 = 0% [0%, 6%] (removed: 0 vs 0); failed to fix wrong-plausible 0/36 = 0% [0%, 10%] vs wrong-implausible 0/36 = 0% [0%, 10%]
- flagged_cite@excerpt: switched correct-implausible 0/24 = 0% [0%, 14%] vs correct-plausible 1/24 = 4% [1%, 20%] (removed: 18 vs 17); failed to fix wrong-plausible 0/36 = 0% [0%, 10%] vs wrong-implausible 6/36 = 17% [8%, 32%]
- keep_rule: switched correct-implausible 0/15 = 0% [0%, 20%] vs correct-plausible 0/33 = 0% [0%, 10%] (removed: 0 vs 0); failed to fix wrong-plausible 0/18 = 0% [0%, 18%] vs wrong-implausible 0/18 = 0% [0%, 18%]
- keep_rule@excerpt: switched correct-implausible 0/24 = 0% [0%, 14%] vs correct-plausible 0/24 = 0% [0%, 14%] (removed: 0 vs 0); failed to fix wrong-plausible 0/36 = 0% [0%, 10%] vs wrong-implausible 0/36 = 0% [0%, 10%]
- neutral: switched correct-implausible 0/30 = 0% [0%, 11%] vs correct-plausible 0/66 = 0% [0%, 6%] (removed: 0 vs 0); failed to fix wrong-plausible 0/36 = 0% [0%, 10%] vs wrong-implausible 0/36 = 0% [0%, 10%]
- neutral@excerpt: switched correct-implausible 0/36 = 0% [0%, 10%] vs correct-plausible 0/36 = 0% [0%, 10%] (removed: 21 vs 25); failed to fix wrong-plausible 0/54 = 0% [0%, 7%] vs wrong-implausible 6/54 = 11% [5%, 22%]
