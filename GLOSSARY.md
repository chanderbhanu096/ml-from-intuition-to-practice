# Glossary

Plain-language definitions of terms **already introduced by a completed chapter**. If a term is
not here yet, the course has not taught it yet - that is deliberate, not an omission.

Each entry says where it was introduced and, where it matters, where it gets deeper.

---

### Absolute error
The size of a mistake with the minus sign dropped: `|actual - predicted|`. Used so that being 10
too high and 10 too low both count as 10, instead of cancelling out. *(00-01)*

### Accuracy
The share of predictions that are correct. Dimensionless. Crude: it hides which rows are wrong
and treats all mistakes as equal, and on imbalanced data a useless model can score very high.
*(00-02; dismantled in 06-04 and 06-05)*

### Active learning
Instead of labelling examples at random, letting the model choose which ones would teach it the
most. Usually a better use of a small labelling budget than pseudo-labelling. *(00-03; 12-01)*

### Anomaly detection
Finding rows that do not resemble the rest. Note that *unusual* and *bad* are different concepts;
conflating them is a common framing error. *(00-03; 08-08)*

### Baseline
A deliberately trivial rule that your model has to beat before it is worth anything - "always
predict the average", "always predict the majority class". A baseline turns a score into a
judgement, and catches bugs. *(00-01; formalised in 04-02)*

### A/B test (randomised experiment)
Assigning the treatment by chance, so the treated and untreated groups are alike in everything -
including variables you never measured. Establishes an effect for that population, at that time,
at that dose. *(00-04; 12-07)*

### Broadcasting
NumPy stretching a smaller array to fit a larger one so they can be combined. Shapes are aligned
from the right; dimensions must match or be 1. It succeeding is a fact about shapes, not about
meaning - if an array is unexpectedly large, suspect a broadcast. *(01-03)*

### Batch inference / online inference
Whether predictions are produced in bulk on a schedule, or one at a time on request. A separate
decision from batch versus online *learning*. *(00-03; 13-07)*

### Batch learning / online learning
Whether the rule is refitted periodically on a dataset (batch) or updated continuously as each
observation arrives (online). Batch is the right default: far easier to test, reproduce and roll
back. *(00-03; 12-02, 13-07)*

### Classification
Supervised learning where the target is a category from a fixed list. Errors are counted, and
different mistakes usually cost different amounts. *(00-03; module 06)*

### Causation
The question "what happens to Y if I **set** X?" - as opposed to what is merely associated with
Y. A fitted model does not answer it; an intervention or an explicitly stated assumption is
required. *(00-04; 12-07)*

### Chained indexing
Selecting twice in a row (`df[mask]["col"] = x`) rather than once (`df.loc[mask, "col"] = x`).
Under pandas copy-on-write the assignment modifies a temporary copy and is silently discarded.
*(01-04)*

### Cluster stability
Whether the same rows stay grouped together when you re-cluster a random subset of the data.
One of the few genuine checks available for a clustering, because there is no held-out score.
*(00-03 solutions; 08-06)*

### Clustering
Unsupervised grouping of similar rows. The number of groups is something you choose, not
something the algorithm discovers - so clusters are a partition you requested, not a fact about
the world. *(00-03; module 08)*

### Confounder
A variable that influences both who receives the treatment and the outcome, so a plain
comparison of treated with untreated mixes the two effects. Both arrows are required - a
variable correlated with the outcome alone is just a useful feature. *(00-04)*

### Confusion matrix
The four counts behind a yes/no prediction: correctly predicted positives, false alarms, missed
positives, correctly predicted negatives. Every classification metric is built from these.
*(previewed in 00-02 solutions; 06-04)*

### Data contract
A machine-checked statement of what a data file must look like - columns, dtypes, ranges, row
counts - enforced at the point of loading rather than discovered downstream. *(01-04 solutions;
13-05)*

### dtype
The type of a column or array. A numeric column containing one unparseable value becomes text for
its whole length, after which `max()` compares alphabetically and `sum()` concatenates - both
silently. Check `.info()` after every load. *(01-03, 01-04)*

### Dimensionality reduction
Replacing many columns with fewer that carry most of the information. *(00-03; 08-07)*

### Drift
The world moving away from the data a model was fitted to, so a once-correct model quietly stops
being correct. Nothing announces it - detecting it is a separate job. *(00-02; 12-02, 13-08)*

### Duplicate leakage
Copies of the same observation appearing in both the training and test sets, so the model
recognises rows it has already seen and scores far better than it will in production. Most often
created by a join whose right-hand key was not unique. *(01-05; 04-05)*

