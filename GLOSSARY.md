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

### Cluster stability
Whether the same rows stay grouped together when you re-cluster a random subset of the data.
One of the few genuine checks available for a clustering, because there is no held-out score.
*(00-03 solutions; 08-06)*

### Clustering
Unsupervised grouping of similar rows. The number of groups is something you choose, not
something the algorithm discovers - so clusters are a partition you requested, not a fact about
the world. *(00-03; module 08)*

### Confusion matrix
The four counts behind a yes/no prediction: correctly predicted positives, false alarms, missed
positives, correctly predicted negatives. Every classification metric is built from these.
*(previewed in 00-02 solutions; 06-04)*

### Dimensionality reduction
Replacing many columns with fewer that carry most of the information. *(00-03; 08-07)*

### Drift
The world moving away from the data a model was fitted to, so a once-correct model quietly stops
being correct. Nothing announces it - detecting it is a separate job. *(00-02; 12-02, 13-08)*

### Feature
A piece of information used as input to a prediction, which you will genuinely have at the moment
you make the prediction. A column is only a feature if that second half is true. Also called a
predictor, or `X`. *(00-01)*

### Held-out set
Rows deliberately hidden while a rule is built, used only to score it afterwards. Scoring on rows
the rule was built from measures memory, not skill. Also called a test set. *(00-01; done
properly in 04-03)*

### k-means
A clustering method that partitions rows into a number of groups **you specify**, by repeatedly
assigning each row to the nearest group centre. Sensitive to feature scaling and to the number
you chose. *(00-03; 08-03)*

### Leakage
Using information when building or scoring a model that would not really be available at
prediction time - typically something from the future, or the answer itself under another name.
Makes a useless model look excellent. *(previewed in 00-01; the subject of 04-05)*

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

### Multi-armed bandit
The simplest reinforcement learning setting: repeatedly choose among options, observe the reward,
and balance trying new options against exploiting the best one so far. *(00-03; 12-05)*

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

### Prediction rule (model)
Anything that turns a row's features into a guess about its target. Arithmetic, a lookup table, a
tree, a neural network - all the same kind of object: information in, guess out. *(00-01)*

### Pseudo-labelling
The simplest semi-supervised method: label the unlabelled rows with your model's own confident
predictions and retrain on everything. Fails when the model is confidently wrong, because the
errors become training labels and reinforce themselves. *(00-03 solutions; 12-01)*

### Regression
Supervised learning where the target is a number on a scale, so "close" means something. The
test: is 7 nearer to 8 than to 2? *(00-03; module 05)*

### Reinforcement learning
Learning a policy from rewards, where your own actions determine what you observe next - which
creates the trade-off between exploring and exploiting. *(00-03; 12-05)*

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

### Supervised learning
Learning from examples where the outcome was recorded, in order to predict it for new rows. Most
of applied ML, and most of this course. *(00-03; modules 05, 06)*

### Synthetic data
Data generated by code rather than measured. Used here when we need to know the true answer in
advance in order to check whether a method finds it. Never quote a number from synthetic data as
a fact about the world. *(00-01)*

### Target
The quantity you want to know but do not have yet - what the model predicts. Also called the
label, or `y`. *(00-01)*

### Training set
The rows used to build the rule. *(00-01; sized and split properly in 04-03)*

### Transfer learning
Starting from a model trained on a large related problem and adapting it with your smaller
dataset, so you inherit general structure and only learn what is specific to you. *(00-03;
10-12, 11-05)*

### Unsupervised learning
Learning where no outcome column exists at all, so you look for structure - groups, dimensions,
oddities. There is no right answer to check against, which is why its results must be validated
from outside the algorithm. *(00-03; module 08)*

### `.fit` / `.predict`
The two-step shape almost every scikit-learn model follows. `fit(X, y)` looks at training data
and sets the rule's internals; `predict(X)` applies the rule to rows and returns predictions.
*(00-01)*
