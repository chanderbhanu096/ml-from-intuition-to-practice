# Progress

**Last updated:** 2026-08-30
**Chapters complete:** 24 of 121
**Next to build:** **03-07 · Vectors, distance, norms, dot products, matrices, shapes**
(`notebooks/03_math_foundations/03-07_vectors_matrices.ipynb`).

A chapter counts as complete only when the learner notebook **and** its solutions notebook
have both been executed from a fresh kernel with no errors, and the chapter quality gate in
the course brief has been checked.

## Validation

Run from the repository root:

```bash
.venv/bin/python scripts/validate_notebooks.py
```

Last full run: 2026-08-30, **50/50 passed** (twenty-four chapters, their twenty-four solutions
notebooks, and the module 02 assessment with its solutions). The notebook template also executes
cleanly. Notebooks are committed without stored outputs (D-15).

## Status by module

| Module | Chapters | Complete | Notes |
|---|---|---|---|
| 00 Orientation | 4 | **4** | complete and validated |
| 01 Python bridge | 6 | **6** | complete and validated |
| 02 Data literacy | 8 | **8** | complete and validated, assessment written |
| 03 Math foundations | 8 | 6 | 03-01 to 03-06 done |
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

**2026-08-30 (27)** - Chapter 03-06 (lines, slopes, and logarithms) and its solutions, the
vocabulary chapter for module 05. Six exact data points - rentals rising 45 per 3 degrees - give a
slope of exactly 15 and an intercept of exactly 0, which sets up the first failure lab: the fit is
perfect on all six days and the intercept describes 0 degrees, four degrees below anything observed.
Centring moves the intercept to 292.5, which is exactly the mean rentals, at no cost to the slope.
Re-measuring in Fahrenheit gives 8.3333 and -266.6667 for the same relationship, both predicting 300
rentals for the same day, which is the argument against comparing raw coefficients across features.
Logarithms introduced as counting multiplications: a fleet growing 25% a month adds 10, then 12.5,
then 15.6, while always multiplying by 1.25, and a straight line fitted to its log recovers exactly
0.22314 = ln(1.25) and exp(intercept) = 40.00, with a doubling time of 3.11 months. The four forms of
the line are tabulated with a worked example of each, including y ~ log(x) adding exactly 3 ln 2 =
2.0794 per doubling and a log-log fit whose slope is exactly the exponent -0.4000. Second failure lab
is the percentage conversion: a coefficient of 0.70 on a logged outcome is 101.38%, not 70%, and 1.00
is 171.83%. Solutions E8 fits a straight line to noisy exponential growth and finds the failure
visible in the residuals a year before it matters - a clean U shape, and a month-24 prediction of 960
against a truth of 8,470. E9 shows a log-log fit returning 1.1683 instead of 1.5 once an additive
constant of 20 is present. E16 compares all four forms on held-out data with the error computed on the
original scale, where log-log wins at 8.699 and the logged-outcome form is worst at 50.765, and draws
the rule that transformed fits must be brought back to the original units before any comparison.
Added `scripts/check_outputs.py`, a linter over an executed notebook's outputs that catches literal
'%%' from a print with no format operator, numpy scalar reprs, negative zeros and nan/inf - three of
which had each slipped through at least once.

