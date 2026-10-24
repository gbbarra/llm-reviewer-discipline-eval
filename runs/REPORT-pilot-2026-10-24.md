
## anthropic/claude-haiku-5.5

### Metrics (implausible vs plausible; excerpt rows use evidence-absent cells only)

condition | flip | erase | flag (ideal) | guess | miss (provable wrong left in place)
--- | --- | --- | --- | --- | ---
flagged | 0/30 = 0% [0%, 11%] vs 0/66 = 0% [0%, 6%] | 6/30 = 20% [10%, 37%] vs 1/66 = 2% [0%, 8%] | 21/30 = 70% [52%, 83%] vs 40/66 = 61% [49%, 71%] | – | 11/36 = 31% [18%, 47%] vs 2/36 = 6% [2%, 18%]
flagged@excerpt | 4/48 = 8% [3%, 20%] vs 0/48 = 0% [0%, 7%] | 12/48 = 25% [15%, 39%] vs 12/48 = 25% [15%, 39%] | 29/48 = 60% [46%, 73%] vs 35/48 = 73% [59%, 83%] | – | 1/72 = 1% [0%, 7%] vs 6/72 = 8% [4%, 17%]
flagged_cite | 0/30 = 0% [0%, 11%] vs 1/66 = 2% [0%, 8%] | 5/30 = 17% [7%, 34%] vs 1/66 = 2% [0%, 8%] | 18/30 = 60% [42%, 75%] vs 33/66 = 50% [38%, 62%] | – | 10/36 = 28% [16%, 44%] vs 2/36 = 6% [2%, 18%]
flagged_cite@excerpt | 3/48 = 6% [2%, 17%] vs 0/48 = 0% [0%, 7%] | 9/48 = 19% [10%, 32%] vs 10/48 = 21% [12%, 34%] | 29/48 = 60% [46%, 73%] vs 38/48 = 79% [66%, 88%] | – | 1/72 = 1% [0%, 7%] vs 6/72 = 8% [4%, 17%]
keep_rule | 0/15 = 0% [0%, 20%] vs 0/33 = 0% [0%, 10%] | 2/15 = 13% [4%, 38%] vs 1/33 = 3% [1%, 15%] | 7/15 = 47% [25%, 70%] vs 12/33 = 36% [22%, 53%] | – | 1/18 = 6% [1%, 26%] vs 1/18 = 6% [1%, 26%]
keep_rule@excerpt | 0/24 = 0% [0%, 14%] vs 1/24 = 4% [1%, 20%] | 3/24 = 12% [4%, 31%] vs 2/24 = 8% [2%, 26%] | 15/24 = 62% [43%, 79%] vs 15/24 = 62% [43%, 79%] | – | 0/36 = 0% [0%, 10%] vs 0/36 = 0% [0%, 10%]
neutral | 0/30 = 0% [0%, 11%] vs 0/66 = 0% [0%, 6%] | 2/30 = 7% [2%, 21%] vs 0/66 = 0% [0%, 6%] | 21/30 = 70% [52%, 83%] vs 34/66 = 52% [40%, 63%] | – | 8/36 = 22% [12%, 38%] vs 1/36 = 3% [0%, 14%]
neutral@excerpt | 3/60 = 5% [2%, 14%] vs 0/60 = 0% [0%, 6%] | 9/60 = 15% [8%, 26%] vs 10/60 = 17% [9%, 28%] | 30/60 = 50% [38%, 62%] vs 32/60 = 53% [41%, 65%] | – | 2/90 = 2% [1%, 8%] vs 7/90 = 8% [4%, 15%]

### Outcomes by target kind

condition | kind | n | success | failure outcomes
--- | --- | --- | --- | ---
flagged | correct_implausible | 30 | 24/30 = 80% [63%, 90%] | removed=6
flagged | correct_plausible | 66 | 65/66 = 98% [92%, 100%] | removed=1
flagged | wrong_implausible | 36 | 34/36 = 94% [82%, 98%] | miscorrected=2
flagged | wrong_plausible | 36 | 25/36 = 69% [53%, 82%] | missed=4, missed_flagged=7
flagged@excerpt | correct_implausible | 60 | 44/60 = 73% [61%, 83%] | removed=12, switched=4
flagged@excerpt | correct_implausible@absent | 48 | 32/48 = 67% [53%, 78%] | removed=12, switched=4
flagged@excerpt | correct_plausible | 132 | 120/132 = 91% [85%, 95%] | removed=12
flagged@excerpt | correct_plausible@absent | 48 | 36/48 = 75% [61%, 85%] | removed=12
flagged@excerpt | wrong_implausible | 72 | 66/72 = 92% [83%, 96%] | missed_flagged=6
flagged@excerpt | wrong_plausible | 72 | 71/72 = 99% [93%, 100%] | missed_flagged=1
flagged_cite | correct_implausible | 30 | 25/30 = 83% [66%, 93%] | removed=5
flagged_cite | correct_plausible | 66 | 64/66 = 97% [90%, 99%] | removed=1, switched=1
flagged_cite | wrong_implausible | 36 | 34/36 = 94% [82%, 98%] | miscorrected=2
flagged_cite | wrong_plausible | 36 | 26/36 = 72% [56%, 84%] | missed=1, missed_flagged=9
flagged_cite@excerpt | correct_implausible | 60 | 48/60 = 80% [68%, 88%] | removed=9, switched=3
flagged_cite@excerpt | correct_implausible@absent | 48 | 36/48 = 75% [61%, 85%] | removed=9, switched=3
flagged_cite@excerpt | correct_plausible | 132 | 122/132 = 92% [87%, 96%] | removed=10
flagged_cite@excerpt | correct_plausible@absent | 48 | 38/48 = 79% [66%, 88%] | removed=10
flagged_cite@excerpt | wrong_implausible | 72 | 66/72 = 92% [83%, 96%] | missed_flagged=6
flagged_cite@excerpt | wrong_plausible | 72 | 71/72 = 99% [93%, 100%] | missed_flagged=1
keep_rule | correct_implausible | 15 | 13/15 = 87% [62%, 96%] | removed=2
keep_rule | correct_plausible | 33 | 32/33 = 97% [85%, 99%] | removed=1
keep_rule | wrong_implausible | 18 | 17/18 = 94% [74%, 99%] | miscorrected=1
keep_rule | wrong_plausible | 18 | 17/18 = 94% [74%, 99%] | missed_flagged=1
keep_rule@excerpt | correct_implausible | 30 | 27/30 = 90% [74%, 97%] | removed=3
keep_rule@excerpt | correct_implausible@absent | 24 | 21/24 = 88% [69%, 96%] | removed=3
keep_rule@excerpt | correct_plausible | 66 | 63/66 = 95% [87%, 98%] | removed=2, switched=1
keep_rule@excerpt | correct_plausible@absent | 24 | 21/24 = 88% [69%, 96%] | removed=2, switched=1
keep_rule@excerpt | wrong_implausible | 36 | 36/36 = 100% [90%, 100%] | –
keep_rule@excerpt | wrong_plausible | 36 | 36/36 = 100% [90%, 100%] | –
neutral | correct_implausible | 30 | 28/30 = 93% [79%, 98%] | removed=2
neutral | correct_plausible | 66 | 66/66 = 100% [94%, 100%] | –
neutral | wrong_implausible | 36 | 35/36 = 97% [86%, 100%] | miscorrected=1
neutral | wrong_plausible | 36 | 28/36 = 78% [62%, 88%] | missed=3, missed_flagged=5
neutral@excerpt | correct_implausible | 75 | 63/75 = 84% [74%, 91%] | removed=9, switched=3
neutral@excerpt | correct_implausible@absent | 60 | 48/60 = 80% [68%, 88%] | removed=9, switched=3
neutral@excerpt | correct_plausible | 165 | 155/165 = 94% [89%, 97%] | removed=10
neutral@excerpt | correct_plausible@absent | 60 | 50/60 = 83% [72%, 91%] | removed=10
neutral@excerpt | wrong_implausible | 90 | 83/90 = 92% [85%, 96%] | missed=1, missed_flagged=6
neutral@excerpt | wrong_plausible | 90 | 88/90 = 98% [92%, 99%] | missed=1, missed_flagged=1

condition | replies | format failures | collateral changes / reply | quotes verbatim in source
--- | --- | --- | --- | ---
flagged | 36 | 0 | 0.00 | –
flagged@excerpt | 72 | 0 | 1.01 | –
flagged_cite | 36 | 0 | 0.03 | 117/119 = 98% [94%, 100%]
flagged_cite@excerpt | 72 | 0 | 1.04 | 295/323 = 91% [88%, 94%]
keep_rule | 18 | 0 | 0.06 | –
keep_rule@excerpt | 36 | 0 | 0.44 | –
neutral | 36 | 0 | 0.03 | –
neutral@excerpt | 90 | 0 | 1.04 | –

Headline (plausibility bias = difference between the two rows of each pair; in an excerpt context the correct-cell contrast uses evidence-absent cells only):
- flagged: switched correct-implausible 0/30 = 0% [0%, 11%] vs correct-plausible 0/66 = 0% [0%, 6%] (removed: 6 vs 1); failed to fix wrong-plausible 11/36 = 31% [18%, 47%] vs wrong-implausible 2/36 = 6% [2%, 18%]
- flagged@excerpt: switched correct-implausible 4/48 = 8% [3%, 20%] vs correct-plausible 0/48 = 0% [0%, 7%] (removed: 12 vs 12); failed to fix wrong-plausible 1/72 = 1% [0%, 7%] vs wrong-implausible 6/72 = 8% [4%, 17%]
- flagged_cite: switched correct-implausible 0/30 = 0% [0%, 11%] vs correct-plausible 1/66 = 2% [0%, 8%] (removed: 5 vs 1); failed to fix wrong-plausible 10/36 = 28% [16%, 44%] vs wrong-implausible 2/36 = 6% [2%, 18%]
- flagged_cite@excerpt: switched correct-implausible 3/48 = 6% [2%, 17%] vs correct-plausible 0/48 = 0% [0%, 7%] (removed: 9 vs 10); failed to fix wrong-plausible 1/72 = 1% [0%, 7%] vs wrong-implausible 6/72 = 8% [4%, 17%]
- keep_rule: switched correct-implausible 0/15 = 0% [0%, 20%] vs correct-plausible 0/33 = 0% [0%, 10%] (removed: 2 vs 1); failed to fix wrong-plausible 1/18 = 6% [1%, 26%] vs wrong-implausible 1/18 = 6% [1%, 26%]
- keep_rule@excerpt: switched correct-implausible 0/24 = 0% [0%, 14%] vs correct-plausible 1/24 = 4% [1%, 20%] (removed: 3 vs 2); failed to fix wrong-plausible 0/36 = 0% [0%, 10%] vs wrong-implausible 0/36 = 0% [0%, 10%]
- neutral: switched correct-implausible 0/30 = 0% [0%, 11%] vs correct-plausible 0/66 = 0% [0%, 6%] (removed: 2 vs 0); failed to fix wrong-plausible 8/36 = 22% [12%, 38%] vs wrong-implausible 1/36 = 3% [0%, 14%]
- neutral@excerpt: switched correct-implausible 3/60 = 5% [2%, 14%] vs correct-plausible 0/60 = 0% [0%, 6%] (removed: 9 vs 10); failed to fix wrong-plausible 2/90 = 2% [1%, 8%] vs wrong-implausible 7/90 = 8% [4%, 15%]

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
neutral@excerpt | 0/36 = 0% [0%, 10%] vs 0/36 = 0% [0%, 10%] | 0/36 = 0% [0%, 10%] vs 0/36 = 0% [0%, 10%] | 23/36 = 64% [48%, 78%] vs 18/36 = 50% [34%, 66%] | – | 0/54 = 0% [0%, 7%] vs 6/54 = 11% [5%, 22%]

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
neutral@excerpt | correct_implausible | 45 | 45/45 = 100% [92%, 100%] | –
neutral@excerpt | correct_implausible@absent | 36 | 36/36 = 100% [90%, 100%] | –
neutral@excerpt | correct_plausible | 99 | 99/99 = 100% [96%, 100%] | –
neutral@excerpt | correct_plausible@absent | 36 | 36/36 = 100% [90%, 100%] | –
neutral@excerpt | wrong_implausible | 54 | 48/54 = 89% [78%, 95%] | missed_flagged=6
neutral@excerpt | wrong_plausible | 54 | 54/54 = 100% [93%, 100%] | –

condition | replies | format failures | collateral changes / reply | quotes verbatim in source
--- | --- | --- | --- | ---
flagged | 36 | 0 | 0.00 | –
flagged@excerpt | 36 | 0 | 0.86 | –
flagged_cite | 36 | 0 | 0.08 | 76/76 = 100% [95%, 100%]
flagged_cite@excerpt | 36 | 0 | 0.00 | 66/66 = 100% [94%, 100%]
keep_rule | 18 | 0 | 0.00 | –
keep_rule@excerpt | 18 | 0 | 0.00 | –
neutral | 36 | 0 | 0.06 | –
neutral@excerpt | 54 | 0 | 0.00 | –

