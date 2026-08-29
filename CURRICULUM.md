# Curriculum

121 chapters in 15 modules. Order is prerequisite-safe: nothing is used before the chapter
that teaches it. Labels are **Core** (do it), **Applied** (do it, it is a project chapter)
and **Optional** (skip on a first pass without breaking anything later).

The workflow below is repeated in every applied chapter until it is automatic:

> **frame -> understand data -> define target -> split -> baseline -> preprocess -> train
> -> evaluate -> inspect errors -> interpret -> choose the next experiment**

`curriculum.yml` holds the same list in machine-readable form, including status.

---

## Module 00 - Orientation (4 chapters)

*Goal: know what this subject is, what it is not, and what question you are answering
before you ever fit a model.*

| ID | Chapter | Label | Prereqs |
|---|---|---|---|
| 00-01 | Start here: the course map, your notebook, and your first prediction by hand | Core | basic Python |
| 00-02 | What machine learning is, is not, and when a rule or a query wins | Core | 00-01 |
| 00-03 | The kinds of learning, and the map of the work | Core | 00-02 |
| 00-04 | Prediction, explanation, and cause | Core | 00-03 |

Outcomes: define a prediction problem in one sentence; say what one row is; recognise the
three or four situations where ML is the wrong tool; name where you are in the lifecycle.

## Module 01 - Python and data bridge (6 chapters, Optional/skippable)

*Goal: enough Python, NumPy and pandas to stop fighting the tools. Chapter 01-01 is a
diagnostic - pass it and skip the module.*

| ID | Chapter | Label | Prereqs |
|---|---|---|---|
| 01-01 | Diagnostic: can you skip this module? | Optional | 00-01 |
| 01-02 | Essential Python for data work | Optional | 01-01 |
| 01-03 | NumPy: arrays, shapes, and vectorised thinking | Optional | 01-02 |
| 01-04 | pandas I: loading, selecting, filtering, dtypes | Optional | 01-03 |
| 01-05 | pandas II: grouping, joining, timestamps | Optional | 01-04 |
| 01-06 | Plotting that says something, and reproducible random numbers | Optional | 01-05 |

## Module 02 - Data literacy and EDA (8 chapters)

*Goal: read a dataset like a sceptic. Most modelling disasters are data misunderstandings
that were visible in the first hour.*

| ID | Chapter | Label | Prereqs |
|---|---|---|---|
| 02-01 | What is a row? observations, features, targets, labels, units, dtypes | Core | 00-04 |
| 02-02 | Where data comes from: provenance and the collection process | Core | 02-01 |
| 02-03 | Sampling and selection bias: the rows you never see | Core | 02-02 |
| 02-04 | Missing values, duplicates, impossible values, inconsistent categories | Core | 02-03 |
| 02-05 | Distributions, outliers, and transformations | Core | 02-04 |
| 02-06 | Univariate, bivariate, multivariate: looking without fooling yourself | Core | 02-05 |
| 02-07 | Honest visualisation, correlation vs causation, and the limits of EDA | Core | 02-06 |
| 02-08 | Applied: a full EDA and a written data dictionary | Applied | 02-07 |

## Module 03 - Mathematical and statistical foundations (8 chapters)

*Goal: the maths you actually use, on the ladder from counting to gradients. Each idea is
re-introduced later next to the model that needs it - see D-10.*

| ID | Chapter | Label | Prereqs |
|---|---|---|---|
| 03-01 | Summaries: mean, median, quantiles, variance, standard deviation | Core | 02-05 |
| 03-02 | Distributions and sampling: why two samples never agree | Core | 03-01 |
| 03-03 | Uncertainty: error bars and confidence intervals by resampling | Core | 03-02 |
| 03-04 | Probability and conditional probability, with counts | Core | 03-02 |
| 03-05 | Bayes' rule you can do on paper | Core | 03-04 |
| 03-06 | Functions, lines, slopes, and logarithms | Core | 03-01 |
| 03-07 | Vectors, distance, norms, dot products, matrices and shapes | Core | 03-06 |
| 03-08 | Loss functions, finite differences, gradients, and what optimisation means | Core | 03-07 |

