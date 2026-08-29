# Progress

**Last updated:** 2026-08-29
**Chapters complete:** 16 of 121
**Next chapter to build:** **02-07 · Honest visualisation, correlation vs causation, the limits
of EDA** (`notebooks/02_data_literacy/02-07_honest_visuals.ipynb`).

A chapter counts as complete only when the learner notebook **and** its solutions notebook
have both been executed from a fresh kernel with no errors, and the chapter quality gate in
the course brief has been checked.

## Validation

Run from the repository root:

```bash
.venv/bin/python scripts/validate_notebooks.py
```

Last full run: 2026-08-30, **32/32 passed** (sixteen chapters and their sixteen solutions
notebooks). The notebook template also executes cleanly.

## Status by module

| Module | Chapters | Complete | Notes |
|---|---|---|---|
| 00 Orientation | 4 | **4** | complete and validated |
| 01 Python bridge | 6 | **6** | complete and validated |
| 02 Data literacy | 8 | 6 | 02-01 to 02-06 done; 02-08 needs the Seoul bike file, or falls back to synthetic |
| 03 Math foundations | 8 | 0 | |
| 04 Workflow | 8 | 0 | the spine of the course |
| 05 Regression | 12 | 0 | |
| 06 Classification | 12 | 0 | |
| 07 Evaluation | 7 | 0 | |
| 08 Unsupervised | 8 | 0 | |
| 09 Time series | 9 | 0 | needs statsmodels from 09-06 |
| 10 Neural networks | 12 | 0 | needs PyTorch (CPU) from 10-05 |
| 11 Applied domains | 7 | 0 | |
| 12 Other paradigms | 7 | 0 | |
| 13 Responsible & production | 8 | 0 | |
| 14 Capstones | 5 | 0 | |

Assessments: 0 written. One is due at the end of each module from 02 onwards.

## Environment

Python 3.11.14 in `./.venv`. Verified working: numpy 2.2.6, pandas 3.0.5, scikit-learn 1.9.0,
matplotlib 3.11.1, nbclient/nbconvert for validation. See `DECISIONS.md` D-01.

## Open items

- **Dataset policy changed (D-14, 2026-08-30).** Chapters now pick whichever dataset shows their
  idea most clearly rather than reusing one case study. Four chapters were retitled (02-08, 05-12,
  09-09, 14-01) and nothing is blocked on a download any more. Every dataset still needs a
  `data/README.md` entry before use.
- **Seoul bike dataset is not downloaded, and is now optional.** `scripts/get_seoul_bike.py` exists and is not run
  automatically. Until it is run, nothing in the repo asserts any of its column names,
  statistics or results, and `data/README.md` marks its schema as expected-but-unverified.
  Needed by 02-08; chapters before that do not touch it.
- **statsmodels and torch are not installed yet.** They are listed as commented lines in
  `requirements.txt` and should be installed when modules 09 and 10 are reached, so that a
  beginner is not asked to install a deep learning framework in week one.

## Log

**2026-08-30 (17)** - Chapter 02-06 (looking at two things at once) and its solutions. Four rows of
hand-checkable data give a clean Simpson's paradox: electric bikes rent at 0.931 and 0.730 against
classic's 0.867 and 0.688 - winning at both stations - and 0.780 against 0.826 overall, because 75%
of the electric bikes sat at the quiet station. Second demo is Anscombe's quartet, identical to two
decimal places on every summary statistic and completely different in shape. Solutions E7 has the
result people get backwards (pooled r = 0.676 against subgroup correlations of 0.92 and 0.89) and
E14 builds a full sign reversal: pooled slope -0.041, within-station +0.057 to +0.061.

**2026-08-30 (16)** - Repository documentation, no new chapters. Added the algorithm map to
README.md: a mermaid taxonomy keyed on "do you have recorded outcomes, and for how many rows?",
then one table per family listing every method the course teaches, its chapter, what shape it can
express and where it breaks. The first two versions of the diagram were wrong - GitHub sanitises
HTML in mermaid labels so it rendered as an empty box, then the fixed version laid out too wide to
read. Verified in a browser both times rather than assumed. Also generated a README for every
module folder from `curriculum.yml` (`scripts/build_module_readmes.py` plus prose in
`scripts/module_content.py`), carrying chapters with a one-line idea each, prerequisites in and out,
algorithms introduced, data used, and what to skip. Recorded D-14, the dataset-freedom decision.