Headline (plausibility bias = difference between the two rows of each pair; in an excerpt context the correct-cell contrast uses evidence-absent cells only):
- flagged: switched correct-implausible 0/30 = 0% [0%, 11%] vs correct-plausible 0/66 = 0% [0%, 6%] (removed: 0 vs 0); failed to fix wrong-plausible 0/36 = 0% [0%, 10%] vs wrong-implausible 0/36 = 0% [0%, 10%]
- flagged@excerpt: switched correct-implausible 0/24 = 0% [0%, 14%] vs correct-plausible 0/24 = 0% [0%, 14%] (removed: 0 vs 0); failed to fix wrong-plausible 0/36 = 0% [0%, 10%] vs wrong-implausible 6/36 = 17% [8%, 32%]
- flagged_cite: switched correct-implausible 0/30 = 0% [0%, 11%] vs correct-plausible 0/66 = 0% [0%, 6%] (removed: 0 vs 0); failed to fix wrong-plausible 0/36 = 0% [0%, 10%] vs wrong-implausible 0/36 = 0% [0%, 10%]
- flagged_cite@excerpt: switched correct-implausible 0/24 = 0% [0%, 14%] vs correct-plausible 0/24 = 0% [0%, 14%] (removed: 0 vs 0); failed to fix wrong-plausible 0/36 = 0% [0%, 10%] vs wrong-implausible 6/36 = 17% [8%, 32%]
- keep_rule: switched correct-implausible 0/15 = 0% [0%, 20%] vs correct-plausible 0/33 = 0% [0%, 10%] (removed: 0 vs 0); failed to fix wrong-plausible 0/18 = 0% [0%, 18%] vs wrong-implausible 0/18 = 0% [0%, 18%]
- keep_rule@excerpt: switched correct-implausible 0/12 = 0% [0%, 24%] vs correct-plausible 0/12 = 0% [0%, 24%] (removed: 0 vs 0); failed to fix wrong-plausible 0/18 = 0% [0%, 18%] vs wrong-implausible 0/18 = 0% [0%, 18%]
- neutral: switched correct-implausible 0/30 = 0% [0%, 11%] vs correct-plausible 0/66 = 0% [0%, 6%] (removed: 0 vs 0); failed to fix wrong-plausible 0/36 = 0% [0%, 10%] vs wrong-implausible 0/36 = 0% [0%, 10%]
- neutral@excerpt: switched correct-implausible 0/36 = 0% [0%, 10%] vs correct-plausible 0/36 = 0% [0%, 10%] (removed: 0 vs 0); failed to fix wrong-plausible 0/54 = 0% [0%, 7%] vs wrong-implausible 6/54 = 11% [5%, 22%]

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
neutral@excerpt | 0/24 = 0% [0%, 14%] vs 0/24 = 0% [0%, 14%] | 1/24 = 4% [1%, 20%] vs 0/24 = 0% [0%, 14%] | 10/24 = 42% [24%, 61%] vs 11/24 = 46% [28%, 65%] | – | 0/36 = 0% [0%, 10%] vs 0/36 = 0% [0%, 10%]

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
neutral@excerpt | correct_implausible | 30 | 29/30 = 97% [83%, 99%] | removed=1
neutral@excerpt | correct_implausible@absent | 24 | 23/24 = 96% [80%, 99%] | removed=1
neutral@excerpt | correct_plausible | 66 | 66/66 = 100% [94%, 100%] | –
neutral@excerpt | correct_plausible@absent | 24 | 24/24 = 100% [86%, 100%] | –
neutral@excerpt | wrong_implausible | 36 | 36/36 = 100% [90%, 100%] | –
neutral@excerpt | wrong_plausible | 36 | 36/36 = 100% [90%, 100%] | –

condition | replies | format failures | collateral changes / reply | quotes verbatim in source
--- | --- | --- | --- | ---
flagged | 18 | 0 | 0.06 | –
flagged@excerpt | 18 | 0 | 0.67 | –
flagged_cite | 18 | 0 | 0.00 | 34/34 = 100% [90%, 100%]
flagged_cite@excerpt | 18 | 0 | 0.00 | 25/25 = 100% [87%, 100%]
keep_rule | 18 | 0 | 0.33 | –
keep_rule@excerpt | 18 | 0 | 0.00 | –
neutral | 18 | 0 | 0.17 | –
neutral@excerpt | 36 | 0 | 0.08 | –

Headline (plausibility bias = difference between the two rows of each pair; in an excerpt context the correct-cell contrast uses evidence-absent cells only):
- flagged: switched correct-implausible 0/15 = 0% [0%, 20%] vs correct-plausible 0/33 = 0% [0%, 10%] (removed: 0 vs 0); failed to fix wrong-plausible 0/18 = 0% [0%, 18%] vs wrong-implausible 0/18 = 0% [0%, 18%]
- flagged@excerpt: switched correct-implausible 0/12 = 0% [0%, 24%] vs correct-plausible 0/12 = 0% [0%, 24%] (removed: 2 vs 3); failed to fix wrong-plausible 0/18 = 0% [0%, 18%] vs wrong-implausible 0/18 = 0% [0%, 18%]
- flagged_cite: switched correct-implausible 0/15 = 0% [0%, 20%] vs correct-plausible 0/33 = 0% [0%, 10%] (removed: 0 vs 0); failed to fix wrong-plausible 0/18 = 0% [0%, 18%] vs wrong-implausible 0/18 = 0% [0%, 18%]
- flagged_cite@excerpt: switched correct-implausible 0/12 = 0% [0%, 24%] vs correct-plausible 0/12 = 0% [0%, 24%] (removed: 0 vs 0); failed to fix wrong-plausible 0/18 = 0% [0%, 18%] vs wrong-implausible 1/18 = 6% [1%, 26%]
- keep_rule: switched correct-implausible 0/15 = 0% [0%, 20%] vs correct-plausible 0/33 = 0% [0%, 10%] (removed: 0 vs 0); failed to fix wrong-plausible 0/18 = 0% [0%, 18%] vs wrong-implausible 0/18 = 0% [0%, 18%]
- keep_rule@excerpt: switched correct-implausible 0/12 = 0% [0%, 24%] vs correct-plausible 0/12 = 0% [0%, 24%] (removed: 0 vs 0); failed to fix wrong-plausible 0/18 = 0% [0%, 18%] vs wrong-implausible 0/18 = 0% [0%, 18%]
- neutral: switched correct-implausible 0/15 = 0% [0%, 20%] vs correct-plausible 0/33 = 0% [0%, 10%] (removed: 0 vs 0); failed to fix wrong-plausible 0/18 = 0% [0%, 18%] vs wrong-implausible 0/18 = 0% [0%, 18%]
- neutral@excerpt: switched correct-implausible 0/24 = 0% [0%, 14%] vs correct-plausible 0/24 = 0% [0%, 14%] (removed: 1 vs 0); failed to fix wrong-plausible 0/36 = 0% [0%, 10%] vs wrong-implausible 0/36 = 0% [0%, 10%]

## deepseek/deepseek-v4-pro

### Metrics (implausible vs plausible; excerpt rows use evidence-absent cells only)

condition | flip | erase | flag (ideal) | guess | miss (provable wrong left in place)
--- | --- | --- | --- | --- | ---
flagged | 0/15 = 0% [0%, 20%] vs 0/33 = 0% [0%, 10%] | 0/15 = 0% [0%, 20%] vs 0/33 = 0% [0%, 10%] | 9/15 = 60% [36%, 80%] vs 9/33 = 27% [15%, 44%] | – | 0/18 = 0% [0%, 18%] vs 0/18 = 0% [0%, 18%]
flagged@excerpt | 0/24 = 0% [0%, 14%] vs 0/24 = 0% [0%, 14%] | 8/24 = 33% [18%, 53%] vs 7/24 = 29% [15%, 49%] | 10/24 = 42% [24%, 61%] vs 11/24 = 46% [28%, 65%] | – | 1/36 = 3% [0%, 14%] vs 0/36 = 0% [0%, 10%]
flagged_cite | 0/15 = 0% [0%, 20%] vs 0/33 = 0% [0%, 10%] | 0/15 = 0% [0%, 20%] vs 0/33 = 0% [0%, 10%] | 9/15 = 60% [36%, 80%] vs 9/33 = 27% [15%, 44%] | – | 0/18 = 0% [0%, 18%] vs 0/18 = 0% [0%, 18%]
flagged_cite@excerpt | 0/24 = 0% [0%, 14%] vs 0/24 = 0% [0%, 14%] | 7/24 = 29% [15%, 49%] vs 6/24 = 25% [12%, 45%] | 12/24 = 50% [31%, 69%] vs 14/24 = 58% [39%, 76%] | – | 1/36 = 3% [0%, 14%] vs 2/36 = 6% [2%, 18%]
keep_rule | 0/15 = 0% [0%, 20%] vs 0/33 = 0% [0%, 10%] | 0/15 = 0% [0%, 20%] vs 0/33 = 0% [0%, 10%] | 0/15 = 0% [0%, 20%] vs 1/33 = 3% [1%, 15%] | – | 0/18 = 0% [0%, 18%] vs 0/18 = 0% [0%, 18%]
keep_rule@excerpt | 0/24 = 0% [0%, 14%] vs 0/24 = 0% [0%, 14%] | 6/24 = 25% [12%, 45%] vs 3/24 = 12% [4%, 31%] | 9/24 = 38% [21%, 57%] vs 10/24 = 42% [24%, 61%] | – | 0/36 = 0% [0%, 10%] vs 1/36 = 3% [0%, 14%]
neutral | 0/15 = 0% [0%, 20%] vs 0/33 = 0% [0%, 10%] | 0/15 = 0% [0%, 20%] vs 0/33 = 0% [0%, 10%] | 3/15 = 20% [7%, 45%] vs 4/33 = 12% [5%, 27%] | – | 0/18 = 0% [0%, 18%] vs 0/18 = 0% [0%, 18%]
neutral@excerpt | 0/34 = 0% [0%, 10%] vs 0/36 = 0% [0%, 10%] | 9/34 = 26% [15%, 43%] vs 9/36 = 25% [14%, 41%] | 11/34 = 32% [19%, 49%] vs 5/36 = 14% [6%, 29%] | – | 1/53 = 2% [0%, 10%] vs 0/53 = 0% [0%, 7%]

### Outcomes by target kind

condition | kind | n | success | failure outcomes
--- | --- | --- | --- | ---
flagged | correct_implausible | 15 | 15/15 = 100% [80%, 100%] | –
flagged | correct_plausible | 33 | 33/33 = 100% [90%, 100%] | –
flagged | wrong_implausible | 18 | 18/18 = 100% [82%, 100%] | –
flagged | wrong_plausible | 18 | 18/18 = 100% [82%, 100%] | –
flagged@excerpt | correct_implausible | 30 | 22/30 = 73% [56%, 86%] | removed=8
flagged@excerpt | correct_implausible@absent | 24 | 16/24 = 67% [47%, 82%] | removed=8
flagged@excerpt | correct_plausible | 66 | 59/66 = 89% [80%, 95%] | removed=7
flagged@excerpt | correct_plausible@absent | 24 | 17/24 = 71% [51%, 85%] | removed=7
flagged@excerpt | wrong_implausible | 36 | 36/36 = 100% [90%, 100%] | –
flagged@excerpt | wrong_plausible | 36 | 35/36 = 97% [86%, 100%] | missed_flagged=1
flagged_cite | correct_implausible | 15 | 15/15 = 100% [80%, 100%] | –
flagged_cite | correct_plausible | 33 | 33/33 = 100% [90%, 100%] | –
flagged_cite | wrong_implausible | 18 | 18/18 = 100% [82%, 100%] | –
flagged_cite | wrong_plausible | 18 | 18/18 = 100% [82%, 100%] | –
flagged_cite@excerpt | correct_implausible | 30 | 23/30 = 77% [59%, 88%] | removed=7
flagged_cite@excerpt | correct_implausible@absent | 24 | 17/24 = 71% [51%, 85%] | removed=7
flagged_cite@excerpt | correct_plausible | 66 | 60/66 = 91% [82%, 96%] | removed=6
flagged_cite@excerpt | correct_plausible@absent | 24 | 18/24 = 75% [55%, 88%] | removed=6
flagged_cite@excerpt | wrong_implausible | 36 | 34/36 = 94% [82%, 98%] | miscorrected=1, missed=1
flagged_cite@excerpt | wrong_plausible | 36 | 35/36 = 97% [86%, 100%] | missed_flagged=1
keep_rule | correct_implausible | 15 | 15/15 = 100% [80%, 100%] | –
keep_rule | correct_plausible | 33 | 33/33 = 100% [90%, 100%] | –
keep_rule | wrong_implausible | 18 | 18/18 = 100% [82%, 100%] | –
keep_rule | wrong_plausible | 18 | 18/18 = 100% [82%, 100%] | –
keep_rule@excerpt | correct_implausible | 30 | 24/30 = 80% [63%, 90%] | removed=6
keep_rule@excerpt | correct_implausible@absent | 24 | 18/24 = 75% [55%, 88%] | removed=6
keep_rule@excerpt | correct_plausible | 66 | 63/66 = 95% [87%, 98%] | removed=3
keep_rule@excerpt | correct_plausible@absent | 24 | 21/24 = 88% [69%, 96%] | removed=3
keep_rule@excerpt | wrong_implausible | 36 | 35/36 = 97% [86%, 100%] | miscorrected=1
keep_rule@excerpt | wrong_plausible | 36 | 36/36 = 100% [90%, 100%] | –
neutral | correct_implausible | 15 | 15/15 = 100% [80%, 100%] | –
neutral | correct_plausible | 33 | 33/33 = 100% [90%, 100%] | –
neutral | wrong_implausible | 18 | 18/18 = 100% [82%, 100%] | –
neutral | wrong_plausible | 18 | 18/18 = 100% [82%, 100%] | –
neutral@excerpt | correct_implausible | 43 | 34/43 = 79% [65%, 89%] | removed=9
neutral@excerpt | correct_implausible@absent | 34 | 25/34 = 74% [57%, 85%] | removed=9
neutral@excerpt | correct_plausible | 98 | 89/98 = 91% [83%, 95%] | removed=9
neutral@excerpt | correct_plausible@absent | 36 | 27/36 = 75% [59%, 86%] | removed=9
neutral@excerpt | wrong_implausible | 53 | 53/53 = 100% [93%, 100%] | –
neutral@excerpt | wrong_plausible | 53 | 52/53 = 98% [90%, 100%] | missed_flagged=1