## Module 04 - A reliable ML workflow (8 chapters)

*Goal: the part that separates a working model from an impressive-looking one. This module
is the spine of the whole course.*

| ID | Chapter | Label | Prereqs |
|---|---|---|---|
| 04-01 | Framing: unit of observation, target, prediction time, horizon | Core | 02-08, 03-01 |
| 04-02 | Baselines first, always | Core | 04-01 |
| 04-03 | Splitting I: train, validation, test; random and stratified | Core | 04-02 |
| 04-04 | Splitting II: grouped and chronological splits | Core | 04-03 |
| 04-05 | Leakage lab: target, temporal, duplicate and preprocessing leakage | Core | 04-04 |
| 04-06 | Preprocessing: imputation, encoding, scaling, transformations | Core | 04-05 |
| 04-07 | Pipelines and cross-validation, done without leaking | Core | 04-06 |
| 04-08 | Reproducibility, seeds, and tracking experiments you can trust | Core | 04-07 |

## Module 05 - Regression (12 chapters)

| ID | Chapter | Label | Prereqs |
|---|---|---|---|
| 05-01 | Predicting a number: mean and median baselines | Core | 04-02 |
| 05-02 | Simple linear regression, fitted by hand | Core | 03-06, 05-01 |
| 05-03 | Multiple linear regression and what a coefficient means | Core | 03-07, 05-02 |
| 05-04 | Metrics: MAE, MSE, RMSE, the trouble with MAPE, and R-squared | Core | 05-01 |
| 05-05 | Residuals: reading the errors your model leaves behind | Core | 05-04 |
| 05-06 | Gradient descent from scratch | Core | 03-08, 05-03 |
| 05-07 | Polynomial and interaction features; underfitting and overfitting | Core | 05-03 |
| 05-08 | Bias and variance, and learning curves that diagnose them | Core | 05-07 |
| 05-09 | Ridge, Lasso, Elastic Net: paying for complexity | Core | 05-08 |
| 05-10 | Regression trees and random forests | Core | 05-08 |
| 05-11 | Gradient boosting, and tuning hyperparameters honestly | Core | 05-10, 04-07 |
| 05-12 | Applied: a regression checkpoint with segment error analysis | Applied | 05-11, 04-05 |

## Module 06 - Classification (12 chapters)

| ID | Chapter | Label | Prereqs |
|---|---|---|---|
| 06-01 | Predicting a category: framing and baselines | Core | 04-02 |
| 06-02 | Logistic regression: from a score to a probability | Core | 03-08, 06-01 |
| 06-03 | Decision boundaries you can see | Core | 06-02 |
| 06-04 | The confusion matrix; accuracy and why it lies | Core | 06-03 |
| 06-05 | Precision, recall, specificity, F1 - and which one your problem needs | Core | 06-04 |
| 06-06 | ROC-AUC and PR-AUC: what each curve actually shows | Core | 06-05 |
| 06-07 | Choosing a threshold when mistakes cost different amounts | Core | 06-06 |
| 06-08 | Class imbalance: real remedies and fake ones | Core | 06-07 |
| 06-09 | Probability calibration: when 0.8 should mean 80% | Core | 06-06 |
| 06-10 | k-nearest neighbours, naive Bayes, and support vector machines | Core | 03-07, 06-03 |
| 06-11 | Trees, random forests and gradient boosting for classification | Core | 05-11, 06-05 |
| 06-12 | Multiclass, multilabel, and classification error analysis | Core | 06-11 |

## Module 07 - Evaluation and interpretation (7 chapters)

| ID | Chapter | Label | Prereqs |
|---|---|---|---|
| 07-01 | Cross-validation patterns for every kind of data | Core | 04-07, 06-05 |
| 07-02 | Learning curves and validation curves as diagnosis | Core | 05-08 |
| 07-03 | Comparing models fairly, and searching hyperparameters | Core | 07-01 |
| 07-04 | Why tuning on the test set flatters you: nested evaluation | Core | 07-03 |
| 07-05 | Error analysis and data slices: where the model fails | Core | 07-02 |
| 07-06 | Interpreting models: coefficients, tree importance, permutation importance, PDP | Core | 07-05 |
| 07-07 | Local explanations and SHAP; statistical vs practical significance; association vs causation | Core | 07-06, 03-03 |

