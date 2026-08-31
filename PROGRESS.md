# Progress

**Last updated:** 2026-08-31
**Chapters complete:** 40 of 121
**Next to build:** **05-07 · Polynomial and interaction features; under/overfitting**
(`notebooks/05_regression/05-07_capacity.ipynb`).

A chapter counts as complete only when the learner notebook **and** its solutions notebook
have both been executed from a fresh kernel with no errors, and the chapter quality gate in
the course brief has been checked.

## Validation

Run from the repository root:

```bash
.venv/bin/python scripts/validate_notebooks.py
```

Last full run: 2026-08-31, **80/80 passed** (thirty-seven chapters, their thirty-seven solutions
notebooks, and the module 02, 03 and 04 assessments with their solutions). The notebook template also executes
cleanly. Notebooks are committed without stored outputs (D-15).

## Status by module

| Module | Chapters | Complete | Notes |
|---|---|---|---|
| 00 Orientation | 4 | **4** | complete and validated |
| 01 Python bridge | 6 | **6** | complete and validated |
| 02 Data literacy | 8 | **8** | complete and validated, assessment written |
| 03 Math foundations | 8 | **8** | complete and validated, assessment written |
| 04 Workflow | 8 | **8** | complete and validated, assessment written |
| 05 Regression | 12 | 6 | 05-01 to 05-06 done |
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

**2026-08-31 (6)** - Chapter 05-06 (gradient descent from scratch) and its solutions, 6 figures in the
chapter and 4 in the solutions. 03-08 already built the five-line loop for one parameter and did the
qualitative learning-rate and scaling failure labs, so this chapter is the quantitative version: the
full vector gradient, the gradient check, the exact stability bound, batch sizes, momentum, and what
"converged" is worth.

**The stability bound is derived and then verified as an exact boundary.** `rate < 1 / lambda_max(X'X/n)`
gives 0.959567 on the standardised design, and the sweep confirms it: 0.50x the limit converges in 5
steps, 0.80x in 22, 0.95x in 104, 0.99x in 538, and 1.00x never. Approaching the limit is a hundred times
*slower* than sitting at half of it, so "the largest rate that does not diverge" is bad advice twice.

**The scaling result is the chapter's headline: 1,776,054 steps against 4.** Condition number 365,727
raw against 1.09 standardised, from one line of preprocessing. Solutions E21 establishes the general
law - steps/condition is 5.57, 4.98, 4.55 across conditions of 7.9, 77 and 849 - so the payoff from
better conditioning is linear and predictable before training starts.