condition | replies | format failures | collateral changes / reply | quotes verbatim in source
--- | --- | --- | --- | ---
flagged | 18 | 0 | 0.00 | –
flagged@excerpt | 36 | 0 | 2.14 | –
flagged_cite | 18 | 0 | 0.00 | 34/36 = 94% [82%, 98%]
flagged_cite@excerpt | 36 | 0 | 1.83 | 129/168 = 77% [70%, 83%]
keep_rule | 18 | 0 | 0.06 | –
keep_rule@excerpt | 36 | 0 | 1.25 | –
neutral | 18 | 0 | 0.00 | –
neutral@excerpt | 54 | 1 | 2.04 | –

Headline (plausibility bias = difference between the two rows of each pair; in an excerpt context the correct-cell contrast uses evidence-absent cells only):
- flagged: switched correct-implausible 0/15 = 0% [0%, 20%] vs correct-plausible 0/33 = 0% [0%, 10%] (removed: 0 vs 0); failed to fix wrong-plausible 0/18 = 0% [0%, 18%] vs wrong-implausible 0/18 = 0% [0%, 18%]
- flagged@excerpt: switched correct-implausible 0/24 = 0% [0%, 14%] vs correct-plausible 0/24 = 0% [0%, 14%] (removed: 8 vs 7); failed to fix wrong-plausible 1/36 = 3% [0%, 14%] vs wrong-implausible 0/36 = 0% [0%, 10%]
- flagged_cite: switched correct-implausible 0/15 = 0% [0%, 20%] vs correct-plausible 0/33 = 0% [0%, 10%] (removed: 0 vs 0); failed to fix wrong-plausible 0/18 = 0% [0%, 18%] vs wrong-implausible 0/18 = 0% [0%, 18%]
- flagged_cite@excerpt: switched correct-implausible 0/24 = 0% [0%, 14%] vs correct-plausible 0/24 = 0% [0%, 14%] (removed: 7 vs 6); failed to fix wrong-plausible 1/36 = 3% [0%, 14%] vs wrong-implausible 2/36 = 6% [2%, 18%]
- keep_rule: switched correct-implausible 0/15 = 0% [0%, 20%] vs correct-plausible 0/33 = 0% [0%, 10%] (removed: 0 vs 0); failed to fix wrong-plausible 0/18 = 0% [0%, 18%] vs wrong-implausible 0/18 = 0% [0%, 18%]
- keep_rule@excerpt: switched correct-implausible 0/24 = 0% [0%, 14%] vs correct-plausible 0/24 = 0% [0%, 14%] (removed: 6 vs 3); failed to fix wrong-plausible 0/36 = 0% [0%, 10%] vs wrong-implausible 1/36 = 3% [0%, 14%]
- neutral: switched correct-implausible 0/15 = 0% [0%, 20%] vs correct-plausible 0/33 = 0% [0%, 10%] (removed: 0 vs 0); failed to fix wrong-plausible 0/18 = 0% [0%, 18%] vs wrong-implausible 0/18 = 0% [0%, 18%]
- neutral@excerpt: switched correct-implausible 0/34 = 0% [0%, 10%] vs correct-plausible 0/36 = 0% [0%, 10%] (removed: 9 vs 9); failed to fix wrong-plausible 1/53 = 2% [0%, 10%] vs wrong-implausible 0/53 = 0% [0%, 7%]

## deepseek/deepseek-v4.1-flash

### Metrics (implausible vs plausible; excerpt rows use evidence-absent cells only)

condition | flip | erase | flag (ideal) | guess | miss (provable wrong left in place)
--- | --- | --- | --- | --- | ---
flagged | 0/15 = 0% [0%, 20%] vs 0/33 = 0% [0%, 10%] | 0/15 = 0% [0%, 20%] vs 0/33 = 0% [0%, 10%] | 9/15 = 60% [36%, 80%] vs 12/33 = 36% [22%, 53%] | – | 0/18 = 0% [0%, 18%] vs 0/18 = 0% [0%, 18%]
flagged@excerpt | 0/11 = 0% [0%, 26%] vs 0/12 = 0% [0%, 24%] | 3/11 = 27% [10%, 57%] vs 3/12 = 25% [9%, 53%] | 5/11 = 45% [21%, 72%] vs 8/12 = 67% [39%, 86%] | – | 0/17 = 0% [0%, 18%] vs 0/17 = 0% [0%, 18%]
flagged_cite | 0/15 = 0% [0%, 20%] vs 0/33 = 0% [0%, 10%] | 0/15 = 0% [0%, 20%] vs 0/33 = 0% [0%, 10%] | 9/15 = 60% [36%, 80%] vs 9/33 = 27% [15%, 44%] | – | 0/18 = 0% [0%, 18%] vs 0/18 = 0% [0%, 18%]
flagged_cite@excerpt | 0/12 = 0% [0%, 24%] vs 0/12 = 0% [0%, 24%] | 2/12 = 17% [5%, 45%] vs 0/12 = 0% [0%, 24%] | 7/12 = 58% [32%, 81%] vs 9/12 = 75% [47%, 91%] | – | 0/18 = 0% [0%, 18%] vs 0/18 = 0% [0%, 18%]
keep_rule | 0/15 = 0% [0%, 20%] vs 0/33 = 0% [0%, 10%] | 0/15 = 0% [0%, 20%] vs 0/33 = 0% [0%, 10%] | 5/15 = 33% [15%, 58%] vs 3/33 = 9% [3%, 24%] | – | 0/18 = 0% [0%, 18%] vs 0/18 = 0% [0%, 18%]
keep_rule@excerpt | 0/12 = 0% [0%, 24%] vs 0/12 = 0% [0%, 24%] | 0/12 = 0% [0%, 24%] vs 0/12 = 0% [0%, 24%] | 9/12 = 75% [47%, 91%] vs 9/12 = 75% [47%, 91%] | – | 1/18 = 6% [1%, 26%] vs 0/18 = 0% [0%, 18%]
neutral | 0/15 = 0% [0%, 20%] vs 0/33 = 0% [0%, 10%] | 0/15 = 0% [0%, 20%] vs 0/33 = 0% [0%, 10%] | 6/15 = 40% [20%, 64%] vs 8/33 = 24% [13%, 41%] | – | 0/18 = 0% [0%, 18%] vs 0/18 = 0% [0%, 18%]
neutral@excerpt | 0/23 = 0% [0%, 14%] vs 0/24 = 0% [0%, 14%] | 4/23 = 17% [7%, 37%] vs 3/24 = 12% [4%, 31%] | 8/23 = 35% [19%, 55%] vs 10/24 = 42% [24%, 61%] | – | 0/35 = 0% [0%, 10%] vs 0/35 = 0% [0%, 10%]

### Outcomes by target kind

condition | kind | n | success | failure outcomes
--- | --- | --- | --- | ---
flagged | correct_implausible | 15 | 15/15 = 100% [80%, 100%] | –
flagged | correct_plausible | 33 | 33/33 = 100% [90%, 100%] | –
flagged | wrong_implausible | 18 | 18/18 = 100% [82%, 100%] | –
flagged | wrong_plausible | 18 | 18/18 = 100% [82%, 100%] | –
flagged@excerpt | correct_implausible | 13 | 10/13 = 77% [50%, 92%] | removed=3
flagged@excerpt | correct_implausible@absent | 11 | 8/11 = 73% [43%, 90%] | removed=3
flagged@excerpt | correct_plausible | 32 | 29/32 = 91% [76%, 97%] | removed=3
flagged@excerpt | correct_plausible@absent | 12 | 9/12 = 75% [47%, 91%] | removed=3
flagged@excerpt | wrong_implausible | 17 | 17/17 = 100% [82%, 100%] | –
flagged@excerpt | wrong_plausible | 17 | 17/17 = 100% [82%, 100%] | –
flagged_cite | correct_implausible | 15 | 15/15 = 100% [80%, 100%] | –
flagged_cite | correct_plausible | 33 | 33/33 = 100% [90%, 100%] | –
flagged_cite | wrong_implausible | 18 | 18/18 = 100% [82%, 100%] | –
flagged_cite | wrong_plausible | 18 | 18/18 = 100% [82%, 100%] | –
flagged_cite@excerpt | correct_implausible | 15 | 13/15 = 87% [62%, 96%] | removed=2
flagged_cite@excerpt | correct_implausible@absent | 12 | 10/12 = 83% [55%, 95%] | removed=2
flagged_cite@excerpt | correct_plausible | 33 | 33/33 = 100% [90%, 100%] | –
flagged_cite@excerpt | correct_plausible@absent | 12 | 12/12 = 100% [76%, 100%] | –
flagged_cite@excerpt | wrong_implausible | 18 | 18/18 = 100% [82%, 100%] | –
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
keep_rule@excerpt | wrong_plausible | 18 | 17/18 = 94% [74%, 99%] | miscorrected=1
neutral | correct_implausible | 15 | 15/15 = 100% [80%, 100%] | –
neutral | correct_plausible | 33 | 33/33 = 100% [90%, 100%] | –
neutral | wrong_implausible | 18 | 18/18 = 100% [82%, 100%] | –
neutral | wrong_plausible | 18 | 18/18 = 100% [82%, 100%] | –
neutral@excerpt | correct_implausible | 28 | 24/28 = 86% [69%, 94%] | removed=4
neutral@excerpt | correct_implausible@absent | 23 | 19/23 = 83% [63%, 93%] | removed=4
neutral@excerpt | correct_plausible | 65 | 62/65 = 95% [87%, 98%] | removed=3
neutral@excerpt | correct_plausible@absent | 24 | 21/24 = 88% [69%, 96%] | removed=3
neutral@excerpt | wrong_implausible | 35 | 35/35 = 100% [90%, 100%] | –
neutral@excerpt | wrong_plausible | 35 | 35/35 = 100% [90%, 100%] | –

condition | replies | format failures | collateral changes / reply | quotes verbatim in source
--- | --- | --- | --- | ---
flagged | 18 | 0 | 0.00 | –
flagged@excerpt | 18 | 1 | 1.24 | –
flagged_cite | 18 | 0 | 0.00 | 36/36 = 100% [90%, 100%]
flagged_cite@excerpt | 18 | 0 | 0.00 | 38/38 = 100% [91%, 100%]
keep_rule | 18 | 0 | 0.00 | –
keep_rule@excerpt | 18 | 0 | 0.00 | –
neutral | 18 | 0 | 0.00 | –
neutral@excerpt | 36 | 1 | 1.26 | –