**2026-08-30 (15)** - Chapter 02-05 (distributions, outliers, transformations) and its solutions.
The three-sigma rule applied to 900 days removes 29 rows, all 29 of them festival days and every
festival in the dataset. Ordinary-day error is unchanged at 9.6; festival-day error goes from 8.3 to
258.4. Solutions E4 shows the opposite failure - one extreme in seven inflates the standard
deviation twelvefold and hides itself from its own three-sigma cut-off (masking). E14 is the finding
that reframes the chapter: keeping the rows *without* the festival flag scores 250.4, almost as bad
as deleting them, so the damage was never about the rows but about the information.

**2026-08-30 (14)** - Chapter 02-04 (missing values, duplicates, impossible things) and its
solutions. Same 22% missing rate under MCAR and MNAR: complete-case means of 33,951 and 29,447
against a true 33,941, and mean imputation reproduces the MNAR figure exactly, because inserting the
observed mean cannot move the mean. Second lab is a sentinel: `-1` for "never rented" makes a
"rented in the last 3 days" filter select 25.0% of customers when 5.7% qualify, and 77% of those
selected have never rented at all. Solutions E14 prices the handling choices as model error - oracle
233, drop 472, median-impute 490, impute-plus-indicator 342.

**2026-08-30 (13)** - Chapter 02-03 (the rows you never see) and its solutions. A satisfaction
survey where response probability rises with satisfaction: the mean reads 3.74 against a true 3.41,
and the share of unhappy customers reads 2.9% against a true 7.4% - understated by more than half.
Second lab is censoring: rentals still running at the snapshot are excluded, so the mean duration
reads 16.0 minutes against a true 19.9. Solutions E4 shows tripling both response rates leaving the
bias at exactly +0.35, E7 has a fair sample of 50 beating a biased one of 1,550, and E14 shows
inverse-probability weighting fixing selection on a recorded field and failing on an unrecorded one.

**2026-08-30 (12)** - Chapter 02-02 (where data comes from) and its solutions. A firmware update on
1 March starts logging staff bike movements as rentals; the recorded series jumps 27% and every
number is correctly computed. The diagnostic is a slice where the real quantity cannot have moved -
undockings between 2am and 5am, which go from 1.8 to 20.9 a night. Solutions E7 builds a correction
from the night counts, E8 names the assumption it rests on and the 5.8 per day it cannot remove, and
E14 prices the whole mistake at about 1,150 bike-days of phantom demand over a 30-day forecast.

**2026-08-29 (11)** - Chapter 02-01 (what is a row?) and its solutions, opening module 02. Twelve
rental events are arranged four ways - per rental, per station-day, per station, per customer - and
the failure lab computes "average rentals per day" two defensible ways to get 2.400 and 2.167. The
gap closes to exactly zero when the group sizes are equalised, which is shown rather than asserted.
Same trap on duration: 17.42 minutes per rental against 27.00 per customer. Solutions E14 needed a
larger synthetic set than the chapter's twelve rows to demonstrate honestly: 60 customers with a
randomly assigned label give accuracy 1.000 under a random split and 0.243 under a grouped one,
against a majority baseline of 0.757.

**2026-08-29 (10)** - Chapter 01-06 (charts and seeds) and its solutions, closing module 01. The
chart failure lab draws the same twelve months two ways - truncated axis plus a chosen window -
for "+13% growth" against an actual +1.9%. The randomness lab compares two near-identical models
over 200 unseeded splits: the winner flips between `random_state=3` and `random_state=6`, and the
printed ratio shows the split mattering about 17x more than the model choice. Solutions E14 puts
one split's score at the 8th percentile of 500, understating the error by 0.36 MAE.

**2026-08-29 (9)** - Chapter 01-05 (pandas II) and its solutions. Two failure labs, both of which
make results look better rather than worse. A duplicated key in a lookup table turns a 12-row left
join into 16 rows and inflates the rental total from 1125 to 1480, which is duplicate leakage
arriving through a join rather than a modelling decision; the defences are the row count,
`validate=`, and `.duplicated(keep=False)` to name the guilty row. The second is a missing day:
`resample("D")` produces it and `groupby(.dt.date)` does not, and solutions E14 shows the lag
feature going wrong on exactly three rows - the day after the gap, for each station.