**The batch-size comparison was rebuilt twice.** By updates, full batch wins (+0.000000 against
mini-batch's +1.06). By epochs - the fair unit - the ranking reverses and mini-batch wins (+0.027 against
full batch's +21.05). Then solutions E11 showed *both* were confounded: holding the learning rate fixed
across batch sizes compares the pairing, not the size, and scaling the rate with the batch (the linear
scaling rule) puts batch 500 back at the optimum in 20 updates. The honest conclusion is that "which
batch size" is not a well-posed question.

**Momentum is given honestly.** On the well-conditioned problem the best beta is 0.30 at 28 steps against
58, and beta 0.9 costs 215 - nearly four times slower than none. On a ravine built by adding a near-copy
of `area` (condition 1,630) beta 0.95 gives 439 steps against 8,602. Momentum is worth roughly what the
conditioning is bad.

**The failure lab was redesigned after the first version's numbers did not exist.** A false "settled" is
unreachable with an absolute tolerance on this loss scale, but with a *relative* tolerance - the more
common formulation - a rate of 1e-7 reports `CONVERGED at step 2` at a loss of 159,888 against an optimum
of 285.88, which is 559 times too high. The gradient norm separates them instantly: 0.00049 against
799.4.

Solutions E10 found that the standard halve-on-increase schedule is useless here and explains why: on a
convex quadratic the loss never increases at a stable rate, so the trigger never fires; started above the
limit it halves to exactly 0.5 against a limit of 0.500017, parking itself in the slowest possible place.
A bold driver that also grows the rate reaches ~6,700 steps from any start, beating the best fixed rate
found by hand. E20's figure needed two panels because at 1.01x the limit the distance to the optimum
*falls* for 32 steps before turning around - a diverging run that looks like a converging one.

**2026-08-31 (5)** - Chapter 05-05 (residuals) and its solutions, 8 figures in the chapter and 5 in the
solutions. The chapter opens with **four models whose RMSE is 2.4000 to four decimal places** - the data
was calibrated by bisection to make them agree - of which one is honest and three are broken in
different ways. Everything else follows from that setup.

Each fault is caught by exactly one grouping and invisible in the others, which is shown as three tables
before any plot appears: curvature by mean residual per third of x (+1.16, -2.25, +0.87), fanning by
standard deviation per third (0.94, 2.08, 3.34), a group split by mean per group (-2.21, +2.30).

**The residual-vs-actual mistake gets a full treatment**, because it is the one beginners make. Two exact
identities are demonstrated: `corr(residual, fitted) = 0` for any least-squares fit with an intercept,
and `corr(residual, actual) = sqrt(1 - R²)`. The second means the wrong plot always slopes upward and
**slopes less for better models** - the diagnostic runs backwards. Solutions E9 makes it concrete across
R-squared 0.9910 (corr 0.0948) to 0.0676 (corr 0.9656), and E21 shows the flat reference is a property of
the *intercept*: fit through the origin and the correlation goes to -0.9782.

**The log-transform advice is given honestly rather than as a recipe.** On multiplicative synthetic data
the residual spread ratio falls from 3.33 to 1.06 on the log scale - and returns to **3.38** when the
predictions are exponentiated back, while price-scale RMSE gets *worse* (100.7 against 94.4) and picks up
a +31.8 bias in the middle third from the geometric-mean back-transformation. The transform fixed the
diagnostic, not the uncertainty.

**The histogram section was rewritten after executing it.** The draft said all four look bell-shaped;
the skew and kurtosis say otherwise. D has excess kurtosis **-1.60** and is visibly bimodal, C has
**+3.30** and long tails, and only B is genuinely missed (-0.36, as respectable as A's +0.09). So the
honest claim is that the histogram catches one fault, half-catches a second, and is blind to the third -
because it discards the pairing with the prediction, which is the information the fitted-value plot uses.

**Failure lab on real data: the California Housing ceiling.** 965 of 20,640 rows (4.68%) sit at exactly
5.00001 because the census top-coded house values at $500k, producing a hard diagonal line of slope -1
in any residual plot. MAE on those rows is **1.4937 against 0.4914** elsewhere - 3.04x worse - and the
point of the section is that the model is probably right and the *recording* is wrong. No test-set metric
could have shown it.

Solutions E20 constructs two datasets with RMSE 7.231024, MAE 6.201088 and R-squared 0.399016 identical
to six decimal places, one showing curvature and one showing bands, by projecting the residual vector off
the span of [1, x] and then bisecting a single noise parameter. It is the cleanest available proof that
metrics are a many-to-one map. E12 finds real spatial structure in the California residuals that the
per-feature sweep misses entirely: 18.1% of the residual variance is between cells of a 20x20 grid, and
49 populated cells have mean residuals from -1.129 to +0.706, while latitude and longitude taken one at a
time barely leave the band of +-0.1.

**2026-08-31 (4)** - Chapter 05-04 (metrics: MAE, MSE, RMSE, MAPE's trouble, R-squared) and its
solutions, 6 figures in the chapter and 4 more in the solutions. The chapter's spine is that **every
metric is a decision about which errors matter**, made visible three times.

The RMSE-to-MAE ratio is taught as a free diagnostic: 1.000 when every error is the same size, 3.000
when one row of nine carries everything, and 1.237 on the chapter's nine deliveries. E9 and E20 in the
solutions establish why the rule is portable - normally distributed errors converge to **sqrt(pi/2) =
1.2533** regardless of scale or sample size, while heavy-tailed errors average 1.4552. So "about 1.25,
fine; well above it, go and read the largest residuals" is a rule that transfers.

One bad prediction in nine makes MSE **37.71x** worse, RMSE 6.14x, MAE 3.40x and MAPE 2.61x - the same
event, four verdicts.

**A planned demonstration turned out to be wrong and was replaced.** The intent was "MAPE prefers the
model that predicts low", shown with a model 3 minutes low against one 3 minutes high. Those score
*identically* (11.0634% each). MAPE's asymmetry lives on the **ratio** scale - predicting 2x costs 100%,
predicting half costs 50% - so the chapter uses that framing instead. Solutions E11 keeps the failed
version deliberately, because a reader will construct it themselves: 10% high and 10% low give the same
MAE **and** the same MAPE, and only sMAPE separates them - preferring the high one, 9.52% against
10.53%, which is MAPE's bias reversed rather than fixed.

Solutions E10 supplies the missing evidence: the constant minimising MAPE on the nine actuals is
**25.00**, five minutes below the median of 30, because a miss on the 16-minute delivery counts 2.8x a
miss on the 45-minute one. Nobody asked the model to under-predict.

Negative R-squared is shown at **-1850.87** on fresh rows from a degree-18 polynomial on 25 points, read
as "the squared error is 1,851 times the mean's". Solutions E12 sweeps every degree: the crossing into
negative territory is at **degree 7**, and it is abrupt - degree 6 still scores +0.2008.

Two corrections found by executing rather than by reasoning. **The fitted-row R-squared is not monotonic**
(0.8459 at degree 11, 0.8048 at 18), which contradicts a claim made two cells earlier; the chapter now
names the cause, which is that raw powers up to 3^18 make the least-squares solve numerically unstable,
and forward-references 05-07. **Adjusted R-squared is not monotonic either** - it falls 0.50 to 0.18 as
noise columns are added, then rises to 0.27 at 21 features on 25 rows, where the denominator `n - p - 1`
is 3 and the correction becomes wild. Both are better teaching than the tidy version would have been.

Figures checked by eye. The MAPE asymmetry plot needed three passes: the "under-prediction can never
exceed 100%" note collided with the annotation on the 2.0x point, and moving either one put it on a
curve. Resolved by making the 100% line a legend entry instead of floating text.

**2026-08-31 (3)** - Chapter 05-03 (multiple regression and what a coefficient means) and its solutions,
6 figures. Built around a **sign flip** on 300 synthetic houses where the truth is known: price rises 3.0
per m2 and 0.9 per year of age, but older houses are smaller. Age fitted alone gives **-1.03**; age fitted
alongside size gives **+0.82**. Both correct, different questions, and the omitted-variable formula
predicts the flip in advance (0.9 + 3.0 x -0.6619 = -1.09 against a measured -1.03).

**Frisch-Waugh-Lovell is the centrepiece**, because it turns "holding the others constant" from a phrase
into a procedure: strip size out of age and out of price, fit a line to the leftovers, and its slope is
the coefficient to six decimals. Drawn as three panels, it is the clearest explanation of a regression
coefficient I know.

The collinearity experiment came out cleaner than designed. Coefficient spread grows 0.056 -> 1.263 as the
correlation goes 0 -> 0.999, while the **prediction spread is 0.0802 in all three, exactly**. That equality
is not luck: the second feature is always built from the same two underlying draws, so `span{first,
second}` is the same plane throughout and only the basis rotates. The residual vector is identical
(sd 1.0528) in every case. Collinearity rotates the coordinates without moving the space.

Real data: California's `AveRooms` and `AveBedrms` are 0.81 correlated, and moving from single-feature to
two-feature fits takes +0.0735 to +0.2901 and -0.1730 to -1.4405, with inflation factors of 6.01 and 5.25.

Three exercise findings. **E9**: twenty pure-noise columns move the coefficients by about 1% - irrelevant
columns are nearly harmless, in sharp contrast to correlated ones - but R-squared climbs from 0.766 to
0.851 at 100 noise columns, which sets up 05-07. **E20**: given `size` and `2 x size`, sklearn returns
(0.3848, 0.7697) with no warning; their combined effect is exactly the single-feature 1.9242 and the
predictions are bit-identical. The library picks the minimum-norm solution, so a coefficient can be
entirely an artefact of the solver.

**E11 was rewritten twice after executing.** I claimed the engineered ratio was "an interpretability fix,
not an accuracy fix" - it costs more than half the R-squared (0.1091 -> 0.0479), because a ratio is
nonlinear and does not span the same space. My replacement parenthetical was also wrong: `AveBedrms -
AveRooms` makes the inflation factor *worse* (62.14), not better. The corrected answer compares four
parameterisations and lands on orthogonalising, which gives a factor of exactly 1.00 at no cost in
R-squared - and returns `AveRooms` to +0.0735, its single-feature value.


**2026-08-31 (2)** - Chapter 05-02 (simple linear regression, fitted by hand) and its solutions, 7
figures. Nine deliveries chosen so every intermediate number is exact: x̄ = 5, ȳ = 30, Sxx = 60, Sxy = 210,
**slope 3.5, intercept 12.5**, residuals all halves summing to zero. The closed form matches
`LinearRegression` and `polyfit` to six decimals.

The figure I am most pleased with is the **covariance rectangles**: each delivery draws a rectangle from
its point to `(x̄, ȳ)`, its area is that row's `product` column, and its colour is the sign. All nine are
blue and they total exactly 210 - what a correlation of 0.99 looks like drawn out.

Identities made concrete rather than asserted: tilting the line by `d` costs `d² x Sxx` (60 here) and
shifting it by `s` costs `n x s²` (81), which are the two axes of the elliptical loss surface; **R-squared
is exactly the skill score under squared error** (0.977394 both ways); and `slope = correlation x
sd(y)/sd(x)`, so on standardised columns the slope *is* the correlation (0.988632).

Exercise results worth keeping. **E9**: changing one delivery from 45 to 95 minutes moves the
least-squares slope from 3.500 to **6.833** and the absolute-error slope **not at all** - stronger than
05-01's mean-versus-median contrast, because the corrupted point never crosses the line. **E10**:
regressing the other way gives a different line, and the product of the two fitted slopes is exactly `r²`
(0.977394). **E15**: a reported slope of 0.29 where 3.5 was expected is diagnosed from the number alone -
`1/3.5 = 0.2857`, the signature of swapped axes.

Two things executing changed. **E12**: I claimed a wrong-intercept line still satisfies the tilt condition;
it does not. The corrected table shows that *any* line through `(x̄, ȳ)` satisfies `sum(residual) = 0` -
so that condition is not evidence of a good fit at all - while only the fitted line also satisfies
`sum(residual x x) = 0`. **E11**: the leave-one-out table has two deliveries with exactly zero influence,
for different reasons - one sits at `x̄` so its weight is zero, the other lies exactly on the line so its
residual is. Influence needs both, which is a better definition than the one I had written.


**2026-08-31 (1)** - Chapter 05-01 (the best constant) and its solutions, opening module 05. Seven
figures on fifteen delivery times, small enough to print and check by hand.

The chapter's thesis: **a metric is not a way of scoring a model, it is a specification of what to
predict.** Four metrics on one dataset give four different best constants - **31.0 (MAPE), 34.0
(absolute error, the median), 36.4 (squared error, the mean), 52.0 (pinball at q=0.9)** - spread over 21
minutes on data whose middle is 34. The baseline module 05 now has to beat is stated precisely: **8.00
minutes of MAE, or 99.17 of MSE.**

Derivations rather than assertions: absolute error is piecewise linear with a kink at every observation
and slope "points below minus points above", so it turns at the median; squared error is a parabola whose
minimum is where the average residual is zero, so it sits at the mean. One stuck driver at 195 minutes
moves the mean 9.91 and the median 1.00. Pinball loss generalises both, and its minimiser is verified to
be the `ceil(q*n)`-th smallest value on all five quantiles.

Two exercise results argue against the chapter's own surface reading. **E9**: as the outlier grows through
60, 100, 200, 500, 1000, the mean's movement is exactly linear while **the median moves 1.00 every time** -
robustness is not a tendency, it is a bound. **E12**: over 1,000 samples the median's sampling spread
(3.3831) is *larger* than the mean's (2.9399). Robustness and efficiency are different properties, and the
median trades the second for the first - so the reason to use it is that it is optimal for absolute error,
not a vague belief that it is safer.

E20 was rewritten after executing: I claimed the ceiling rule held in every case and the test said 95%.
All nine disagreements have `q*n` an exact integer, and in every one the rule's value is still optimal -
the minimiser is simply not unique there. The exercise now tests optimality rather than point equality,
and reports 180/180 optimal, 171/180 identical.


**2026-08-30 (40)** - Module 04 assessment and its solutions. 40 marks over recall, doing and judgement,
on 2,041 synthetic support tickets from 300 customers over 18 months. Built so that the workflow's lessons
are *measurable* rather than merely recalled: 293 of the 300 customers appear more than once (so grouping
is a live question), 15.97% of `description_length` is missing, and `customer_lifetime_tickets` is a
whole-history aggregate that cannot be known at prediction time.

The eight Part B tasks cover all eight chapters and mark themselves against salted digests; the checker was
tested to accept every correct value and to reject B4's answer offered for B3.

The leak is the centrepiece. Adding `customer_lifetime_tickets` improves MAE from 3.5837 to **3.0185**, and
- the stronger evidence - **that column alone scores 3.2158, beating all five legitimate features together
(3.5837)**. A one-feature model should not beat a five-feature one unless the one feature has seen the
answer.

C1 hands the learner a histogram of thirty random splits and a colleague's "MAE 3.34", which turns out to
be **the best of the thirty, 2.92 standard deviations below the mean of 3.6062**. C3 makes the point the
module has been building to twice over: the grouped estimate (3.5954) is the honest one for a deployment
that serves unseen customers, *and* it differs from the random-split estimate by only 0.01 - about a ninth
of the split-to-split spread. On 04-04's gym data the same comparison was worth +0.0957 and reversed a
model ranking. The size of the effect is a property of the data, and measuring it is the only way to know.

**Module 04 is closed**: eight chapters, 51 figures, an assessment, and every chapter validated from a
fresh kernel.

**2026-08-30 (39)** - Chapter 04-08 (reproducibility) and its solutions, 6 figures, finishing module 04.

Frames reproducibility as five levels - seeds, code, data, environment, hardware - and measures which of
them actually moves a number. **The split seed produces 5.2 times the spread of the model seed** (sd
0.0487 against 0.0094), and varying both is indistinguishable from varying the split alone. The chapter's
sharpest point falls out of that: `random_state=0` happens to be a hard split here and reports 1.0032
where the average split gives 0.8809 - **14% pessimistic, permanently, by accident**. A seed makes a
number stable; it does not make it representative, and those are different problems.

Below the seed: floating-point addition is not associative, and the same 100,000 values summed in two
orders differ by one part in 10^15. Put on one log axis with the seed effects, the sources span thirteen
orders of magnitude - and the library-version bar has no measurable size at all, which is why it is the
one that actually breaks a result a year later.

The experiment record pulls the whole module together: every field in it (baseline, spread, split rule,
settings, environment, and *why*) was argued for by an earlier chapter.

Exercise results. **E9 is the chapter's real conclusion**: ridge has no randomness of its own, so its
model-seed spread is zero to 2e-16 - and its split-seed spread is 0.0513, essentially the forest's 0.0487.
A deterministic model does not give a deterministic result; it gives a deterministic result *per split*.
**E12**: the same forest with the same `random_state` but different `n_jobs` gives predictions differing
by about 1e-15, because the order in which 200 tree predictions are averaged changes with the thread
split. **E20** builds a regression test for a *result* - recorded, matched, and caught when tampered with -
which almost no project has and most want.

Fixed after executing: the no-seed demonstration prints different values on every run by construction, so
the prose that quoted them was rewritten to quote none; and a `\n` inside a non-raw patch string became a
real newline and broke a figure's string literal.

**Module 04 is complete** - eight chapters, 51 figures, every one of them about something that happens
before or around the model rather than inside it.

**2026-08-30 (38)** - Chapter 04-07 (pipelines and cross-validation) and its solutions, 6 figures. First
chapter in module 04 on a real dataset: California housing, with a `region` column derived from latitude
and holes punched into `MedInc` and `HouseAge` so the pipeline has genuine work to do.

The chapter's centre turned out to be a correction to my own draft. I had written that `best_score_` is
optimistic by 0.024 "because it is the maximum of fourteen noisy numbers" - 04-03's selection premium
arriving on schedule. Executing the decomposition showed that is **wrong**: nested cross-validation
returns *exactly* what plain 5-fold cross-validation of the chosen settings returns (**premium
+0.0000**), and the entire 0.024 is the inner loop being 4-fold, so training on 3/4 of the rows instead of
4/5. The four-row table A/B/C/D that separates them is now the heart of the chapter, and it is the third
time in module 04 that a comparison changed two things at once - after 04-04's stricter-but-smaller split
and 04-06's row-dropping.

E20 confirms it at scale: with the fold counts matched, the premium is **+0.0000 at 2, 6, 14 and 30
candidates and +0.0001 at 60**, against 04-03's 0.12 from forty. The reconciliation is that the premium
counts *effectively independent* candidates - sixty ridge alphas trace one smooth curve with one minimum,
while 04-03's forty random four-column subsets were genuinely different and mostly worthless.

Other measured results: the manual workflow's optimism against a pipeline is +0.0181 on 400 rows and
+0.0109 on 4,000, against 0.25 on pure noise in 04-05 - same code, different data. Nesting costs about
five times the compute. **E9 contradicts 04-06 and is right to**: logging this target helps by 16%
(0.5585 against 0.6615) where logging the rents hurt, because California house values really are
multiplicative and the synthetic rents were built additively - and skew alone cannot tell you which you
have. E12: the random forest has the largest train-test gap (0.222) and is not the worst model; ridge has
the smallest (0.105) and is by far the worst, because a small gap can mean "underfits equally badly on
both".

**2026-08-30 (37)** - Chapter 04-06 (preprocessing) and its solutions, 8 figures. New dataset: 1,200
synthetic rental listings with twelve administrative district codes, 13% of `area_m2` missing at random
and 13% of `age_years` missing **because the building is old** - so one column's missingness is
informative and the other's is not, by construction.

Four decisions, each measured. **Imputation:** the age gap is 32.8 EUR at 2.38 standard errors, area's is
13.5 at 1.11, and the missing indicator earns 0.61 EUR for age and nothing for area - exactly as the test
predicts. **Encoding:** an arbitrary ordinal order recovers **9.5%** of what the district column is worth
(75.92 against one-hot's 58.50 and 77.75 for dropping it). **Scaling:** kNN pays 15.65 EUR unscaled;
ridge and the random forest pay -0.01. **Transforms:** logging the target costs 0.75 EUR and
under-predicts the mean by 5.6, because exp of a mean of logs is a geometric mean; Duan's smearing
correction (1.0248) repairs the level and slightly worsens the MAE.

The trap the chapter is built around: dropping incomplete rows scores **51.41** against 58.50 for
imputing, which looks decisive until you notice it is measured on different rows. On the same 915
complete rows both score 51.41 - identical, because there is nothing left to impute. The discarded rows
rent for 336 against 365, so dropping them made the *question* easier. Same shape as 04-04's E10.

Two exercise answers push back on the chapter's own moral. **E9:** `KNNImputer` beats the mean by 3.39
EUR - five times what the indicator was worth - because `area_m2` is MAR and well predicted by rooms and
district, so "the mean is usually fine" is wrong here and the honest advice is to measure. **E10:**
ordering the ordinal code by training-fold mean rent recovers **94%** of one-hot's value in a single
column, so the chapter's 9.5% is a fact about alphabetical codes, not about ordinal encoding - and what
E10 re-invents is target encoding, which is why it must be fitted inside the fold.

Fixed after executing: E8's informativeness threshold was a quarter of the target's standard deviation,
which flagged neither column - replaced with 03-03's standard error of a difference, which flags age and
clears area. E11's two pipelines were not like for like (one had an indicator), inflating a difference the
prose called negligible; corrected to 58.50 against 58.54. Six figure titles had a doubled backslash and
rendered a literal `\n`.

**2026-08-30 (36)** - Visual pass over module 04, after a second request for more visual learning
(D-17: six to ten figures per chapter, and a figure per *idea* rather than per chapter). 04-01 went from 3
figures to 6, 04-02 from 2 to 5, 04-03 from 4 to 6, and 04-05 from 5 to 7. Seven new figures in total, all
checked by eye and three of them redrawn after looking: a target-encoding schematic that had picked an
all-zero category so its average was uninformative, a one-rule chart whose point labels collided with its
legend, and a baselines ladder whose reference label sat on top of a bar.

The additions worth naming, because they show what "a figure per idea" buys: the **framing funnel** (600
members to 521 eligible to 70 positive - framing as row selection); **paired histograms** of the leaky and
the honest feature, where the leak's perfect separation at month 18.5 is visible rather than asserted;
**predicted-versus-actual panels** in which the forest visibly spreads without moving closer to the
diagonal; the **correlation histogram** of 5,000 noise columns with the selector's tail highlighted,
against E5's predicted maximum of 0.255 (measured: 0.3049); **error bars that shrink while the dot stays
still** for the test-size trade-off; and two closing summary cards - the filled-in eight-line prediction
contract, and every predictor in 04-02 on one axis with the free bar drawn across it.

**2026-08-30 (35)** - Chapter 04-05 (the leakage lab) and its solutions. Puts all four kinds on one
scale and ranks them, and the ranking contradicts the folklore.

**Fitting a scaler and a mean-imputer on the whole dataset costs +0.0005** - measured over 30 datasets,
standard deviation 0.0048, and the leaky version wins in only 37% of them. It is not a small effect, it is
undetectable. **Feature selection fitted on the whole dataset gives 79.5% accuracy at predicting a coin
flip** from 5,000 columns of pure noise, five-fold cross-validated with folds agreeing to within 0.05.
Target-encoding a 149-category column on a coin-flip target gives AUC 0.7659.

That gives the chapter a principle instead of a list: **severity is proportional to how much the fitted
step learned about `y`.** A scaler learns two numbers per column and never sees the target; a selector
learns which columns correlate with it. The full ranking spans a factor of 700, from 0.0005 to 0.3641.

Nine figures including three schematics: the four-kind taxonomy, the inflation-versus-search-width curve,
the ranked bar chart of every leak in module 04, and the three-symptom checklist.

Exercise findings worth keeping. E9: keeping **more** pre-selected noise columns makes it worse, not
better - 96.5% accuracy on a coin flip with k=100, because a hundred weak illegitimate associations stack.
E10: smoothing a target encoding does **not** fix it (0.7659 to 0.7503 at heavy smoothing) - smoothing
addresses variance, and the leak is about whose labels went in. E11: dissection shows only the *selector*
matters - moving the imputer and scaler outside changes 0.5550 to 0.5600, moving the selector out gives
0.8150.

E12 was rewritten after executing it. I had claimed drop-one-feature would identify `months_on_file`; it
ranks the innocent `tenure_months` first (0.0492 against 0.0252), because drop-one is confounded by
redundancy - `visits_lifetime` can stand in for `months_on_file`, so dropping it costs little, while
`tenure_months` is the only decoder for the pair. The "score from it alone" column fingers the culprits
correctly at 0.9323 and 0.9153. The two diagnostics answer different questions and only the second is the
leakage one.

**2026-08-30 (34)** - Chapter 04-04 (grouped and chronological splitting) and its solutions, built to
the new D-17 visual standard: **nine figures**, including three pure schematics that carry no data.

Uses 04-01's E18 member-month table (6,318 rows, 580 members, 10.9 rows each). Under a random 70/30 split
**539 of 544 test members - 99.1% - are also in training**. What that costs depends entirely on the model:
logistic regression **+0.0021**, random forest **+0.0957**, k-nearest-neighbours **+0.1052**, because
inflation scales with capacity to memorise.

The finding worth the chapter: **the ranking reverses.** The random split says the forest is best (0.7580
against 0.7313); the honest split says the logistic regression is (0.7292 against 0.6624). A leaky split
does not merely inflate - it systematically favours the models that leak best, so it changes what you
ship.

Four-stage ladder measured for both models: random rows / grouped only / chronological only / grouped AND
forward. The forest loses most at the grouping step, the logistic regression at the chronological step,
and the crossing survives every stage.

Figures: the block schematic of a random versus grouped split (the picture the whole chapter rests on),
the composition of the "held-out" set, the inflation bars, the crossing-lines slope chart, three real
per-month split profiles, the forward-chaining staircase, and a 2x2 decision grid.

Exercise answers that qualify the headline. E9: inflation grows with tree depth to +0.0835 at 238 leaves
and then **falls** to +0.0607 at 842, because an unlimited tree's leaky score has itself collapsed - so
inflation scales with capacity only over the range where the model still works. E10: of the 0.1134 total
drop, **0.0248 is less training data and 0.0886 is leakage** - four fifths real. E12: with one row per
member the inflation vanishes (-0.0272), the control the chapter needed, and the base rate jumps 0.1198 to
0.2155 because per-member sampling weights members equally - 04-01's unit-of-observation lesson arriving
uninvited. E20 finds a fourth leak neither grouping nor chronology removes: **target overlap**, worth
0.0368 once the training-size effect (0.0514) is separated out.

**2026-08-30 (33)** - Chapter 04-03 (splitting: train, validation, test) and its solutions. Audits the
two previous chapters: the same logistic regression over **200 random splits** scores anywhere from
**0.6080 to 0.8185** (sd 0.0425), and the AUC 0.6359 that 04-01 and 04-02 both reported sits at the **3rd
percentile**. Nothing in those chapters was wrong - every gap they argued about was larger than this noise
- but the four-decimal single-split number is now properly framed as one draw.

Four demonstrations, each with its own figure: the scissors (unlimited tree depth reaches MAE 0.3453 on
its own rows and 3.4772 on unseen ones, best depth 3); the split lottery histogram; stratification
(held-out base rate exactly 13.38% every time against a plain range of 7.01% to 22.29%, or 11 to 35
cancellers); and the selection premium - best of 40 candidates scores 0.7532 on the set that chose it and
0.6366 on the set that did not.

The premium curve was rebuilt after executing it. A single realisation was non-monotone and unusable, so
it now averages 200 draws at each size: the reported score climbs 0.7121 to 0.7422 from ten to eighty
candidates while the delivered score goes 0.6342 to 0.6223. Past about ten candidates the search buys no
real performance at all.

Three exercise answers push back on the tidy lesson. E9: stratification does **not** narrow the AUC spread
here - sd 0.0425 either way - because it fixes the base rate and not which members are held out, so its
justification is comparability rather than variance. E8: the model and 04-02's one-rule threshold are
indistinguishable even paired (+0.0074, sd 0.0339, logistic wins 58% of splits). E20 was rewritten
entirely: I predicted a log-shaped premium curve and it saturates instead, and the k=1 point is a 0.0281
offset that is not selection at all but the test set being harder than the validation set - the honest
decomposition is a constant handicap plus a selection term that arrives early and stays.

**2026-08-30 (32)** - Chapter 04-02 (baselines) and its solutions. Predicts next month's visits on the
same gym panel, split chronologically at month 16. The result the chapter is built on: **both models lose
to a one-line baseline.** Per-member running mean MAE **2.3640**; linear regression 2.3992 (-1.49%);
random forest with 200 trees 2.4353 (-3.02%), and -1.95% and -7.10% on squared error too, so it is not a
metric artefact. Eight hundred trees reaches 2.4338 and never arrives, so it is not capacity either. The
mechanism is that fitted coefficients carry sampling noise and a rule with no parameters cannot.

Second surprise, and a good one: **persistence (3.0482) is worse than a constant (2.9688)**, because each
month's visits are a noisy count and one draw is a worse estimate of a member's rate than twelve - 03-02's
square-root law turning up where nobody expects it. E9 confirms the same effect from the other side: a
three-month window scores 2.5444 and longer windows keep improving to the full history.

The same forest shows **+17.97%** skill against the global median, which is the chapter's central warning
about choosing which baseline to quote.

Three exercise answers contradict the obvious prediction and are worth keeping. E11: the per-member
*median* loses to the mean (2.4024 vs 2.3640) even though the metric is absolute error, because 03-01 is
about summarising data you have, not predicting a future draw. E10: removing columns helps the linear
model and hurts the forest, so neither "more features" nor "fewer features" is a rule. E20: the learning
curve flattens above the baseline rather than towards it, and the 100% point moved by 0.0065 from row
order alone - a useful calibration for how much of the fourth decimal to believe.

**2026-08-30 (31)** - Chapter 04-01 (framing) and its solutions, opening module 04. Turns "predict who
will churn" into a five-question contract on 9,059 member-months of a synthetic gym panel. The unit of
observation alone gives **33.00%, 2.19% and 1.51%** for the phrase "churn rate", and the horizon moves the
base rate from **1.73% to 22.84%** with everything else held fixed. Central visual is the wall diagram -
nine members' timelines with the feature window, the prediction point and the outcome window shaded -
which is the picture the rest of the module refers back to.

The failure lab came out stronger than planned. Two whole-history columns take AUC from 0.636 to **1.000**,
but neither does it alone: `months_on_file` manages 0.954, and it is the *harmless* `tenure_months`
(correlation +0.0367 with the target) that completes the leak, because `months_on_file + 12 -
tenure_months` reconstructs the exact cancellation month, and cancellers end in months 13-18 while
survivors end in 19-24 with no overlap. So leakage is a property of the feature set, not of individual
columns - which also gives E11's per-column detector an honest limitation to state.

Second finding worth keeping: the honest model's accuracy (0.847) is **below** the constant baseline
(0.866) while its AUC shows real signal, which sets up 04-02 directly. E10 was rewritten after executing:
a single 70/30 split shows AUC falling from 0.845 at a two-month horizon to 0.636 at six, a clean story
that is entirely noise - cross-validated, every horizon sits between 0.698 and 0.733, and the fold-to-fold
sd at two months is 0.149.

**2026-08-30 (30)** - Module 03 assessment and its solutions. 40 marks over recall, doing and
judgement, on 400 synthetic parcel deliveries from a two-depot courier network. The eight Part B tasks
cover all eight chapters and mark themselves against salted digests, so no answer is readable in the
notebook source; the checker was tested to accept the correct value, accept it 0.01 out, and reject the
two plausible wrong answers for the Bayes task (85, the sensitivity, and 6, the base rate). Part C1 hands
the learner four loss curves and asks which is which - the first assessment question in the course that
is read off a picture. C3 turned out better than designed: the two-feature model scores 33.77 against a
supposed noise floor of 36.0, because the 400 noise values actually drawn have a variance of 34.05, and
adding `weight_kg` - which by construction cannot matter - lowers the training error again to 33.766.
That is held-out data argued for in three numbers, and it sets up module 04.

**2026-08-30 (29)** - Chapter 03-08 (loss, gradients, and how a model is fitted) and its solutions
built and validated, finishing module 03 and the mathematics. Gradient descent in five lines recovers
`np.polyfit`'s answer to four decimals. Two failure labs: the learning rate (0.001 sits at 24,582 against
a best of 431.78; 1.01 climbs to 9.09e+11) and unscaled features (**115 steps standardised against 21,769
raw**, condition number 5,482 against 1). New in this chapter, following the request for more visuals and
more arithmetic: a tangent-line plot, five snapshots of the line swinging into place, contour maps of the
loss with the descent path drawn on them (circles against stripes), and a three-panel picture of a step
that is too small, right, and too large. The derivative table shows the second difference is a constant
849.61, so one division lands on the bottom exactly - Newton's method, introduced and then rejected on the
8-terabyte curvature matrix a million-parameter model would need. Distance to the optimum was measured
shrinking by exactly `1 - 2 x learning_rate` per step. Exercises expanded to 28, most of them hand
arithmetic. Two things executing changed: the divergence verdict was misreporting 9.09e+11 as "still
descending" because it was finite, and **E23's premise was wrong** - I claimed a too-large rate makes the
loss curve oscillate where a sign error makes it monotone, and the two curves turn out to be *identical to
every decimal place*, so the answer was rewritten around the parameter trajectory, which does separate
them.

**2026-08-30 (28)** - Chapter 03-07 (vectors, distance, and shapes) and its solutions. Five flats,
three columns, and a failure lab that changes how the rest of the course treats data: asked for the
nearest match to 1210 euros / 4 rooms / 5 km, raw Euclidean distance returns flat A, which has two
rooms and sits 1 km out, while flat B - an exact match on both non-price requirements, 40 euros
dearer - comes third. The contribution table shows why: rent supplies between 83.3% and 99.997% of
every squared distance, because a 40-euro gap contributes 1,600 and a two-room gap contributes 4.
Standardising flips the answer to B at 0.1097. Norms next, with a case where L1 and L2 disagree - out
by 3.0 on one feature against 1.8 on two gives L1 3.000 vs 3.600 and L2 3.000 vs 2.546 - which is
03-01's squared-versus-absolute fork appearing a third time, and which is also Ridge against Lasso.
The dot product is then introduced as a weighted sum and immediately as a prediction, with flat A
checked by hand at 76.0, so module 05's prediction step is already familiar. Cosine similarity
contrasted with distance on a listener who has identical taste and ten times the activity: euclidean
20.125 and cosine 1.0000. Closes on shapes, the matmul contract, and reading a real ValueError.
Solutions E8 is the sharpest version of the chapter's point - dividing rent by 1000, with no
standardisation anywhere, flips the nearest flat from A to B, so unscaled distance is not a weak
measure of similarity but a statement about spreadsheet units. E10 predicts and confirms that income
supplies 99.94% of the distance in an unscaled kNN. E16 measures the curse of dimensionality: the
ratio of furthest to nearest neighbour falls from 73.9 at two dimensions to 1.268 at two hundred.

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