## Module 08 - Unsupervised learning (8 chapters)

| ID | Chapter | Label | Prereqs |
|---|---|---|---|
| 08-01 | Learning without labels: what it can and cannot establish | Core | 02-06 |
| 08-02 | Similarity, distance, scaling, and high-dimensional strangeness | Core | 03-07, 08-01 |
| 08-03 | k-means | Core | 08-02 |
| 08-04 | Hierarchical clustering | Core | 08-03 |
| 08-05 | DBSCAN and Gaussian mixtures | Core | 08-03 |
| 08-06 | Evaluating clusters, stability, and interpreting them responsibly | Core | 08-05 |
| 08-07 | PCA | Core | 03-07, 08-02 |
| 08-08 | t-SNE and UMAP (and their limits); anomaly detection; optional association rules | Core | 08-07 |

## Module 09 - Time series and forecasting (9 chapters)

| ID | Chapter | Label | Prereqs |
|---|---|---|---|
| 09-01 | Time-series framing: explaining vs nowcasting vs forecasting | Core | 04-01 |
| 09-02 | Trend and seasonality | Core | 09-01 |
| 09-03 | Lags, rolling features, autocorrelation | Core | 09-02 |
| 09-04 | Naive and seasonal-naive baselines; what a horizon costs you | Core | 09-03 |
| 09-05 | Expanding and rolling-window evaluation; the temporal leakage lab | Core | 09-04, 04-05 |
| 09-06 | Exponential smoothing | Core | 09-04 |
| 09-07 | ARIMA, enough to read a paper and ask a good question | Optional | 09-06 |
| 09-08 | ML-based forecasting and prediction intervals | Core | 09-05, 05-11 |
| 09-09 | Applied: a forecasting checkpoint, error by season and horizon, drift | Applied | 09-08 |

## Module 10 - Neural networks and deep learning (12 chapters)

*PyTorch, CPU only for core chapters (D-05).*

| ID | Chapter | Label | Prereqs |
|---|---|---|---|
| 10-01 | A neuron is a weighted sum and a decision | Core | 03-07, 06-02 |
| 10-02 | A forward pass with real numbers, on paper | Core | 10-01 |
| 10-03 | Activation functions and loss functions | Core | 10-02 |
| 10-04 | Backpropagation from scratch in NumPy | Core | 03-08, 10-03 |
| 10-05 | Your first multilayer perceptron in PyTorch | Core | 10-04 |
| 10-06 | Batches, epochs, learning rates, initialisation | Core | 10-05 |
| 10-07 | Optimisers and regularisation | Core | 10-06 |
| 10-08 | Debugging a neural network that will not learn | Core | 10-07 |
| 10-09 | Convolution intuition | Core | 10-08 |
| 10-10 | Sequence models and why attention was invented | Core | 10-08 |
| 10-11 | Transformers and embeddings | Core | 10-10 |
| 10-12 | Transfer learning, self-supervision, generative and foundation models: an honest map | Core | 10-11 |

## Module 11 - Applied domains (7 chapters)

| ID | Chapter | Label | Prereqs |
|---|---|---|---|
| 11-01 | NLP: bag of words and TF-IDF | Applied | 06-05 |
| 11-02 | NLP: text classification end to end | Applied | 11-01, 04-07 |
| 11-03 | NLP: embeddings, and what they do and do not capture | Applied | 11-02, 10-11 |
| 11-04 | Vision: images as tensors, and what a convolution sees | Applied | 10-09 |
| 11-05 | Vision: augmentation and transfer learning | Applied | 11-04 |
| 11-06 | Recommenders: popularity baseline, content-based, collaborative filtering | Applied | 08-02 |
| 11-07 | Recommenders: ranking metrics, cold start, feedback loops | Applied | 11-06 |

## Module 12 - Other learning paradigms (7 chapters)