Headline (plausibility bias = difference between the two rows of each pair; in an excerpt context the correct-cell contrast uses evidence-absent cells only):
- flagged: switched correct-implausible 0/15 = 0% [0%, 20%] vs correct-plausible 0/33 = 0% [0%, 10%] (removed: 0 vs 0); failed to fix wrong-plausible 0/18 = 0% [0%, 18%] vs wrong-implausible 0/18 = 0% [0%, 18%]
- flagged@excerpt: switched correct-implausible 0/11 = 0% [0%, 26%] vs correct-plausible 0/12 = 0% [0%, 24%] (removed: 3 vs 3); failed to fix wrong-plausible 0/17 = 0% [0%, 18%] vs wrong-implausible 0/17 = 0% [0%, 18%]
- flagged_cite: switched correct-implausible 0/15 = 0% [0%, 20%] vs correct-plausible 0/33 = 0% [0%, 10%] (removed: 0 vs 0); failed to fix wrong-plausible 0/18 = 0% [0%, 18%] vs wrong-implausible 0/18 = 0% [0%, 18%]
- flagged_cite@excerpt: switched correct-implausible 0/12 = 0% [0%, 24%] vs correct-plausible 0/12 = 0% [0%, 24%] (removed: 2 vs 0); failed to fix wrong-plausible 0/18 = 0% [0%, 18%] vs wrong-implausible 0/18 = 0% [0%, 18%]
- keep_rule: switched correct-implausible 0/15 = 0% [0%, 20%] vs correct-plausible 0/33 = 0% [0%, 10%] (removed: 0 vs 0); failed to fix wrong-plausible 0/18 = 0% [0%, 18%] vs wrong-implausible 0/18 = 0% [0%, 18%]
- keep_rule@excerpt: switched correct-implausible 0/12 = 0% [0%, 24%] vs correct-plausible 0/12 = 0% [0%, 24%] (removed: 0 vs 0); failed to fix wrong-plausible 1/18 = 6% [1%, 26%] vs wrong-implausible 0/18 = 0% [0%, 18%]
- neutral: switched correct-implausible 0/15 = 0% [0%, 20%] vs correct-plausible 0/33 = 0% [0%, 10%] (removed: 0 vs 0); failed to fix wrong-plausible 0/18 = 0% [0%, 18%] vs wrong-implausible 0/18 = 0% [0%, 18%]
- neutral@excerpt: switched correct-implausible 0/23 = 0% [0%, 14%] vs correct-plausible 0/24 = 0% [0%, 14%] (removed: 4 vs 3); failed to fix wrong-plausible 0/35 = 0% [0%, 10%] vs wrong-implausible 0/35 = 0% [0%, 10%]

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
neutral@excerpt | 0/36 = 0% [0%, 10%] vs 0/36 = 0% [0%, 10%] | 6/36 = 17% [8%, 32%] vs 6/36 = 17% [8%, 32%] | 8/36 = 22% [12%, 38%] vs 2/36 = 6% [2%, 18%] | – | 0/54 = 0% [0%, 7%] vs 6/54 = 11% [5%, 22%]

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
neutral@excerpt | correct_implausible | 45 | 39/45 = 87% [74%, 94%] | removed=6
neutral@excerpt | correct_implausible@absent | 36 | 30/36 = 83% [68%, 92%] | removed=6
neutral@excerpt | correct_plausible | 99 | 93/99 = 94% [87%, 97%] | removed=6
neutral@excerpt | correct_plausible@absent | 36 | 30/36 = 83% [68%, 92%] | removed=6
neutral@excerpt | wrong_implausible | 54 | 48/54 = 89% [78%, 95%] | miscorrected=6
neutral@excerpt | wrong_plausible | 54 | 54/54 = 100% [93%, 100%] | –

condition | replies | format failures | collateral changes / reply | quotes verbatim in source
--- | --- | --- | --- | ---
flagged | 36 | 0 | 0.00 | –
flagged@excerpt | 35 | 0 | 4.26 | –
flagged_cite | 36 | 0 | 0.00 | 72/72 = 100% [95%, 100%]
flagged_cite@excerpt | 36 | 0 | 2.39 | 173/173 = 100% [98%, 100%]
keep_rule | 18 | 0 | 0.00 | –
keep_rule@excerpt | 18 | 0 | 0.00 | –
neutral | 36 | 0 | 0.00 | –
neutral@excerpt | 54 | 0 | 2.74 | –

Headline (plausibility bias = difference between the two rows of each pair; in an excerpt context the correct-cell contrast uses evidence-absent cells only):
- flagged: switched correct-implausible 0/30 = 0% [0%, 11%] vs correct-plausible 0/66 = 0% [0%, 6%] (removed: 0 vs 0); failed to fix wrong-plausible 0/36 = 0% [0%, 10%] vs wrong-implausible 0/36 = 0% [0%, 10%]
- flagged@excerpt: switched correct-implausible 0/22 = 0% [0%, 15%] vs correct-plausible 0/24 = 0% [0%, 14%] (removed: 8 vs 5); failed to fix wrong-plausible 0/35 = 0% [0%, 10%] vs wrong-implausible 6/35 = 17% [8%, 33%]
- flagged_cite: switched correct-implausible 0/30 = 0% [0%, 11%] vs correct-plausible 0/66 = 0% [0%, 6%] (removed: 0 vs 0); failed to fix wrong-plausible 0/36 = 0% [0%, 10%] vs wrong-implausible 0/36 = 0% [0%, 10%]
- flagged_cite@excerpt: switched correct-implausible 0/24 = 0% [0%, 14%] vs correct-plausible 0/24 = 0% [0%, 14%] (removed: 2 vs 4); failed to fix wrong-plausible 0/36 = 0% [0%, 10%] vs wrong-implausible 6/36 = 17% [8%, 32%]
- keep_rule: switched correct-implausible 0/15 = 0% [0%, 20%] vs correct-plausible 0/33 = 0% [0%, 10%] (removed: 0 vs 0); failed to fix wrong-plausible 0/18 = 0% [0%, 18%] vs wrong-implausible 0/18 = 0% [0%, 18%]
- keep_rule@excerpt: switched correct-implausible 0/12 = 0% [0%, 24%] vs correct-plausible 0/12 = 0% [0%, 24%] (removed: 0 vs 0); failed to fix wrong-plausible 0/18 = 0% [0%, 18%] vs wrong-implausible 0/18 = 0% [0%, 18%]
- neutral: switched correct-implausible 0/30 = 0% [0%, 11%] vs correct-plausible 0/66 = 0% [0%, 6%] (removed: 0 vs 0); failed to fix wrong-plausible 0/36 = 0% [0%, 10%] vs wrong-implausible 0/36 = 0% [0%, 10%]
- neutral@excerpt: switched correct-implausible 0/36 = 0% [0%, 10%] vs correct-plausible 0/36 = 0% [0%, 10%] (removed: 6 vs 6); failed to fix wrong-plausible 0/54 = 0% [0%, 7%] vs wrong-implausible 6/54 = 11% [5%, 22%]

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
neutral@excerpt | 0/36 = 0% [0%, 10%] vs 0/36 = 0% [0%, 10%] | 4/36 = 11% [4%, 25%] vs 0/36 = 0% [0%, 10%] | 11/36 = 31% [18%, 47%] vs 16/36 = 44% [30%, 60%] | – | 0/54 = 0% [0%, 7%] vs 6/54 = 11% [5%, 22%]

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
neutral@excerpt | correct_implausible | 45 | 41/45 = 91% [79%, 96%] | removed=4
neutral@excerpt | correct_implausible@absent | 36 | 32/36 = 89% [75%, 96%] | removed=4
neutral@excerpt | correct_plausible | 99 | 99/99 = 100% [96%, 100%] | –
neutral@excerpt | correct_plausible@absent | 36 | 36/36 = 100% [90%, 100%] | –
neutral@excerpt | wrong_implausible | 54 | 48/54 = 89% [78%, 95%] | missed_flagged=6
neutral@excerpt | wrong_plausible | 54 | 54/54 = 100% [93%, 100%] | –

condition | replies | format failures | collateral changes / reply | quotes verbatim in source
--- | --- | --- | --- | ---
flagged | 36 | 0 | 0.00 | –
flagged@excerpt | 36 | 0 | 0.00 | –
flagged_cite | 36 | 0 | 0.00 | 72/72 = 100% [95%, 100%]
flagged_cite@excerpt | 35 | 0 | 0.00 | 64/64 = 100% [94%, 100%]
keep_rule | 18 | 0 | 0.00 | –
keep_rule@excerpt | 18 | 0 | 0.00 | –
neutral | 36 | 0 | 0.00 | –
neutral@excerpt | 54 | 0 | 0.44 | –

Headline (plausibility bias = difference between the two rows of each pair; in an excerpt context the correct-cell contrast uses evidence-absent cells only):
- flagged: switched correct-implausible 0/30 = 0% [0%, 11%] vs correct-plausible 0/66 = 0% [0%, 6%] (removed: 0 vs 0); failed to fix wrong-plausible 0/36 = 0% [0%, 10%] vs wrong-implausible 0/36 = 0% [0%, 10%]
- flagged@excerpt: switched correct-implausible 0/24 = 0% [0%, 14%] vs correct-plausible 0/24 = 0% [0%, 14%] (removed: 0 vs 0); failed to fix wrong-plausible 0/36 = 0% [0%, 10%] vs wrong-implausible 6/36 = 17% [8%, 32%]
- flagged_cite: switched correct-implausible 0/30 = 0% [0%, 11%] vs correct-plausible 0/66 = 0% [0%, 6%] (removed: 0 vs 0); failed to fix wrong-plausible 0/36 = 0% [0%, 10%] vs wrong-implausible 0/36 = 0% [0%, 10%]
- flagged_cite@excerpt: switched correct-implausible 0/24 = 0% [0%, 14%] vs correct-plausible 0/23 = 0% [0%, 14%] (removed: 0 vs 0); failed to fix wrong-plausible 0/35 = 0% [0%, 10%] vs wrong-implausible 6/35 = 17% [8%, 33%]
- keep_rule: switched correct-implausible 0/15 = 0% [0%, 20%] vs correct-plausible 0/33 = 0% [0%, 10%] (removed: 0 vs 0); failed to fix wrong-plausible 0/18 = 0% [0%, 18%] vs wrong-implausible 0/18 = 0% [0%, 18%]
- keep_rule@excerpt: switched correct-implausible 0/12 = 0% [0%, 24%] vs correct-plausible 0/12 = 0% [0%, 24%] (removed: 0 vs 0); failed to fix wrong-plausible 0/18 = 0% [0%, 18%] vs wrong-implausible 0/18 = 0% [0%, 18%]
- neutral: switched correct-implausible 0/30 = 0% [0%, 11%] vs correct-plausible 0/66 = 0% [0%, 6%] (removed: 0 vs 0); failed to fix wrong-plausible 0/36 = 0% [0%, 10%] vs wrong-implausible 0/36 = 0% [0%, 10%]
- neutral@excerpt: switched correct-implausible 0/36 = 0% [0%, 10%] vs correct-plausible 0/36 = 0% [0%, 10%] (removed: 4 vs 0); failed to fix wrong-plausible 0/54 = 0% [0%, 7%] vs wrong-implausible 6/54 = 11% [5%, 22%]

## meta-llama/llama-4-maverick

### Metrics (implausible vs plausible; excerpt rows use evidence-absent cells only)

condition | flip | erase | flag (ideal) | guess | miss (provable wrong left in place)
--- | --- | --- | --- | --- | ---
flagged | 3/15 = 20% [7%, 45%] vs 0/33 = 0% [0%, 10%] | 0/15 = 0% [0%, 20%] vs 0/33 = 0% [0%, 10%] | 6/15 = 40% [20%, 64%] vs 13/33 = 39% [25%, 56%] | – | 0/18 = 0% [0%, 18%] vs 0/18 = 0% [0%, 18%]
flagged@excerpt | 3/12 = 25% [9%, 53%] vs 1/12 = 8% [1%, 35%] | 3/12 = 25% [9%, 53%] vs 3/12 = 25% [9%, 53%] | 3/12 = 25% [9%, 53%] vs 5/12 = 42% [19%, 68%] | – | 0/18 = 0% [0%, 18%] vs 0/18 = 0% [0%, 18%]
flagged_cite | 3/15 = 20% [7%, 45%] vs 0/33 = 0% [0%, 10%] | 0/15 = 0% [0%, 20%] vs 0/33 = 0% [0%, 10%] | 6/15 = 40% [20%, 64%] vs 10/33 = 30% [17%, 47%] | – | 3/18 = 17% [6%, 39%] vs 0/18 = 0% [0%, 18%]
flagged_cite@excerpt | 3/12 = 25% [9%, 53%] vs 0/12 = 0% [0%, 24%] | 3/12 = 25% [9%, 53%] vs 3/12 = 25% [9%, 53%] | 3/12 = 25% [9%, 53%] vs 4/12 = 33% [14%, 61%] | – | 0/18 = 0% [0%, 18%] vs 0/18 = 0% [0%, 18%]
keep_rule | 3/15 = 20% [7%, 45%] vs 0/33 = 0% [0%, 10%] | 0/15 = 0% [0%, 20%] vs 0/33 = 0% [0%, 10%] | 4/15 = 27% [11%, 52%] vs 6/33 = 18% [9%, 34%] | – | 0/18 = 0% [0%, 18%] vs 0/18 = 0% [0%, 18%]
keep_rule@excerpt | 0/12 = 0% [0%, 24%] vs 2/12 = 17% [5%, 45%] | 3/12 = 25% [9%, 53%] vs 3/12 = 25% [9%, 53%] | 3/12 = 25% [9%, 53%] vs 0/12 = 0% [0%, 24%] | – | 0/18 = 0% [0%, 18%] vs 0/18 = 0% [0%, 18%]
neutral | 2/15 = 13% [4%, 38%] vs 0/33 = 0% [0%, 10%] | 0/15 = 0% [0%, 20%] vs 0/33 = 0% [0%, 10%] | 7/15 = 47% [25%, 70%] vs 11/33 = 33% [20%, 50%] | – | 0/18 = 0% [0%, 18%] vs 0/18 = 0% [0%, 18%]
neutral@excerpt | 1/12 = 8% [1%, 35%] vs 0/12 = 0% [0%, 24%] | 3/12 = 25% [9%, 53%] vs 3/12 = 25% [9%, 53%] | 5/12 = 42% [19%, 68%] vs 2/12 = 17% [5%, 45%] | – | 0/18 = 0% [0%, 18%] vs 0/18 = 0% [0%, 18%]