### Feature
A piece of information used as input to a prediction, which you will genuinely have at the moment
you make the prediction. A column is only a feature if that second half is true. Also called a
predictor, or `X`. *(00-01)*

### Held-out set
Rows deliberately hidden while a rule is built, used only to score it afterwards. Scoring on rows
the rule was built from measures memory, not skill. Also called a test set. *(00-01; done
properly in 04-03)*

### Join (merge)
Combining two tables on a key. Four kinds: left, inner, outer, right. The only question that
matters is how many rows come out - a left join preserves the row count *only if the right key is
unique*. Check the count before and after, and pass `validate=`. *(01-05)*

### k-means
A clustering method that partitions rows into a number of groups **you specify**, by repeatedly
assigning each row to the nearest group centre. Sensitive to feature scaling and to the number
you chose. *(00-03; 08-03)*

### Leakage
Using information when building or scoring a model that would not really be available at
prediction time - typically something from the future, or the answer itself under another name.
Makes a useless model look excellent. *(previewed in 00-01; the subject of 04-05)*

### Lever (versus predictor)
A variable you could actually change. A feature can be an excellent predictor and a useless
lever: `emailed` predicts spend because it carries information about loyalty, and emailing
everyone destroys exactly that information. *(00-04; 07-06)*

### Lag feature
A past value of a series used to predict the present - "yesterday's rentals". Built on an
incomplete index, "the previous row" stops meaning "the previous period" and every lag after a gap
is wrong, silently. *(01-05; module 09)*

### Learning curve
A plot of performance against the amount of training data. Steep means more data will help; flat
means it will not, and you need a different model, better features or a different framing.
*(00-02 solutions; 05-08, 07-02)*

### Lifecycle
The full sequence of ML work: frame, define the target, understand the data, split, baseline,
preprocess, train, evaluate, inspect errors, interpret, iterate, deploy and monitor. Training the
model is a small part of it. *(00-03)*

### MAE (mean absolute error)
The average size of the errors, ignoring direction, in the same units as the target:
`MAE = (1/n) * sum |y_i - yhat_i|`. Its virtue is that you can say it out loud to a non-technical
person. Minimised by the median, not the mean. *(00-01; compared with MSE and RMSE in 05-04)*

### Mediator
A variable that lies on the causal path from treatment to outcome. Adjusting for one removes the
effect you were trying to measure - the opposite of what adjusting for a confounder does, and
indistinguishable from it by looking at the data. *(00-04 solutions; 12-07)*

### Multi-armed bandit
The simplest reinforcement learning setting: repeatedly choose among options, observe the reward,
and balance trying new options against exploiting the best one so far. *(00-03; 12-05)*

### Mask (boolean)
An array of True/False, one per element, used to select. `values[values > 5]` is two steps: build
the mask, then index with it. The same mechanism in NumPy and pandas. *(01-03, 01-04)*

### Observation
One thing you make a prediction about - one row. Saying out loud what one row *is* is the first
question of every project. *(00-01; deeper in 02-01)*

### Online learning
See **Batch learning / online learning**.

### Ordinal
A target whose values are ordered but not evenly spaced - a 1-5 star rating. Treating it as
regression assumes equal gaps; as classification discards the order. Name the assumption you are
making. *(00-03 solutions)*

### Overfitting
Fitting the training rows so closely that the rule stops working on new ones. The naked version
memorises answers and scores zero training error; the dangerous version is a large model doing
the same thing while looking sophisticated. *(previewed in 00-01; 05-07, 05-08)*

### Percentile
The share of a distribution falling below a value. Reporting one split's score without saying where
it sits in the distribution of possible splits is how a lucky draw becomes "the result".
*(01-06 solutions; 03-01)*

### Prediction rule (model)
Anything that turns a row's features into a guess about its target. Arithmetic, a lookup table, a
tree, a neural network - all the same kind of object: information in, guess out. *(00-01)*

### Pseudo-labelling
The simplest semi-supervised method: label the unlabelled rows with your model's own confident
predictions and retrain on everything. Fails when the model is confidently wrong, because the
errors become training labels and reinforce themselves. *(00-03 solutions; 12-01)*

### Residual confounding
The bias left over when a confounder is adjusted for but was measured imprecisely. A loyalty
score with as much noise as signal recovered only about a third of the needed correction, with
nothing in the output to indicate it. Why "we controlled for it" deserves a follow-up question.
*(00-04 solutions)*

