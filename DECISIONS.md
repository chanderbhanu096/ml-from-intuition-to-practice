# Decisions

Every non-obvious choice in this course, with the reason. Newest first inside each section.

## Environment

**D-01 - Python 3.11 in a local `.venv`.** (2026-08-29)
3.13/3.14 are ahead of some scientific wheels; 3.11 has the widest support for
scikit-learn, PyTorch and statsmodels. A venv keeps the course from colliding with the
learner's other projects. Verified working: numpy 2.2.6, pandas 3.0.5, scikit-learn 1.9.0,
matplotlib 3.11.1.

**D-02 - Minimal dependency set.** (2026-08-29)
numpy, pandas, matplotlib, scikit-learn, jupyter. Nothing else until a module genuinely
needs it (statsmodels in module 09, PyTorch in module 10). Reason: every extra library is
another install failure between a beginner and their first result, and library calls are
not understanding.

**D-03 - No seaborn.** (2026-08-29)
matplotlib only. Seaborn hides the plotting mechanics behind one-liners; early on the
learner should see that a chart is data plus axes plus labels. Where seaborn would be
genuinely shorter (pair plots), the notebook writes the loop explicitly - it is five lines.

**D-04 - HistGradientBoosting instead of XGBoost/LightGBM.** (2026-08-29)
scikit-learn ships a fast, competitive boosting implementation. It removes an install step
and keeps one consistent API across the whole course. The vocabulary transfers; module 05
names the differences so the learner is not surprised in an interview.

**D-05 - PyTorch for module 10, CPU only.** (2026-08-29)
Chosen over Keras/TensorFlow because its explicit training loop *is* the teaching content:
forward pass, loss, `backward()`, optimiser step, each visible on its own line. Core
notebooks stay small enough to train on a laptop CPU; anything needing a GPU is marked
optional.

## Datasets

**D-06 - Seoul bike sharing is the recurring case study, but is not required to start.**
(2026-08-29) The dataset is not present in this repository. Modules 00-01 use tiny
hand-written tables; module 02 onwards uses it if it has been downloaded, and falls back to
clearly-labelled synthetic data otherwise. See `data/README.md`. No column name, statistic
or result from that dataset is asserted anywhere in this repo until a real file has been
loaded and inspected.

**D-07 - Seoul bike is used for regression, EDA, feature engineering, splitting, leakage,
error analysis and forecasting only.** (2026-08-29) It is not forced into classification
or clustering chapters; inventing a fake binary target there would teach a bad habit
(manufacturing a problem to fit a method). Classification uses its own datasets.

## Curriculum

**D-08 - Phase 0 compressed from four notebooks into three.** (2026-08-29)
"How to use Jupyter" is folded into chapter 00-01 rather than standing alone: a learner
reading a notebook is already using Jupyter, and a whole chapter on cell execution delays
the first real idea. In exchange, 00-01 also teaches one genuine concept (a prediction is a
rule from known inputs to an unknown output) so orientation is not a content-free chapter.

**D-09 - The learner diagnostic lives in 00-01, the Python diagnostic in 01-01.**
(2026-08-29) Two different questions - "how much ML do you know" and "is your Python good
enough" - asked at the two different moments they matter, so module 01 can be skipped
honestly instead of guessed at.

**D-10 - Maths is spread across the course, not front-loaded.** (2026-08-29)
Module 03 exists, but each of its ideas is also re-introduced immediately before the model
that needs it (distances before kNN, gradients before gradient descent, likelihood before
logistic regression). A single maths block early is the most reliable way to lose a near
beginner.

**D-14 - Each chapter picks the dataset that teaches its idea most clearly.** (2026-08-30)
Supersedes the "Seoul bike as the recurring case study" plan in D-06 and D-07. The owner's
instruction: use whatever dataset helps understand that particular algorithm. This is a real
pedagogical gain rather than a relaxation - a single recurring dataset forces every method through
one lens, and several methods only show their character on data with the right shape: class
imbalance for 06-08, heavy tails for 05-09, genuinely separated clusters for 08-03, a real seasonal
cycle for 09-02, text for 11-01. Chapters now choose freely from small built-in datasets,
clearly-labelled synthetic data with a known truth, and named public datasets. Seoul bike remains
available and is no longer required, so no chapter is blocked on a download. The rule that survives
unchanged: **no dataset is used until its source, licence, unit of observation and known limitations
are recorded** in `data/README.md`, and synthetic data is always labelled SYNTHETIC.

**D-13 - Orientation's third chapter split into 00-03 and 00-04.** (2026-08-29)
The plan put kinds of learning, prediction-vs-explanation-vs-cause, and the lifecycle in one
chapter. Written out that is roughly 90 minutes with two unrelated centres of gravity, and the
causality half needs a failure lab of its own - it is the most expensive confusion in applied
ML. Split into 00-03 (the families of learning plus the lifecycle map) and 00-04 (prediction,
explanation, cause). Module 00 is now 4 chapters; the course is 121.

**D-16 - Every chapter carries a picture of the mechanism and a page of arithmetic.** (2026-08-30)
From 03-08 onwards a chapter is not finished until it contains, in addition to whatever plots the data
needs: at least one figure that draws the *mechanism* rather than the data - a loss surface with the
optimiser's path on it, a decision boundary moving, a tree's splits carving the plane - and at least one
table of numbers whose pattern the reader is asked to spot before it is explained. Exercise sets lead with
hand calculation on three or four rows, small enough to do on paper and check in one cell.

Why. The two things a beginner most often lacks are a mental image of what the algorithm is doing and the
confidence that the arithmetic is arithmetic. A scatter plot of the data supplies neither. 03-08's contour
maps make "badly conditioned" a picture of stripes rather than a definition, and its derivative table makes
the second difference a constant the reader notices themselves - after which Newton's method needs no
motivation. The cost is roughly a third more content per chapter and a slower build; the chapters already
written are not being retrofitted, because the budget is better spent on the 95 not yet built.

Consequence: the figures are checked by eye during authoring, not only executed. A plot that runs without
error can still be unreadable - 03-08's first valley contour was drawn on a window where the valley was
invisible, and its first learning-rate panel had a y-limit that flattened the bowl to a line. Both passed
execution and both were useless.

**D-15 - Notebooks are committed without stored outputs.** (2026-08-30)
Every `.ipynb` here is committed with empty `outputs` and null `execution_count`. Notebooks are
executed to verify them; the execution artefacts are not kept. Three reasons. The learner should run
the notebook themselves, and one that arrives pre-filled with answers invites reading instead of
running - the opposite of what "predict before running" is for. Stored outputs embed matplotlib
figures as base64 PNGs: 02-07 and 02-08 were briefly committed with outputs at 328 KB and 288 KB
against roughly 29 KB for comparable chapters without, a tenfold cost for content regenerated in two
seconds. And diffs stay readable, since a one-word prose fix should not show as a hundred changed
lines of image data. Consequence: `scripts/validate_notebooks.py` executes in memory and
deliberately does not write back, so when a notebook is executed with `nbconvert --execute --inplace`
during authoring - the convenient way to check prose against real output - **the outputs must be
stripped before committing**. This was missed for five chapters and corrected on 2026-08-30.

**D-11 - Notebook file naming `MM-CC_slug.ipynb`.** (2026-08-29)
Module and chapter numbers in the filename, so learning order is sort order and a file is
still identifiable when it is opened alone or moved.

**D-12 - No repository licence chosen.** (2026-08-29)
Licensing is the owner's decision, not this course's. `data/README.md` records the licence
of each *dataset*, which is a different question.