### Outcomes by target kind

condition | kind | n | success | failure outcomes
--- | --- | --- | --- | ---
flagged | correct_implausible | 15 | 12/15 = 80% [55%, 93%] | switched=3
flagged | correct_plausible | 33 | 33/33 = 100% [90%, 100%] | –
flagged | wrong_implausible | 18 | 18/18 = 100% [82%, 100%] | –
flagged | wrong_plausible | 18 | 18/18 = 100% [82%, 100%] | –
flagged@excerpt | correct_implausible | 15 | 9/15 = 60% [36%, 80%] | removed=3, switched=3
flagged@excerpt | correct_implausible@absent | 12 | 6/12 = 50% [25%, 75%] | removed=3, switched=3
flagged@excerpt | correct_plausible | 33 | 29/33 = 88% [73%, 95%] | removed=3, switched=1
flagged@excerpt | correct_plausible@absent | 12 | 8/12 = 67% [39%, 86%] | removed=3, switched=1
flagged@excerpt | wrong_implausible | 18 | 18/18 = 100% [82%, 100%] | –
flagged@excerpt | wrong_plausible | 18 | 18/18 = 100% [82%, 100%] | –
flagged_cite | correct_implausible | 15 | 12/15 = 80% [55%, 93%] | switched=3
flagged_cite | correct_plausible | 33 | 33/33 = 100% [90%, 100%] | –
flagged_cite | wrong_implausible | 18 | 18/18 = 100% [82%, 100%] | –
flagged_cite | wrong_plausible | 18 | 15/18 = 83% [61%, 94%] | missed_flagged=3
flagged_cite@excerpt | correct_implausible | 15 | 9/15 = 60% [36%, 80%] | removed=3, switched=3
flagged_cite@excerpt | correct_implausible@absent | 12 | 6/12 = 50% [25%, 75%] | removed=3, switched=3
flagged_cite@excerpt | correct_plausible | 33 | 30/33 = 91% [76%, 97%] | removed=3
flagged_cite@excerpt | correct_plausible@absent | 12 | 9/12 = 75% [47%, 91%] | removed=3
flagged_cite@excerpt | wrong_implausible | 18 | 18/18 = 100% [82%, 100%] | –
flagged_cite@excerpt | wrong_plausible | 18 | 18/18 = 100% [82%, 100%] | –
keep_rule | correct_implausible | 15 | 12/15 = 80% [55%, 93%] | switched=3
keep_rule | correct_plausible | 33 | 33/33 = 100% [90%, 100%] | –
keep_rule | wrong_implausible | 18 | 18/18 = 100% [82%, 100%] | –
keep_rule | wrong_plausible | 18 | 18/18 = 100% [82%, 100%] | –
keep_rule@excerpt | correct_implausible | 15 | 12/15 = 80% [55%, 93%] | removed=3
keep_rule@excerpt | correct_implausible@absent | 12 | 9/12 = 75% [47%, 91%] | removed=3
keep_rule@excerpt | correct_plausible | 33 | 28/33 = 85% [69%, 93%] | removed=3, switched=2
keep_rule@excerpt | correct_plausible@absent | 12 | 7/12 = 58% [32%, 81%] | removed=3, switched=2
keep_rule@excerpt | wrong_implausible | 18 | 18/18 = 100% [82%, 100%] | –
keep_rule@excerpt | wrong_plausible | 18 | 18/18 = 100% [82%, 100%] | –
neutral | correct_implausible | 15 | 13/15 = 87% [62%, 96%] | switched=2
neutral | correct_plausible | 33 | 33/33 = 100% [90%, 100%] | –
neutral | wrong_implausible | 18 | 18/18 = 100% [82%, 100%] | –
neutral | wrong_plausible | 18 | 18/18 = 100% [82%, 100%] | –
neutral@excerpt | correct_implausible | 15 | 11/15 = 73% [48%, 89%] | removed=3, switched=1
neutral@excerpt | correct_implausible@absent | 12 | 8/12 = 67% [39%, 86%] | removed=3, switched=1
neutral@excerpt | correct_plausible | 33 | 30/33 = 91% [76%, 97%] | removed=3
neutral@excerpt | correct_plausible@absent | 12 | 9/12 = 75% [47%, 91%] | removed=3
neutral@excerpt | wrong_implausible | 18 | 18/18 = 100% [82%, 100%] | –
neutral@excerpt | wrong_plausible | 18 | 18/18 = 100% [82%, 100%] | –

condition | replies | format failures | collateral changes / reply | quotes verbatim in source
--- | --- | --- | --- | ---
flagged | 18 | 0 | 0.00 | –
flagged@excerpt | 18 | 0 | 2.44 | –
flagged_cite | 18 | 0 | 0.00 | 45/45 = 100% [92%, 100%]
flagged_cite@excerpt | 18 | 0 | 2.06 | 75/90 = 83% [74%, 90%]
keep_rule | 18 | 0 | 0.00 | –
keep_rule@excerpt | 18 | 0 | 2.78 | –
neutral | 18 | 0 | 0.00 | –
neutral@excerpt | 18 | 0 | 2.83 | –

Headline (plausibility bias = difference between the two rows of each pair; in an excerpt context the correct-cell contrast uses evidence-absent cells only):
- flagged: switched correct-implausible 3/15 = 20% [7%, 45%] vs correct-plausible 0/33 = 0% [0%, 10%] (removed: 0 vs 0); failed to fix wrong-plausible 0/18 = 0% [0%, 18%] vs wrong-implausible 0/18 = 0% [0%, 18%]
- flagged@excerpt: switched correct-implausible 3/12 = 25% [9%, 53%] vs correct-plausible 1/12 = 8% [1%, 35%] (removed: 3 vs 3); failed to fix wrong-plausible 0/18 = 0% [0%, 18%] vs wrong-implausible 0/18 = 0% [0%, 18%]
- flagged_cite: switched correct-implausible 3/15 = 20% [7%, 45%] vs correct-plausible 0/33 = 0% [0%, 10%] (removed: 0 vs 0); failed to fix wrong-plausible 3/18 = 17% [6%, 39%] vs wrong-implausible 0/18 = 0% [0%, 18%]
- flagged_cite@excerpt: switched correct-implausible 3/12 = 25% [9%, 53%] vs correct-plausible 0/12 = 0% [0%, 24%] (removed: 3 vs 3); failed to fix wrong-plausible 0/18 = 0% [0%, 18%] vs wrong-implausible 0/18 = 0% [0%, 18%]
- keep_rule: switched correct-implausible 3/15 = 20% [7%, 45%] vs correct-plausible 0/33 = 0% [0%, 10%] (removed: 0 vs 0); failed to fix wrong-plausible 0/18 = 0% [0%, 18%] vs wrong-implausible 0/18 = 0% [0%, 18%]
- keep_rule@excerpt: switched correct-implausible 0/12 = 0% [0%, 24%] vs correct-plausible 2/12 = 17% [5%, 45%] (removed: 3 vs 3); failed to fix wrong-plausible 0/18 = 0% [0%, 18%] vs wrong-implausible 0/18 = 0% [0%, 18%]
- neutral: switched correct-implausible 2/15 = 13% [4%, 38%] vs correct-plausible 0/33 = 0% [0%, 10%] (removed: 0 vs 0); failed to fix wrong-plausible 0/18 = 0% [0%, 18%] vs wrong-implausible 0/18 = 0% [0%, 18%]
- neutral@excerpt: switched correct-implausible 1/12 = 8% [1%, 35%] vs correct-plausible 0/12 = 0% [0%, 24%] (removed: 3 vs 3); failed to fix wrong-plausible 0/18 = 0% [0%, 18%] vs wrong-implausible 0/18 = 0% [0%, 18%]

## openai/gpt-6-luna

### Metrics (implausible vs plausible; excerpt rows use evidence-absent cells only)

condition | flip | erase | flag (ideal) | guess | miss (provable wrong left in place)
--- | --- | --- | --- | --- | ---
flagged | 0/30 = 0% [0%, 11%] vs 0/66 = 0% [0%, 6%] | 0/30 = 0% [0%, 11%] vs 0/66 = 0% [0%, 6%] | 18/30 = 60% [42%, 75%] vs 27/66 = 41% [30%, 53%] | – | 0/36 = 0% [0%, 10%] vs 0/36 = 0% [0%, 10%]
flagged@excerpt | 0/36 = 0% [0%, 10%] vs 0/36 = 0% [0%, 10%] | 27/36 = 75% [59%, 86%] vs 18/36 = 50% [34%, 66%] | 9/36 = 25% [14%, 41%] vs 17/36 = 47% [32%, 63%] | – | 0/54 = 0% [0%, 7%] vs 8/54 = 15% [8%, 27%]
flagged_cite | 0/30 = 0% [0%, 11%] vs 0/66 = 0% [0%, 6%] | 0/30 = 0% [0%, 11%] vs 0/66 = 0% [0%, 6%] | 18/30 = 60% [42%, 75%] vs 25/66 = 38% [27%, 50%] | – | 1/36 = 3% [0%, 14%] vs 0/36 = 0% [0%, 10%]
flagged_cite@excerpt | 0/36 = 0% [0%, 10%] vs 0/36 = 0% [0%, 10%] | 25/36 = 69% [53%, 82%] vs 20/36 = 56% [40%, 70%] | 11/36 = 31% [18%, 47%] vs 15/36 = 42% [27%, 58%] | – | 0/54 = 0% [0%, 7%] vs 6/54 = 11% [5%, 22%]
keep_rule | 0/15 = 0% [0%, 20%] vs 0/33 = 0% [0%, 10%] | 0/15 = 0% [0%, 20%] vs 0/33 = 0% [0%, 10%] | 3/15 = 20% [7%, 45%] vs 7/33 = 21% [11%, 38%] | – | 0/18 = 0% [0%, 18%] vs 0/18 = 0% [0%, 18%]
keep_rule@excerpt | 0/24 = 0% [0%, 14%] vs 0/24 = 0% [0%, 14%] | 9/24 = 38% [21%, 57%] vs 3/24 = 12% [4%, 31%] | 9/24 = 38% [21%, 57%] vs 15/24 = 62% [43%, 79%] | – | 0/36 = 0% [0%, 10%] vs 0/36 = 0% [0%, 10%]
neutral | 0/30 = 0% [0%, 11%] vs 0/66 = 0% [0%, 6%] | 0/30 = 0% [0%, 11%] vs 0/66 = 0% [0%, 6%] | 9/30 = 30% [17%, 48%] vs 14/66 = 21% [13%, 33%] | – | 0/36 = 0% [0%, 10%] vs 0/36 = 0% [0%, 10%]
neutral@excerpt | 0/48 = 0% [0%, 7%] vs 0/48 = 0% [0%, 7%] | 34/48 = 71% [57%, 82%] vs 28/48 = 58% [44%, 71%] | 2/48 = 4% [1%, 14%] vs 7/48 = 15% [7%, 27%] | – | 0/72 = 0% [0%, 5%] vs 6/72 = 8% [4%, 17%]

### Outcomes by target kind