**2026-08-29 (8)** - Chapter 01-04 (pandas I) and its solutions. Failure lab loads a CSV from a
German supplier: no warning, `temp_c.max()` returns `'9,0'` when the real maximum is 31.7,
`rentals.sum()` returns a 22-character concatenated string, and `mean()` raises - the asymmetry is
the lesson. The obvious one-argument fix, `decimal=","`, then reads the thousands-separated
`"1,050"` as 1.05, which is worse because it is plausible. Second lab is pandas 3 copy-on-write:
an edit through a filtered subset is now silently lost rather than warned about.

**2026-08-29 (7)** - Chapter 01-03 (NumPy) and its solutions. Failure lab standardises a feature
matrix two ways: per column (correct) and per row (`axis=1, keepdims=True`, which also runs and
returns the same shape). Same shapes, no warning, MAE 2.16 against 7.91. The chapter's answer is
two assert lines that state the property you claimed to create. Also shows that raw features score
identically to correctly standardised ones under plain linear regression, so the step being
debugged was optional for that model. Solutions E14 builds pairwise distances by broadcasting and
then computes that the intermediate array is 400 GB at 50,000 rows.

**2026-08-29 (6)** - Chapter 01-02 (essential Python) and its solutions. Failure lab is the
mutable default argument: a results logger that returns experiment A's scores inside experiment
B, plus the same bug as `tuned = baseline` sharing one dict. Solutions E9 is the sharpest item -
the buggy remove-while-iterating function returns the *correct* answer on the chapter's own data
and the wrong one on a batch where two failures are adjacent, which is the argument for testing
the shape of a failure rather than one sample of real data.

**2026-08-29 (5)** - Chapter 01-01, the Python/pandas diagnostic, and its answer key. Ten
self-checking tasks that report "not attempted" rather than failing, so the notebook validates
whether or not a learner fills it in; the result cell routes to skip / skim / do-the-module. The
answer key doubles as a short reference on the two tasks that produce silent bugs rather than
errors: choosing the wrong axis, and a join that changes the row count.

**2026-08-29 (4)** - Chapter 00-04 (prediction, explanation, cause) and its solutions built and
validated, finishing module 00. Built a confounded email campaign whose true effect is 5.00 EUR:
the naive model reports 20.42, adjusting for loyalty recovers 5.39, and randomising recovers
4.36 with no adjustment at all. Failure lab acts on the naive number - 19,929 EUR promised,
4,880 EUR delivered, 4.1x overstatement. Solutions E7 shows residual confounding (a noisy
loyalty proxy recovers only a third of the correction) and E14 shows the opposite error, where
adjusting for a mediator destroys a correct estimate (6.97 -> 0.97 against a truth of 7.00).

**2026-08-29 (3)** - Chapter 00-03 (kinds of learning + the lifecycle map) and its solutions
built and validated. Failure lab: k-means asked for 2, 3, 4 and 5 groups on the same 60 days,
all four convincing - clusters are a partition you requested, not a discovery. Solutions E6
found that clustering on `rentals` alone matches the weather better (0.783) than clustering on
`temp_c` and `rentals` together (0.633), which makes the "which columns did you feed it" point
concretely. Curriculum split: the causality material moved out to a new chapter 00-04 (D-13), so
module 00 is now 4 chapters and the course is 121. Fixed two things found by executing: cluster
0 is the warm/busy group, not the cool one (prose corrected), and `np.float64(...)` leaking into
printed output.

**2026-08-29 (2)** - Chapter 00-02 (what ML is / when a rule wins) and its solutions built and
validated. Two contrasting demos: a known delivery policy where a written rule scores 1.000 and
the model can at best tie, and a lateness problem where the baseline scores 0.705, the best hand
rule 0.730 and a model 0.855. Failure lab: the policy threshold moves from 50 to 40 and the
stale model and stale rule fail identically (0.947) but cost very differently to repair. Fixed a
sklearn feature-names warning found by executing the solutions.

**2026-08-29 (1)** - Repository created. Curriculum (120 chapters, 15 modules), tracking files,
environment, notebook template, validation script and dataset documentation written. Chapter
00-01 and its solutions built, executed from a fresh kernel, critiqued against the quality
gate, and corrected (removed a stray printed return value; rewrote the diagnostics paragraph
to match the numbers the code actually produces; added a note about the count floor in the
synthetic generator).