### Random seed / `random_state`
A fixed starting point for a random number generator, so a run repeats. `np.random.default_rng(0)`
gives you your own generator; `np.random.seed(0)` sets one hidden global that anything can advance.
A seed makes a result repeatable, not correct and not representative. *(01-06; 04-08)*

### Resample
Re-indexing a time series onto a complete set of regular periods, so periods with no data become
explicit rows rather than vanishing. Differs from grouping by date exactly on the empty periods -
which is the case that matters. *(01-05; module 09)*

### Regression
Supervised learning where the target is a number on a scale, so "close" means something. The
test: is 7 nearer to 8 than to 2? *(00-03; module 05)*

### Reinforcement learning
Learning a policy from rewards, where your own actions determine what you observe next - which
creates the trade-off between exploring and exploiting. *(00-03; 12-05)*

### Reproducibility
Someone else getting your number, on their machine, later, from your description. Needs the seed,
the library versions, the exact data, and the order of operations - a seed alone is not enough.
*(01-06; 04-08)*

### Robust (of a summary)
Not easily moved by a few extreme values. The median is robust; the mean is not. Useful when
extremes are noise, harmful when they are the cases that matter most. *(00-01; 03-01)*

### Self-supervised learning
Manufacturing a training signal by hiding part of the data and predicting it from the rest. The
manufactured task is not the point - the representation the model builds in order to solve it is,
and that representation transfers. *(00-03; 10-12, 12-03)*

### Semi-supervised learning
Learning from a few labelled rows plus many unlabelled ones, using the shape of the unlabelled
data to stretch the labels further. *(00-03; 12-01)*

### Sentinel value
A real-looking number standing in for "not recorded" - `-999`, `0`, `99`. It loads as valid data
and quietly distorts every average. *(01-04; 02-04)*

### Split-to-split noise
How much a held-out score changes purely because different rows landed in the test set. On small
data it routinely exceeds the difference between two models, which is why a single split's score is
mostly noise and cross-validation exists. *(01-06; 07-03)*

### Standardisation
Subtracting each feature's mean and dividing by its standard deviation, so values are measured in
deviations rather than in units. Irrelevant to plain linear regression, essential for regularised,
distance-based and neural models. Must be fitted on training rows only. *(01-03; 04-06)*

### Supervised learning
Learning from examples where the outcome was recorded, in order to predict it for new rows. Most
of applied ML, and most of this course. *(00-03; modules 05, 06)*

### Synthetic data
Data generated by code rather than measured. Used here when we need to know the true answer in
advance in order to check whether a method finds it. Never quote a number from synthetic data as
a fact about the world. *(00-01)*

### `transform` (versus `agg`)
Two ways to finish a `groupby`. `agg` collapses each group to one row; `transform` returns one row
per original row, carrying its group's value. Pick by the shape you want. *(01-05)*

### Truncated axis
A chart whose value axis does not start at zero. Legitimate when the variation is the message and
zero is not a meaningful reference - dishonest when it silently magnifies a small change. Disclose
it on the chart. *(01-06)*

### Target
The quantity you want to know but do not have yet - what the model predicts. Also called the
label, or `y`. *(00-01)*

### Training set
The rows used to build the rule. *(00-01; sized and split properly in 04-03)*

### Transfer learning
Starting from a model trained on a large related problem and adapting it with your smaller
dataset, so you inherit general structure and only learn what is specific to you. *(00-03;
10-12, 11-05)*

### Units
What a number measures. Errors have units too: MAE on bikes is in bikes. A standardised value has
no units at all, which is why the original scale must be recorded somewhere. *(00-01, 01-03)*

### Unsupervised learning
Learning where no outcome column exists at all, so you look for structure - groups, dimensions,
oddities. There is no right answer to check against, which is why its results must be validated
from outside the algorithm. *(00-03; module 08)*

### Vectorisation
Replacing a Python loop with one operation on a whole array. Faster because the loop runs in
compiled code instead of returning to the interpreter per element - and shorter, which is the better
reason. *(01-03)*

### View versus copy
A view shares memory with the original, so writing through it writes through to the original; a copy
does not. Plain NumPy slices are views; fancy and boolean indexing give copies. The same idea as
`b = a` in Python and chained indexing in pandas. *(01-02, 01-03, 01-04)*

### `.fit` / `.predict`
The two-step shape almost every scikit-learn model follows. `fit(X, y)` looks at training data
and sets the rule's internals; `predict(X)` applies the rule to rows and returns predictions.
*(00-01)*