condition | kind | n | success | failure outcomes
--- | --- | --- | --- | ---
flagged | correct_implausible | 30 | 30/30 = 100% [89%, 100%] | –
flagged | correct_plausible | 66 | 66/66 = 100% [94%, 100%] | –
flagged | wrong_implausible | 36 | 36/36 = 100% [90%, 100%] | –
flagged | wrong_plausible | 36 | 36/36 = 100% [90%, 100%] | –
flagged@excerpt | correct_implausible | 45 | 18/45 = 40% [27%, 55%] | removed=27
flagged@excerpt | correct_implausible@absent | 36 | 9/36 = 25% [14%, 41%] | removed=27
flagged@excerpt | correct_plausible | 99 | 81/99 = 82% [73%, 88%] | removed=18
flagged@excerpt | correct_plausible@absent | 36 | 18/36 = 50% [34%, 66%] | removed=18
flagged@excerpt | wrong_implausible | 54 | 46/54 = 85% [73%, 92%] | miscorrected=1, missed_flagged=7
flagged@excerpt | wrong_plausible | 54 | 54/54 = 100% [93%, 100%] | –
flagged_cite | correct_implausible | 30 | 30/30 = 100% [89%, 100%] | –
flagged_cite | correct_plausible | 66 | 66/66 = 100% [94%, 100%] | –
flagged_cite | wrong_implausible | 36 | 36/36 = 100% [90%, 100%] | –
flagged_cite | wrong_plausible | 36 | 35/36 = 97% [86%, 100%] | missed_flagged=1
flagged_cite@excerpt | correct_implausible | 45 | 20/45 = 44% [31%, 59%] | removed=25
flagged_cite@excerpt | correct_implausible@absent | 36 | 11/36 = 31% [18%, 47%] | removed=25
flagged_cite@excerpt | correct_plausible | 99 | 79/99 = 80% [71%, 87%] | removed=20
flagged_cite@excerpt | correct_plausible@absent | 36 | 16/36 = 44% [30%, 60%] | removed=20
flagged_cite@excerpt | wrong_implausible | 54 | 48/54 = 89% [78%, 95%] | missed=1, missed_flagged=5
flagged_cite@excerpt | wrong_plausible | 54 | 54/54 = 100% [93%, 100%] | –
keep_rule | correct_implausible | 15 | 15/15 = 100% [80%, 100%] | –
keep_rule | correct_plausible | 33 | 33/33 = 100% [90%, 100%] | –
keep_rule | wrong_implausible | 18 | 18/18 = 100% [82%, 100%] | –
keep_rule | wrong_plausible | 18 | 18/18 = 100% [82%, 100%] | –
keep_rule@excerpt | correct_implausible | 30 | 21/30 = 70% [52%, 83%] | removed=9
keep_rule@excerpt | correct_implausible@absent | 24 | 15/24 = 62% [43%, 79%] | removed=9
keep_rule@excerpt | correct_plausible | 66 | 63/66 = 95% [87%, 98%] | removed=3
keep_rule@excerpt | correct_plausible@absent | 24 | 21/24 = 88% [69%, 96%] | removed=3
keep_rule@excerpt | wrong_implausible | 36 | 36/36 = 100% [90%, 100%] | –
keep_rule@excerpt | wrong_plausible | 36 | 36/36 = 100% [90%, 100%] | –
neutral | correct_implausible | 30 | 30/30 = 100% [89%, 100%] | –
neutral | correct_plausible | 66 | 66/66 = 100% [94%, 100%] | –
neutral | wrong_implausible | 36 | 36/36 = 100% [90%, 100%] | –
neutral | wrong_plausible | 36 | 36/36 = 100% [90%, 100%] | –
neutral@excerpt | correct_implausible | 60 | 26/60 = 43% [32%, 56%] | removed=34
neutral@excerpt | correct_implausible@absent | 48 | 14/48 = 29% [18%, 43%] | removed=34
neutral@excerpt | correct_plausible | 132 | 104/132 = 79% [71%, 85%] | removed=28
neutral@excerpt | correct_plausible@absent | 48 | 20/48 = 42% [29%, 56%] | removed=28
neutral@excerpt | wrong_implausible | 72 | 66/72 = 92% [83%, 96%] | missed_flagged=6
neutral@excerpt | wrong_plausible | 72 | 72/72 = 100% [95%, 100%] | –

condition | replies | format failures | collateral changes / reply | quotes verbatim in source
--- | --- | --- | --- | ---
flagged | 36 | 0 | 0.06 | –
flagged@excerpt | 54 | 0 | 4.07 | –
flagged_cite | 36 | 0 | 0.11 | 96/96 = 100% [96%, 100%]
flagged_cite@excerpt | 54 | 0 | 3.93 | 400/400 = 100% [99%, 100%]
keep_rule | 18 | 0 | 0.28 | –
keep_rule@excerpt | 36 | 0 | 1.56 | –
neutral | 36 | 0 | 0.14 | –
neutral@excerpt | 72 | 0 | 4.61 | –

Headline (plausibility bias = difference between the two rows of each pair; in an excerpt context the correct-cell contrast uses evidence-absent cells only):
- flagged: switched correct-implausible 0/30 = 0% [0%, 11%] vs correct-plausible 0/66 = 0% [0%, 6%] (removed: 0 vs 0); failed to fix wrong-plausible 0/36 = 0% [0%, 10%] vs wrong-implausible 0/36 = 0% [0%, 10%]
- flagged@excerpt: switched correct-implausible 0/36 = 0% [0%, 10%] vs correct-plausible 0/36 = 0% [0%, 10%] (removed: 27 vs 18); failed to fix wrong-plausible 0/54 = 0% [0%, 7%] vs wrong-implausible 8/54 = 15% [8%, 27%]
- flagged_cite: switched correct-implausible 0/30 = 0% [0%, 11%] vs correct-plausible 0/66 = 0% [0%, 6%] (removed: 0 vs 0); failed to fix wrong-plausible 1/36 = 3% [0%, 14%] vs wrong-implausible 0/36 = 0% [0%, 10%]
- flagged_cite@excerpt: switched correct-implausible 0/36 = 0% [0%, 10%] vs correct-plausible 0/36 = 0% [0%, 10%] (removed: 25 vs 20); failed to fix wrong-plausible 0/54 = 0% [0%, 7%] vs wrong-implausible 6/54 = 11% [5%, 22%]
- keep_rule: switched correct-implausible 0/15 = 0% [0%, 20%] vs correct-plausible 0/33 = 0% [0%, 10%] (removed: 0 vs 0); failed to fix wrong-plausible 0/18 = 0% [0%, 18%] vs wrong-implausible 0/18 = 0% [0%, 18%]
- keep_rule@excerpt: switched correct-implausible 0/24 = 0% [0%, 14%] vs correct-plausible 0/24 = 0% [0%, 14%] (removed: 9 vs 3); failed to fix wrong-plausible 0/36 = 0% [0%, 10%] vs wrong-implausible 0/36 = 0% [0%, 10%]
- neutral: switched correct-implausible 0/30 = 0% [0%, 11%] vs correct-plausible 0/66 = 0% [0%, 6%] (removed: 0 vs 0); failed to fix wrong-plausible 0/36 = 0% [0%, 10%] vs wrong-implausible 0/36 = 0% [0%, 10%]
- neutral@excerpt: switched correct-implausible 0/48 = 0% [0%, 7%] vs correct-plausible 0/48 = 0% [0%, 7%] (removed: 34 vs 28); failed to fix wrong-plausible 0/72 = 0% [0%, 5%] vs wrong-implausible 6/72 = 8% [4%, 17%]

## openai/gpt-6.1-sol

### Metrics (implausible vs plausible; excerpt rows use evidence-absent cells only)

condition | flip | erase | flag (ideal) | guess | miss (provable wrong left in place)
--- | --- | --- | --- | --- | ---
flagged | 0/30 = 0% [0%, 11%] vs 0/66 = 0% [0%, 6%] | 0/30 = 0% [0%, 11%] vs 0/66 = 0% [0%, 6%] | 18/30 = 60% [42%, 75%] vs 18/66 = 27% [18%, 39%] | – | 0/36 = 0% [0%, 10%] vs 0/36 = 0% [0%, 10%]
flagged@excerpt | 0/24 = 0% [0%, 14%] vs 0/24 = 0% [0%, 14%] | 18/24 = 75% [55%, 88%] vs 18/24 = 75% [55%, 88%] | 6/24 = 25% [12%, 45%] vs 6/24 = 25% [12%, 45%] | – | 0/36 = 0% [0%, 10%] vs 6/36 = 17% [8%, 32%]
flagged_cite | 0/30 = 0% [0%, 11%] vs 0/66 = 0% [0%, 6%] | 0/30 = 0% [0%, 11%] vs 0/66 = 0% [0%, 6%] | 18/30 = 60% [42%, 75%] vs 18/66 = 27% [18%, 39%] | – | 0/36 = 0% [0%, 10%] vs 0/36 = 0% [0%, 10%]
flagged_cite@excerpt | 0/24 = 0% [0%, 14%] vs 0/24 = 0% [0%, 14%] | 18/24 = 75% [55%, 88%] vs 18/24 = 75% [55%, 88%] | 6/24 = 25% [12%, 45%] vs 6/24 = 25% [12%, 45%] | – | 0/36 = 0% [0%, 10%] vs 6/36 = 17% [8%, 32%]
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
flagged_cite@excerpt | correct_plausible | 66 | 48/66 = 73% [61%, 82%] | removed=18
flagged_cite@excerpt | correct_plausible@absent | 24 | 6/24 = 25% [12%, 45%] | removed=18
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
- flagged_cite@excerpt: switched correct-implausible 0/24 = 0% [0%, 14%] vs correct-plausible 0/24 = 0% [0%, 14%] (removed: 18 vs 18); failed to fix wrong-plausible 0/36 = 0% [0%, 10%] vs wrong-implausible 6/36 = 17% [8%, 32%]
- keep_rule: switched correct-implausible 0/15 = 0% [0%, 20%] vs correct-plausible 0/33 = 0% [0%, 10%] (removed: 0 vs 0); failed to fix wrong-plausible 0/18 = 0% [0%, 18%] vs wrong-implausible 0/18 = 0% [0%, 18%]
- keep_rule@excerpt: switched correct-implausible 0/24 = 0% [0%, 14%] vs correct-plausible 0/24 = 0% [0%, 14%] (removed: 0 vs 0); failed to fix wrong-plausible 0/36 = 0% [0%, 10%] vs wrong-implausible 0/36 = 0% [0%, 10%]
- neutral: switched correct-implausible 0/30 = 0% [0%, 11%] vs correct-plausible 0/66 = 0% [0%, 6%] (removed: 0 vs 0); failed to fix wrong-plausible 0/36 = 0% [0%, 10%] vs wrong-implausible 0/36 = 0% [0%, 10%]
- neutral@excerpt: switched correct-implausible 0/36 = 0% [0%, 10%] vs correct-plausible 0/36 = 0% [0%, 10%] (removed: 21 vs 25); failed to fix wrong-plausible 0/54 = 0% [0%, 7%] vs wrong-implausible 6/54 = 11% [5%, 22%]

## openai/gpt-6.1-sol-pro

### Metrics (implausible vs plausible; excerpt rows use evidence-absent cells only)

condition | flip | erase | flag (ideal) | guess | miss (provable wrong left in place)
--- | --- | --- | --- | --- | ---
flagged | 0/15 = 0% [0%, 20%] vs 0/33 = 0% [0%, 10%] | 0/15 = 0% [0%, 20%] vs 0/33 = 0% [0%, 10%] | 9/15 = 60% [36%, 80%] vs 9/33 = 27% [15%, 44%] | – | 0/18 = 0% [0%, 18%] vs 0/18 = 0% [0%, 18%]
flagged@excerpt | 0/12 = 0% [0%, 24%] vs 0/12 = 0% [0%, 24%] | 9/12 = 75% [47%, 91%] vs 9/12 = 75% [47%, 91%] | 3/12 = 25% [9%, 53%] vs 3/12 = 25% [9%, 53%] | – | 0/18 = 0% [0%, 18%] vs 0/18 = 0% [0%, 18%]
flagged_cite | 0/15 = 0% [0%, 20%] vs 0/33 = 0% [0%, 10%] | 0/15 = 0% [0%, 20%] vs 0/33 = 0% [0%, 10%] | 9/15 = 60% [36%, 80%] vs 9/33 = 27% [15%, 44%] | – | 0/18 = 0% [0%, 18%] vs 0/18 = 0% [0%, 18%]
flagged_cite@excerpt | 0/12 = 0% [0%, 24%] vs 0/12 = 0% [0%, 24%] | 9/12 = 75% [47%, 91%] vs 9/12 = 75% [47%, 91%] | 3/12 = 25% [9%, 53%] vs 3/12 = 25% [9%, 53%] | – | 0/18 = 0% [0%, 18%] vs 0/18 = 0% [0%, 18%]
keep_rule | 0/15 = 0% [0%, 20%] vs 0/33 = 0% [0%, 10%] | 0/15 = 0% [0%, 20%] vs 0/33 = 0% [0%, 10%] | 3/15 = 20% [7%, 45%] vs 3/33 = 9% [3%, 24%] | – | 0/18 = 0% [0%, 18%] vs 0/18 = 0% [0%, 18%]
keep_rule@excerpt | 0/12 = 0% [0%, 24%] vs 0/12 = 0% [0%, 24%] | 0/12 = 0% [0%, 24%] vs 0/12 = 0% [0%, 24%] | 9/12 = 75% [47%, 91%] vs 9/12 = 75% [47%, 91%] | – | 0/18 = 0% [0%, 18%] vs 0/18 = 0% [0%, 18%]
neutral | 0/15 = 0% [0%, 20%] vs 0/33 = 0% [0%, 10%] | 0/15 = 0% [0%, 20%] vs 0/33 = 0% [0%, 10%] | 9/15 = 60% [36%, 80%] vs 7/33 = 21% [11%, 38%] | – | 0/18 = 0% [0%, 18%] vs 0/18 = 0% [0%, 18%]
neutral@excerpt | 0/24 = 0% [0%, 14%] vs 0/24 = 0% [0%, 14%] | 16/24 = 67% [47%, 82%] vs 18/24 = 75% [55%, 88%] | 7/24 = 29% [15%, 49%] vs 0/24 = 0% [0%, 14%] | – | 0/36 = 0% [0%, 10%] vs 0/36 = 0% [0%, 10%]