| ID | Chapter | Label | Prereqs |
|---|---|---|---|
| 12-01 | Semi-supervised and active learning | Optional | 06-09 |
| 12-02 | Online learning, incremental learning, and concept drift | Core | 09-09 |
| 12-03 | Transfer and self-supervised learning, revisited concretely | Optional | 10-12 |
| 12-04 | Probabilistic modelling and honest uncertainty | Optional | 03-05, 09-08 |
| 12-05 | Multi-armed bandits, RL concepts, and a tiny tabular Q-learning example | Optional | 03-04 |
| 12-06 | Graph machine learning and federated learning: intuition only | Optional | 08-02 |
| 12-07 | Causal prediction vs causal inference, plus the advanced field map | Core | 07-07 |

## Module 13 - Responsible and production ML (8 chapters)

| ID | Chapter | Label | Prereqs |
|---|---|---|---|
| 13-01 | Fairness: goals that conflict, representation, harmful proxies | Core | 07-05 |
| 13-02 | Privacy, security, misuse, and human oversight | Core | 13-01 |
| 13-03 | Data cards and model cards | Core | 13-02 |
| 13-04 | Packaging a pipeline so prediction matches training | Core | 04-07 |
| 13-05 | Testing data and testing models | Core | 13-04 |
| 13-06 | Experiment tracking and versioning | Core | 04-08 |
| 13-07 | Batch and online inference, deployment and rollback | Core | 13-04 |
| 13-08 | Monitoring: data quality, drift, performance, and retraining triggers | Core | 13-07, 12-02 |

## Module 14 - Capstones (5 chapters)

*Each capstone requires written justification, not a recipe. Longer than a normal chapter.*

| ID | Chapter | Label | Prereqs |
|---|---|---|---|
| 14-01 | Guided: an end-to-end, time-aware project | Applied | 09-09, 13-08 |
| 14-02 | Less guided: a classification project | Applied | 06-12, 07-07 |
| 14-03 | Open: an unsupervised or anomaly investigation | Applied | 08-08 |
| 14-04 | Small deep-learning or domain project | Applied | 11-05 |
| 14-05 | Final open-ended project, including "is ML even appropriate here?" | Applied | 14-01..14-04 |

---

## Assessments

A cumulative assessment closes each module from 02 onwards, mixing old and new material,
and always containing at least one deliberately ambiguous problem where the correct first
move is to ask clarifying questions rather than to model. They live in `assessments/`.

## Pedagogical changes from the original outline

Recorded here as required; the reasoning is in `DECISIONS.md`.

- **Phase 0 restructured to 4 notebooks** (D-08, D-13). "How to use Jupyter" is
  folded into 00-01; a standalone chapter on running cells delays the first real idea for a
  learner who is, by definition, already running cells. 00-01 therefore also carries a real
  concept so orientation is not content-free.
- **The taxonomy and the causality material were separated** (D-13). Kinds of learning plus
  the lifecycle is a map of the field; prediction versus cause is one sharp idea that needs its
  own failure lab. Together they made a 90-minute chapter with two centres of gravity.
- **The learner diagnostic was split in two** (D-09): ML expectations in 00-01, Python
  readiness in 01-01, each asked where it is actionable.
- **Maths is deliberately not a single block** (D-10). Module 03 exists as a reference and a
  first pass, but every mathematical idea reappears immediately before the model that needs
  it.
- **Each chapter chooses its own dataset** (D-14). The original plan made Seoul bike sharing a
  recurring case study; that is now optional. Methods reveal their character on data with the right
  shape - imbalance, heavy tails, real clusters, a genuine seasonal cycle - and forcing one dataset
  through every chapter would hide exactly what several chapters exist to show. Every dataset still
  has to be documented in `data/README.md` before use.
- **Classification and clustering do not manufacture targets from unsuitable data** (D-07). Manufacturing
  a binary target from a count would teach exactly the habit this course argues against.
- **Boosting is taught with scikit-learn's HistGradientBoosting** rather than XGBoost
  (D-04), and the vocabulary differences are named explicitly so the learner is not
  ambushed in an interview.