**2026-08-30 (26)** - Chapter 03-05 (Bayes' rule you can do on paper) and its solutions. Teaches
the natural-frequency method first - invent 100,000 people, turn every rate into a count, fill four
cells, divide - which gives 4.72% for the screening problem without writing the formula down. The
formula is then introduced as a name for what was just counted, and checked against it to six
decimals. Odds form next, because "multiply the odds by 99" is doable in your head where the
percentage form is not, and because it exposes the asymmetry: a positive multiplies the odds by 99 to
reach 1 in 21, while a negative multiplies by 0.0101 and reaches 1 in 197,902. Sequential updating
gives 4.72%, 83.06% and 99.79% for one, two and three positives. The failure lab then takes that
apart. Two models of why a test errs - independent noise, or a stable trait in 1% of healthy people -
produce an identical 1% false-positive rate and are indistinguishable from any measurement of the
test. Simulated over forty million people, two positives mean 0.8308 under independent errors and
0.0468 under the stable trait, while the sequential calculation returns 0.8306 in both. Bayes' rule
is not wrong; the likelihood is, because P(two positives given healthy) is 0.0001 in one world and
0.01 in the other. This is 03-04's brake cables in a new setting. Closes on where the prior comes
from, with the same test giving 4.7% under random screening and 91.7% after a specialist referral.
Solutions E8 answers the question the chapter leaves open by sweeping the share of correlated errors
while holding the overall false-positive rate pinned at 0.0100: confirmatory value falls from 0.8225
to 0.0468, and a twentieth of the errors being correlated already halves it. E12 explains naive
Bayes' saturated probabilities as the same effect, and E16 extends to three hypotheses with a warning
about exhaustiveness.

**2026-08-30 (25)** - Chapter 03-04 (probability, by counting) and its solutions. Level 0
mathematics: every probability in the chapter is one count divided by another, from a four-cell table
of 1,000 inspected bikes - 36 cracked-and-alarmed, 4 missed, 96 false alarms, 864 quiet and sound.
The first failure lab is confusing the inverse: P(alarm given cracked) is 0.9000 and P(cracked given
alarm) is 0.2727 from the same 36 bikes, a factor of 3.30, because 960 sound bikes produce 96 false
alarms while 40 cracked ones produce 36 true ones. Holding the sensor fixed and varying only the base
rate moves P(cracked given alarm) from 0.0089 to 0.9310, which is the chapter's central point - a
detector's usefulness is not a property of the detector. Both quantities are then named as recall and
precision, so module 07's metrics arrive as two denominators rather than two definitions. Independence
shown two ways on a colour table that is exactly independent (expected counts 16, 384, 24, 576, all
matching observed) against the sensor table where independence predicts 5.3 and observes 36. Second
failure lab: two brake cables whose individual failure rate is 0.998% either way, but which fail
together 1 in 247 rather than 1 in 10,040 when they share a batch - 40.7 times the independent
calculation, confirmed by simulating ten million bikes, with P(second fails given first failed) at
0.4082 against 0.00997. Solutions E6 extends it to three and four cables, where the ratio reaches
1,833 and 82,672, so redundancy buys least exactly where it is claimed to buy most. E9 builds a table
that is dependent in each of two workshops in opposite directions and exactly independent when pooled,
which is 02-06's Simpson's paradox in probability notation. E10's screening calculation gives 4.7%,
and E16 shows the batch dependence is detectable from failures alone at a fleet of only 200. Notebook
executed to a scratchpad copy rather than in place, per D-15.

**2026-08-30 (23)** - Chapter 03-03 (error bars from the data you actually have) and its solutions.
The bootstrap in four lines, checked against a truth we still hold: resampling one week of seven
mornings gives a standard error of 1.6483 against the 1.6048 that 03-02 needed a million-row
population to compute. Stresses that the bootstrap distribution centres on the sample's own estimate,
4.75, not on the truth, 6.01 - it measures precision and can never detect bias. Failure lab one
measures what "95% confidence" delivers: coverage is 0.859 at n = 7, 0.933 at n = 30 and only reaches
0.948 at n = 300, because resamples of a small sample under-represent the tail, so the interval you
can compute is too narrow exactly when you need it. Forty intervals plotted against the truth, 37
containing it. Failure lab two is the total one: bootstrap intervals for a maximum have coverage
0.000 at every sample size, and the width shrinks from 0.961 to 0.030 as n grows, so the method
becomes more confident while staying wrong - a resample cannot contain a value the sample did not
have. Closes with the reason to learn it: intervals for a difference between two groups (2.190, CI
0.999 to 3.420, true value 1.502) and for a ratio (0.6242, CI 0.4735 to 0.8110), the latter visibly
asymmetric and having no simple formula. Solutions E12 is worse than the exercise implies - naive
resampling of an autocorrelated series gives an interval of -0.0081 to 0.0077 for a slope whose
observed value is 0.0482, so it is not merely 1.8x too narrow but centred on zero and excluding the
estimate. E16 builds an interval for the maximum that works, with coverage 0.955/0.951/0.952, and
draws the general trade: assumptions buy extrapolation and fail quietly, while the bootstrap assumes
almost nothing and fails loudly.

**2026-08-30 (24)** - Repository consistency fix, no new content. Chapters 02-07 onward had been
committed with stored notebook outputs, which every earlier chapter did not have: 02-07 and 02-08
were 328 KB and 288 KB against roughly 29 KB for comparable chapters, almost all of it base64 PNG.
Stripped outputs and execution counts from all ten affected notebooks, re-validated the whole course
at 44/44, and wrote the convention down as D-15 so it does not recur - notebooks are verified by
execution and committed clean, because the learner should run them rather than read them, and because
a one-word prose fix should not appear as a hundred lines of changed image data.

**2026-08-30 (22)** - Chapter 03-02 (why two samples never agree) and its solutions. Invents a
population of a million bus mornings so the truth is knowable - true mean 6.0064, sd 4.2460 - and
then reopens 03-01's answer: across 100,000 weeks of seven mornings the sample means centre correctly
on 6.0031 but 95% of them fall between 3.27 and 9.57, so "6 minutes late" was correct with imaginary
precision. Standard error verified against sd/sqrt(n) at four sample sizes, with the relative column
landing on 1.000, 0.500, 0.249, 0.124 - quadruple the data to halve the error. First failure lab is
sd against se: the sample sd climbs from 3.91 to 4.24 and stops, while the se falls from 1.60 to
0.20, with an honest footnote that ddof=1 makes the variance unbiased and not its square root.
Central limit theorem measured rather than asserted - skewness of the sampling distribution 1.399,
0.991, 0.625, 0.250, 0.146 at n = 1, 2, 5, 30, 100 - so "n = 30 is enough" is folklore with a rate
attached. Second failure lab: two arms drawn from the same population, 100 mornings each, produce a
13.3% "winner"; across 40,000 such trials the typical apparent gap is 6.76% and 61.6% exceed 5%. The
spread of the difference comes out 0.6030 against the predicted se x sqrt(2) = 0.6005, which is the
variances-add fact 03-01 promised. Closes by reversing the robustness story: on the moderately skewed
population the median is 13% less precise than the mean, and on a population where 3% of mornings are
breakdowns it is five times more precise. Solutions E8 is the uncomfortable one - the standard error
you can compute from your own sample of 7 averages 1.4878 against a truth of 1.6086, biased low by
7.5%, with 64.2% of samples understating their own uncertainty. E15 shows the sqrt(n) law is a fact
about averages only: the se of the maximum falls by a factor of 1.25 while the se of the mean falls
by 32, and the average maximum grows without limit.

**2026-08-30 (21)** - Chapter 03-01 (summaries: the arithmetic behind typical and spread) and its
solutions, opening module 03. Seven bus-lateness values chosen so every hand calculation comes out
whole: sum 42, mean 6, median 5, deviations summing to zero, sum of squares 84, variance 12 or 14.
The chapter's spine is that the mean minimises total squared error and the median minimises total
absolute error - shown by grid search, with the squared-error minimum landing on 84, the same number
computed by hand - which is the same fork as RMSE against MAE in module 07 and least squares against
least absolute deviation in 05. Failure lab: np.var returns 12.0 and pd.Series.var returns 14.0 on
identical data with no warning, a 16.7% difference in variance and 8% in standard deviation, because
numpy defaults to ddof=0 and pandas to ddof=1. Why n-1 is then measured rather than derived: over
200,000 samples of size 5 from a population with variance exactly 1, the /n formula averages 0.8017
against the predicted (n-1)/n = 0.8000, and /(n-1) averages 1.0022. Second failure lab: numpy has
thirteen quantile methods and on seven values they give six distinct IQRs from 5.0 to 6.0, so a
quartile on a small sample is a convention. Breakdown demonstrated - one value moved from 12 to 1000
takes the mean from 6.00 to 147.14 while the median stays at exactly 5.0 - with the caution that
robustness would have hidden 02-05's festivals. Closes with the weighted mean: three bus routes
average 12.00 minutes unweighted and 5.70 weighted. Solutions E16 is the payoff - minimising the sum
of errors raised to power p gives the median at 1, the mean at 2, and the midrange (7.0) as p grows,
so all three familiar summaries are one family indexed by how much a large error should hurt. E8
confirms the n-1 correction is exact on an exponential population too, so it is not a normality
result. E9 catches a real wrinkle: a 10% trim on seven values drops floor(0.7) = 0 points and is
silently identical to the mean.

**2026-08-30 (20)** - Module 02 cumulative assessment and its solutions, the first assessment in
the course. 40 marks in three parts: ten recall questions, eight computed quantities, three judgement
questions. Part B marks itself - answers are stored as salted SHA-256 digests so the notebook source
does not reveal them, with a plus or minus 0.01 tolerance on decimals; verified that all eight correct
answers pass, that wrong answers and unknown task ids fail, and that the tolerance works. The dataset
is synthetic library loans, 1,176 delivered rows, seeded, carrying four planted defects that have to
be found rather than announced: 75 duplicate rows overstating the loan count by 6.81%; a -1 sentinel
for unreturned loans (86 rows, 7.81%) that drags the naive mean of days_kept from 13.03 down to
11.93; a 28-day ceiling holding 114 returned loans (11.23%) against 12 at 27 days; and an
aggregation trap where the mean over loans is 13.03 and the mean over members is 16.65, because
heavy borrowers return faster and contribute more rows. Part C is a Simpson reversal: ebooks renew
more at central (0.647 vs 0.618) and at riverside (0.416 vs 0.351) but less overall (0.471 vs 0.543),
because 76.4% of ebook loans sit at riverside. Full marks on C1 require naming the condition under
which the pooled answer would be the right one. Ends with a score table and a remediation map from
each question to the chapter that covers it. Module 02 is now complete: eight chapters, eight
solutions, one assessment, 38/38 notebooks passing.

**2026-08-30 (19)** - Chapter 02-08 (a full exploratory analysis and the document it produces) and
its solutions, closing module 02. First chapter on a real dataset: California housing, 20,640 census
block groups from 1990, fetched from scikit-learn and not committed (D-14). It has no missing values
and no duplicate rows and is misleading in four ways, which is the chapter's spine. Verified findings:
household counts recover exactly from Population/AveOccup (largest deviation from a whole number
0.00000000 across all 20,640 rows), which explains the impossible averages - the worst row is 6
households and 7,460 residents, giving AveOccup 1243.33; the 79 rows with AveRooms > 20 or AveOccup >
20 are 0.38% of the data and were suppressing two real relationships, r(AveOccup, target) -0.024 with
them and -0.242 without, r(AveRooms, target) 0.152 and 0.274; three ceilings found by counting rows
at the maximum rather than reading it - 965 rows at $500,001 (4.68%), 1,273 at HouseAge 52, 49 at
MedInc 15.0001; the censored rows are the richest (mean MedInc 7.83 against 3.68) and the cap moves a
one-column slope from 0.4179 to 0.3999. Chapter ends by writing a data dictionary and a limitations
section to a file, each limitation naming a conclusion it forbids. Solutions E7 is the strongest
aggregation result in the module and it is real: r(HouseAge, value) is +0.106 statewide but negative
in six of eight k-means regions (-0.335, -0.324, -0.278), while r(MedInc, value) holds at 0.51 to
0.75 everywhere - one relationship survives disaggregation and one does not. E11 was rewritten after
checking it: a whole-frame three-sigma sweep removes 846 rows, flags nothing at all on the target
(its cut-off, 5.530, sits above the censored maximum of 5.00001), catches 77 of the 79 artefacts at a
cost of 769 ordinary rows, and deletes the expensive end of the market (mean target 3.07 removed
against 2.03 kept). Dataset fully documented in data/README.md including that no licence accompanies
the file. Also fixed by executing: MedInc has 49 rows at the exact ceiling, not the 51 an earlier
`>= 15` probe suggested; two slope figures and one correlation quoted from a probe that used a train
split rather than the notebook's full fit; and a city name that had not been verified from the
coordinates, replaced with the coordinates.

**2026-08-30 (18)** - Chapter 02-07 (showing what you found, without saying more than you found)
and its solutions. Three demonstrations, all executed. A bar chart of two docking-rack averages is
accurate - 45.54 s against 40.13 s - and hides that 28.5% of new dockings are slower than the old
average and a random new docking wins only 64.6% of the time. Two independently generated random
walks correlate at 0.914 on levels and -0.011 on their monthly changes, which is the twin-axis trap
and a forward reference to module 09. The centrepiece is three worlds - opens cause rides, rides
cause opens, enthusiasm causes both - tuned so all three land on r = 0.754 exactly and are
standardised so the clouds are indistinguishable; simulating the intervention gives 0.800 extra
rides in the first world and exactly zero in the other two. Second failure lab screens 40 pure-noise
columns against a pure-noise target: the winner is r = 0.254, it comes back at -0.045 on fresh data,
and 60.1% of noise runs beat it (the best-of-40 median is 0.264 against 0.074 for one pre-chosen
column), so the finding is below average for noise. Chapter closes with a table of what EDA can and
cannot settle and a four-line format for writing a finding. Solutions E15 adds a fourth world -
mutual causation, b = 1/3 giving r = 2b/(1+b squared) = 0.600 - which is equally indistinguishable
and has a third distinct intervention effect of 0.333. Fixed by executing: a stray returned tuple
printing as np.float64, a literal `5%%` in a non-formatted string, a claim that the intervention
effect was 0.800 standard deviations when it is 0.800 rides units, and "about a third" for a share
that is 28.5%.

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