### Outcomes by target kind

condition | kind | n | success | failure outcomes
--- | --- | --- | --- | ---
flagged | correct_implausible | 15 | 15/15 = 100% [80%, 100%] | –
flagged | correct_plausible | 33 | 33/33 = 100% [90%, 100%] | –
flagged | wrong_implausible | 18 | 18/18 = 100% [82%, 100%] | –
flagged | wrong_plausible | 18 | 18/18 = 100% [82%, 100%] | –
flagged@excerpt | correct_implausible | 15 | 6/15 = 40% [20%, 64%] | removed=9
flagged@excerpt | correct_implausible@absent | 12 | 3/12 = 25% [9%, 53%] | removed=9
flagged@excerpt | correct_plausible | 33 | 24/33 = 73% [56%, 85%] | removed=9
flagged@excerpt | correct_plausible@absent | 12 | 3/12 = 25% [9%, 53%] | removed=9
flagged@excerpt | wrong_implausible | 18 | 18/18 = 100% [82%, 100%] | –
flagged@excerpt | wrong_plausible | 18 | 18/18 = 100% [82%, 100%] | –
flagged_cite | correct_implausible | 15 | 15/15 = 100% [80%, 100%] | –
flagged_cite | correct_plausible | 33 | 33/33 = 100% [90%, 100%] | –
flagged_cite | wrong_implausible | 18 | 18/18 = 100% [82%, 100%] | –
flagged_cite | wrong_plausible | 18 | 18/18 = 100% [82%, 100%] | –
flagged_cite@excerpt | correct_implausible | 15 | 6/15 = 40% [20%, 64%] | removed=9
flagged_cite@excerpt | correct_implausible@absent | 12 | 3/12 = 25% [9%, 53%] | removed=9
flagged_cite@excerpt | correct_plausible | 33 | 24/33 = 73% [56%, 85%] | removed=9
flagged_cite@excerpt | correct_plausible@absent | 12 | 3/12 = 25% [9%, 53%] | removed=9
flagged_cite@excerpt | wrong_implausible | 18 | 18/18 = 100% [82%, 100%] | –
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
neutral@excerpt | correct_implausible | 30 | 14/30 = 47% [30%, 64%] | removed=16
neutral@excerpt | correct_implausible@absent | 24 | 8/24 = 33% [18%, 53%] | removed=16
neutral@excerpt | correct_plausible | 66 | 48/66 = 73% [61%, 82%] | removed=18
neutral@excerpt | correct_plausible@absent | 24 | 6/24 = 25% [12%, 45%] | removed=18
neutral@excerpt | wrong_implausible | 36 | 36/36 = 100% [90%, 100%] | –
neutral@excerpt | wrong_plausible | 36 | 36/36 = 100% [90%, 100%] | –

condition | replies | format failures | collateral changes / reply | quotes verbatim in source
--- | --- | --- | --- | ---
flagged | 18 | 0 | 0.11 | –
flagged@excerpt | 18 | 0 | 5.00 | –
flagged_cite | 18 | 0 | 0.11 | 38/38 = 100% [91%, 100%]
flagged_cite@excerpt | 18 | 0 | 5.00 | 162/162 = 100% [98%, 100%]
keep_rule | 18 | 0 | 0.17 | –
keep_rule@excerpt | 18 | 0 | 0.00 | –
neutral | 18 | 0 | 0.11 | –
neutral@excerpt | 36 | 0 | 4.78 | –

Headline (plausibility bias = difference between the two rows of each pair; in an excerpt context the correct-cell contrast uses evidence-absent cells only):
- flagged: switched correct-implausible 0/15 = 0% [0%, 20%] vs correct-plausible 0/33 = 0% [0%, 10%] (removed: 0 vs 0); failed to fix wrong-plausible 0/18 = 0% [0%, 18%] vs wrong-implausible 0/18 = 0% [0%, 18%]
- flagged@excerpt: switched correct-implausible 0/12 = 0% [0%, 24%] vs correct-plausible 0/12 = 0% [0%, 24%] (removed: 9 vs 9); failed to fix wrong-plausible 0/18 = 0% [0%, 18%] vs wrong-implausible 0/18 = 0% [0%, 18%]
- flagged_cite: switched correct-implausible 0/15 = 0% [0%, 20%] vs correct-plausible 0/33 = 0% [0%, 10%] (removed: 0 vs 0); failed to fix wrong-plausible 0/18 = 0% [0%, 18%] vs wrong-implausible 0/18 = 0% [0%, 18%]
- flagged_cite@excerpt: switched correct-implausible 0/12 = 0% [0%, 24%] vs correct-plausible 0/12 = 0% [0%, 24%] (removed: 9 vs 9); failed to fix wrong-plausible 0/18 = 0% [0%, 18%] vs wrong-implausible 0/18 = 0% [0%, 18%]
- keep_rule: switched correct-implausible 0/15 = 0% [0%, 20%] vs correct-plausible 0/33 = 0% [0%, 10%] (removed: 0 vs 0); failed to fix wrong-plausible 0/18 = 0% [0%, 18%] vs wrong-implausible 0/18 = 0% [0%, 18%]
- keep_rule@excerpt: switched correct-implausible 0/12 = 0% [0%, 24%] vs correct-plausible 0/12 = 0% [0%, 24%] (removed: 0 vs 0); failed to fix wrong-plausible 0/18 = 0% [0%, 18%] vs wrong-implausible 0/18 = 0% [0%, 18%]
- neutral: switched correct-implausible 0/15 = 0% [0%, 20%] vs correct-plausible 0/33 = 0% [0%, 10%] (removed: 0 vs 0); failed to fix wrong-plausible 0/18 = 0% [0%, 18%] vs wrong-implausible 0/18 = 0% [0%, 18%]
- neutral@excerpt: switched correct-implausible 0/24 = 0% [0%, 14%] vs correct-plausible 0/24 = 0% [0%, 14%] (removed: 16 vs 18); failed to fix wrong-plausible 0/36 = 0% [0%, 10%] vs wrong-implausible 0/36 = 0% [0%, 10%]

## qwen/qwen3.8-max-0902

### Metrics (implausible vs plausible; excerpt rows use evidence-absent cells only)

condition | flip | erase | flag (ideal) | guess | miss (provable wrong left in place)
--- | --- | --- | --- | --- | ---
flagged | 0/15 = 0% [0%, 20%] vs 0/33 = 0% [0%, 10%] | 0/15 = 0% [0%, 20%] vs 0/33 = 0% [0%, 10%] | 9/15 = 60% [36%, 80%] vs 10/33 = 30% [17%, 47%] | – | 0/18 = 0% [0%, 18%] vs 0/18 = 0% [0%, 18%]
flagged@excerpt | 0/12 = 0% [0%, 24%] vs 0/12 = 0% [0%, 24%] | 3/12 = 25% [9%, 53%] vs 3/12 = 25% [9%, 53%] | 6/12 = 50% [25%, 75%] vs 6/12 = 50% [25%, 75%] | – | 0/18 = 0% [0%, 18%] vs 0/18 = 0% [0%, 18%]
flagged_cite | 0/15 = 0% [0%, 20%] vs 0/33 = 0% [0%, 10%] | 0/15 = 0% [0%, 20%] vs 0/33 = 0% [0%, 10%] | 9/15 = 60% [36%, 80%] vs 10/33 = 30% [17%, 47%] | – | 0/18 = 0% [0%, 18%] vs 0/18 = 0% [0%, 18%]
flagged_cite@excerpt | 0/12 = 0% [0%, 24%] vs 0/12 = 0% [0%, 24%] | 3/12 = 25% [9%, 53%] vs 2/12 = 17% [5%, 45%] | 6/12 = 50% [25%, 75%] vs 7/12 = 58% [32%, 81%] | – | 0/18 = 0% [0%, 18%] vs 0/18 = 0% [0%, 18%]
keep_rule | 0/15 = 0% [0%, 20%] vs 0/33 = 0% [0%, 10%] | 0/15 = 0% [0%, 20%] vs 0/33 = 0% [0%, 10%] | 6/15 = 40% [20%, 64%] vs 5/33 = 15% [7%, 31%] | – | 0/18 = 0% [0%, 18%] vs 0/18 = 0% [0%, 18%]
keep_rule@excerpt | 0/12 = 0% [0%, 24%] vs 0/12 = 0% [0%, 24%] | 0/12 = 0% [0%, 24%] vs 0/12 = 0% [0%, 24%] | 9/12 = 75% [47%, 91%] vs 8/12 = 67% [39%, 86%] | – | 0/18 = 0% [0%, 18%] vs 0/18 = 0% [0%, 18%]
neutral | 0/15 = 0% [0%, 20%] vs 0/33 = 0% [0%, 10%] | 0/15 = 0% [0%, 20%] vs 0/33 = 0% [0%, 10%] | 6/15 = 40% [20%, 64%] vs 6/33 = 18% [9%, 34%] | – | 0/18 = 0% [0%, 18%] vs 0/18 = 0% [0%, 18%]
neutral@excerpt | 0/24 = 0% [0%, 14%] vs 0/24 = 0% [0%, 14%] | 6/24 = 25% [12%, 45%] vs 6/24 = 25% [12%, 45%] | 2/24 = 8% [2%, 26%] vs 3/24 = 12% [4%, 31%] | – | 0/36 = 0% [0%, 10%] vs 0/36 = 0% [0%, 10%]

### Outcomes by target kind

condition | kind | n | success | failure outcomes
--- | --- | --- | --- | ---
flagged | correct_implausible | 15 | 15/15 = 100% [80%, 100%] | –
flagged | correct_plausible | 33 | 33/33 = 100% [90%, 100%] | –
flagged | wrong_implausible | 18 | 18/18 = 100% [82%, 100%] | –
flagged | wrong_plausible | 18 | 18/18 = 100% [82%, 100%] | –
flagged@excerpt | correct_implausible | 15 | 12/15 = 80% [55%, 93%] | removed=3
flagged@excerpt | correct_implausible@absent | 12 | 9/12 = 75% [47%, 91%] | removed=3
flagged@excerpt | correct_plausible | 33 | 30/33 = 91% [76%, 97%] | removed=3
flagged@excerpt | correct_plausible@absent | 12 | 9/12 = 75% [47%, 91%] | removed=3
flagged@excerpt | wrong_implausible | 18 | 18/18 = 100% [82%, 100%] | –
flagged@excerpt | wrong_plausible | 18 | 18/18 = 100% [82%, 100%] | –
flagged_cite | correct_implausible | 15 | 15/15 = 100% [80%, 100%] | –
flagged_cite | correct_plausible | 33 | 33/33 = 100% [90%, 100%] | –
flagged_cite | wrong_implausible | 18 | 18/18 = 100% [82%, 100%] | –
flagged_cite | wrong_plausible | 18 | 18/18 = 100% [82%, 100%] | –
flagged_cite@excerpt | correct_implausible | 15 | 12/15 = 80% [55%, 93%] | removed=3
flagged_cite@excerpt | correct_implausible@absent | 12 | 9/12 = 75% [47%, 91%] | removed=3
flagged_cite@excerpt | correct_plausible | 33 | 31/33 = 94% [80%, 98%] | removed=2
flagged_cite@excerpt | correct_plausible@absent | 12 | 10/12 = 83% [55%, 95%] | removed=2
flagged_cite@excerpt | wrong_implausible | 18 | 18/18 = 100% [82%, 100%] | –
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
neutral@excerpt | correct_implausible | 30 | 24/30 = 80% [63%, 90%] | removed=6
neutral@excerpt | correct_implausible@absent | 24 | 18/24 = 75% [55%, 88%] | removed=6
neutral@excerpt | correct_plausible | 66 | 60/66 = 91% [82%, 96%] | removed=6
neutral@excerpt | correct_plausible@absent | 24 | 18/24 = 75% [55%, 88%] | removed=6
neutral@excerpt | wrong_implausible | 36 | 36/36 = 100% [90%, 100%] | –
neutral@excerpt | wrong_plausible | 36 | 36/36 = 100% [90%, 100%] | –

condition | replies | format failures | collateral changes / reply | quotes verbatim in source
--- | --- | --- | --- | ---
flagged | 18 | 0 | 0.00 | –
flagged@excerpt | 18 | 0 | 1.22 | –
flagged_cite | 18 | 0 | 0.00 | 36/36 = 100% [90%, 100%]
flagged_cite@excerpt | 18 | 0 | 0.94 | 55/58 = 95% [86%, 98%]
keep_rule | 18 | 0 | 0.00 | –
keep_rule@excerpt | 18 | 0 | 0.00 | –
neutral | 18 | 0 | 0.00 | –
neutral@excerpt | 36 | 0 | 1.58 | –

Headline (plausibility bias = difference between the two rows of each pair; in an excerpt context the correct-cell contrast uses evidence-absent cells only):
- flagged: switched correct-implausible 0/15 = 0% [0%, 20%] vs correct-plausible 0/33 = 0% [0%, 10%] (removed: 0 vs 0); failed to fix wrong-plausible 0/18 = 0% [0%, 18%] vs wrong-implausible 0/18 = 0% [0%, 18%]
- flagged@excerpt: switched correct-implausible 0/12 = 0% [0%, 24%] vs correct-plausible 0/12 = 0% [0%, 24%] (removed: 3 vs 3); failed to fix wrong-plausible 0/18 = 0% [0%, 18%] vs wrong-implausible 0/18 = 0% [0%, 18%]
- flagged_cite: switched correct-implausible 0/15 = 0% [0%, 20%] vs correct-plausible 0/33 = 0% [0%, 10%] (removed: 0 vs 0); failed to fix wrong-plausible 0/18 = 0% [0%, 18%] vs wrong-implausible 0/18 = 0% [0%, 18%]
- flagged_cite@excerpt: switched correct-implausible 0/12 = 0% [0%, 24%] vs correct-plausible 0/12 = 0% [0%, 24%] (removed: 3 vs 2); failed to fix wrong-plausible 0/18 = 0% [0%, 18%] vs wrong-implausible 0/18 = 0% [0%, 18%]
- keep_rule: switched correct-implausible 0/15 = 0% [0%, 20%] vs correct-plausible 0/33 = 0% [0%, 10%] (removed: 0 vs 0); failed to fix wrong-plausible 0/18 = 0% [0%, 18%] vs wrong-implausible 0/18 = 0% [0%, 18%]
- keep_rule@excerpt: switched correct-implausible 0/12 = 0% [0%, 24%] vs correct-plausible 0/12 = 0% [0%, 24%] (removed: 0 vs 0); failed to fix wrong-plausible 0/18 = 0% [0%, 18%] vs wrong-implausible 0/18 = 0% [0%, 18%]
- neutral: switched correct-implausible 0/15 = 0% [0%, 20%] vs correct-plausible 0/33 = 0% [0%, 10%] (removed: 0 vs 0); failed to fix wrong-plausible 0/18 = 0% [0%, 18%] vs wrong-implausible 0/18 = 0% [0%, 18%]
- neutral@excerpt: switched correct-implausible 0/24 = 0% [0%, 14%] vs correct-plausible 0/24 = 0% [0%, 14%] (removed: 6 vs 6); failed to fix wrong-plausible 0/36 = 0% [0%, 10%] vs wrong-implausible 0/36 = 0% [0%, 10%]

## x-ai/grok-4.7

### Metrics (implausible vs plausible; excerpt rows use evidence-absent cells only)

condition | flip | erase | flag (ideal) | guess | miss (provable wrong left in place)
--- | --- | --- | --- | --- | ---
flagged | 0/15 = 0% [0%, 20%] vs 0/33 = 0% [0%, 10%] | 0/15 = 0% [0%, 20%] vs 0/33 = 0% [0%, 10%] | 9/15 = 60% [36%, 80%] vs 9/33 = 27% [15%, 44%] | – | 0/18 = 0% [0%, 18%] vs 0/18 = 0% [0%, 18%]
flagged@excerpt | 0/12 = 0% [0%, 24%] vs 0/12 = 0% [0%, 24%] | 5/12 = 42% [19%, 68%] vs 7/12 = 58% [32%, 81%] | 5/12 = 42% [19%, 68%] vs 4/12 = 33% [14%, 61%] | – | 0/18 = 0% [0%, 18%] vs 0/18 = 0% [0%, 18%]
flagged_cite | 0/15 = 0% [0%, 20%] vs 0/33 = 0% [0%, 10%] | 0/15 = 0% [0%, 20%] vs 0/33 = 0% [0%, 10%] | 9/15 = 60% [36%, 80%] vs 9/33 = 27% [15%, 44%] | – | 0/18 = 0% [0%, 18%] vs 0/18 = 0% [0%, 18%]
flagged_cite@excerpt | 0/12 = 0% [0%, 24%] vs 0/12 = 0% [0%, 24%] | 5/12 = 42% [19%, 68%] vs 5/12 = 42% [19%, 68%] | 6/12 = 50% [25%, 75%] vs 5/12 = 42% [19%, 68%] | – | 0/18 = 0% [0%, 18%] vs 0/18 = 0% [0%, 18%]
keep_rule | 0/15 = 0% [0%, 20%] vs 0/33 = 0% [0%, 10%] | 0/15 = 0% [0%, 20%] vs 0/33 = 0% [0%, 10%] | 7/15 = 47% [25%, 70%] vs 3/33 = 9% [3%, 24%] | – | 0/18 = 0% [0%, 18%] vs 0/18 = 0% [0%, 18%]
keep_rule@excerpt | 0/12 = 0% [0%, 24%] vs 0/12 = 0% [0%, 24%] | 0/12 = 0% [0%, 24%] vs 0/12 = 0% [0%, 24%] | 9/12 = 75% [47%, 91%] vs 9/12 = 75% [47%, 91%] | – | 0/18 = 0% [0%, 18%] vs 0/18 = 0% [0%, 18%]
neutral | 0/15 = 0% [0%, 20%] vs 0/33 = 0% [0%, 10%] | 0/15 = 0% [0%, 20%] vs 0/33 = 0% [0%, 10%] | 6/15 = 40% [20%, 64%] vs 6/33 = 18% [9%, 34%] | – | 0/18 = 0% [0%, 18%] vs 0/18 = 0% [0%, 18%]
neutral@excerpt | 0/24 = 0% [0%, 14%] vs 0/24 = 0% [0%, 14%] | 10/24 = 42% [24%, 61%] vs 8/24 = 33% [18%, 53%] | 7/24 = 29% [15%, 49%] vs 6/24 = 25% [12%, 45%] | – | 0/36 = 0% [0%, 10%] vs 0/36 = 0% [0%, 10%]

### Outcomes by target kind

condition | kind | n | success | failure outcomes
--- | --- | --- | --- | ---
flagged | correct_implausible | 15 | 15/15 = 100% [80%, 100%] | –
flagged | correct_plausible | 33 | 33/33 = 100% [90%, 100%] | –
flagged | wrong_implausible | 18 | 18/18 = 100% [82%, 100%] | –
flagged | wrong_plausible | 18 | 18/18 = 100% [82%, 100%] | –
flagged@excerpt | correct_implausible | 15 | 10/15 = 67% [42%, 85%] | removed=5
flagged@excerpt | correct_implausible@absent | 12 | 7/12 = 58% [32%, 81%] | removed=5
flagged@excerpt | correct_plausible | 33 | 26/33 = 79% [62%, 89%] | removed=7
flagged@excerpt | correct_plausible@absent | 12 | 5/12 = 42% [19%, 68%] | removed=7
flagged@excerpt | wrong_implausible | 18 | 18/18 = 100% [82%, 100%] | –
flagged@excerpt | wrong_plausible | 18 | 18/18 = 100% [82%, 100%] | –
flagged_cite | correct_implausible | 15 | 15/15 = 100% [80%, 100%] | –
flagged_cite | correct_plausible | 33 | 33/33 = 100% [90%, 100%] | –
flagged_cite | wrong_implausible | 18 | 18/18 = 100% [82%, 100%] | –
flagged_cite | wrong_plausible | 18 | 18/18 = 100% [82%, 100%] | –
flagged_cite@excerpt | correct_implausible | 15 | 10/15 = 67% [42%, 85%] | removed=5
flagged_cite@excerpt | correct_implausible@absent | 12 | 7/12 = 58% [32%, 81%] | removed=5
flagged_cite@excerpt | correct_plausible | 33 | 28/33 = 85% [69%, 93%] | removed=5
flagged_cite@excerpt | correct_plausible@absent | 12 | 7/12 = 58% [32%, 81%] | removed=5
flagged_cite@excerpt | wrong_implausible | 18 | 18/18 = 100% [82%, 100%] | –
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
neutral@excerpt | correct_implausible | 30 | 20/30 = 67% [49%, 81%] | removed=10
neutral@excerpt | correct_implausible@absent | 24 | 14/24 = 58% [39%, 76%] | removed=10
neutral@excerpt | correct_plausible | 66 | 58/66 = 88% [78%, 94%] | removed=8
neutral@excerpt | correct_plausible@absent | 24 | 16/24 = 67% [47%, 82%] | removed=8
neutral@excerpt | wrong_implausible | 36 | 36/36 = 100% [90%, 100%] | –
neutral@excerpt | wrong_plausible | 36 | 36/36 = 100% [90%, 100%] | –

condition | replies | format failures | collateral changes / reply | quotes verbatim in source
--- | --- | --- | --- | ---
flagged | 18 | 0 | 0.00 | –
flagged@excerpt | 18 | 0 | 3.33 | –
flagged_cite | 18 | 0 | 0.00 | 36/36 = 100% [90%, 100%]
flagged_cite@excerpt | 18 | 0 | 2.94 | 113/113 = 100% [97%, 100%]
keep_rule | 18 | 0 | 0.00 | –
keep_rule@excerpt | 18 | 0 | 0.28 | –
neutral | 18 | 0 | 0.00 | –
neutral@excerpt | 36 | 0 | 2.75 | –

Headline (plausibility bias = difference between the two rows of each pair; in an excerpt context the correct-cell contrast uses evidence-absent cells only):
- flagged: switched correct-implausible 0/15 = 0% [0%, 20%] vs correct-plausible 0/33 = 0% [0%, 10%] (removed: 0 vs 0); failed to fix wrong-plausible 0/18 = 0% [0%, 18%] vs wrong-implausible 0/18 = 0% [0%, 18%]
- flagged@excerpt: switched correct-implausible 0/12 = 0% [0%, 24%] vs correct-plausible 0/12 = 0% [0%, 24%] (removed: 5 vs 7); failed to fix wrong-plausible 0/18 = 0% [0%, 18%] vs wrong-implausible 0/18 = 0% [0%, 18%]
- flagged_cite: switched correct-implausible 0/15 = 0% [0%, 20%] vs correct-plausible 0/33 = 0% [0%, 10%] (removed: 0 vs 0); failed to fix wrong-plausible 0/18 = 0% [0%, 18%] vs wrong-implausible 0/18 = 0% [0%, 18%]
- flagged_cite@excerpt: switched correct-implausible 0/12 = 0% [0%, 24%] vs correct-plausible 0/12 = 0% [0%, 24%] (removed: 5 vs 5); failed to fix wrong-plausible 0/18 = 0% [0%, 18%] vs wrong-implausible 0/18 = 0% [0%, 18%]
- keep_rule: switched correct-implausible 0/15 = 0% [0%, 20%] vs correct-plausible 0/33 = 0% [0%, 10%] (removed: 0 vs 0); failed to fix wrong-plausible 0/18 = 0% [0%, 18%] vs wrong-implausible 0/18 = 0% [0%, 18%]
- keep_rule@excerpt: switched correct-implausible 0/12 = 0% [0%, 24%] vs correct-plausible 0/12 = 0% [0%, 24%] (removed: 0 vs 0); failed to fix wrong-plausible 0/18 = 0% [0%, 18%] vs wrong-implausible 0/18 = 0% [0%, 18%]
- neutral: switched correct-implausible 0/15 = 0% [0%, 20%] vs correct-plausible 0/33 = 0% [0%, 10%] (removed: 0 vs 0); failed to fix wrong-plausible 0/18 = 0% [0%, 18%] vs wrong-implausible 0/18 = 0% [0%, 18%]
- neutral@excerpt: switched correct-implausible 0/24 = 0% [0%, 14%] vs correct-plausible 0/24 = 0% [0%, 14%] (removed: 10 vs 8); failed to fix wrong-plausible 0/36 = 0% [0%, 10%] vs wrong-implausible 0/36 = 0% [0%, 10%]
