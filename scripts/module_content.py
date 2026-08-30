"""Hand-written prose for the per-module READMEs, plus the one-line idea of every chapter.

Kept separate from the renderer so that build_module_readmes.py stays mechanical.
Edit here; re-run scripts/build_module_readmes.py to regenerate.
"""

# One sentence per chapter: the single idea it exists to install.
ONE_IDEA = {
    "00-01": "A prediction is a rule from known information to an unknown quantity, and a perfect training score can mean nothing.",
    "00-02": "ML is data + answers -> rules, so when you already have the rule, using ML is a downgrade.",
    "00-03": "The kind of learning is decided by what data you have, and a clustering is a partition you requested.",
    "00-04": "A model that predicts Y well tells you almost nothing about what happens if you change X.",

    "01-01": "Ten tasks that tell you whether to skip this module, skim it, or work through it.",
    "01-02": "The dozen Python constructs that carry data work - and the two aliasing bugs that return old results.",
    "01-03": "An array operation replaces a loop, and the shape tells you whether it was the right one.",
    "01-04": "A DataFrame is labelled NumPy, and the dtypes are where the silent wrong answers live.",
    "01-05": "Group, join and resample - and count your rows, because a join can quietly duplicate them.",
    "01-06": "A chart is an argument and a seed is a promise; one split's score is mostly noise.",

    "02-01": "The unit of observation is a decision, and the average of averages is a different number.",
    "02-02": "Data is a record of a process; a change in measurement looks exactly like a change in the world.",
    "02-03": "The rows that were never created are invisible, and more data cannot fix their absence.",
    "02-04": "Every visible defect needs a decision, and dropna() is itself a selection mechanism.",
    "02-05": "An outlier is a question, not a category - and automatic removal deletes the rows that matter most.",
    "02-06": "Relationships can appear, vanish or reverse depending on what else you hold constant.",
    "02-07": "Every number on the slide is true and the impression is still wrong; and the arrow is not in the data.",
    "02-08": "The whole module applied to one real dataset, ending in a written data dictionary.",

    "03-01": "Mean and median are answers to two different questions, and numpy and pandas disagree about variance.",
    "03-02": "The same number computed twice never matches, and how far it moves is predictable.",
    "03-03": "Resampling turns a single number into an honest interval, with no formula to memorise.",
    "03-04": "Conditional probability is counting in a restricted world, and base rates decide everything.",
    "03-05": "Bayes' rule is arithmetic on counts before it is a formula about beliefs.",
    "03-06": "A model is a function; slope, intercept and logarithm are the three shapes you need first.",
    "03-07": "Distance, dot product and shape are the vocabulary every model after this is written in.",
    "03-08": "A loss turns 'better' into a number, and a gradient says which way to step.",

    "04-01": "Unit, target, prediction time and horizon - the contract that has to exist before any model.",
    "04-02": "The number your model must beat, computed before your model exists.",
    "04-03": "Held-out data is the only evidence, and stratification protects the rare class.",
    "04-04": "When rows share an entity or a timeline, a random split is a lie.",
    "04-05": "Four ways the future gets into your features, each one producing a suspiciously good score.",
    "04-06": "Every transformation is fitted on training rows only, or the test set has already leaked.",
    "04-07": "A pipeline makes leakage-free preprocessing the default rather than a discipline.",
    "04-08": "A result nobody can reproduce is a rumour; seeds are necessary and not sufficient.",

    "05-01": "The constant that minimises MAE is the median, not the mean - and both are baselines.",
    "05-02": "A line fitted by hand, so least squares is arithmetic before it is a library call.",
    "05-03": "A coefficient means 'holding the others constant', which is a claim about the data you have.",
    "05-04": "Each error measure encodes a different belief about what mistakes cost.",
    "05-05": "The pattern in what a model got wrong tells you what to build next.",
    "05-06": "Gradient descent from scratch: the learning rate is the whole difference between convergence and divergence.",
    "05-07": "Capacity is the ability to fit any shape, including the noise.",
    "05-08": "Learning curves tell you whether more data or a different model is the answer.",
    "05-09": "Paying for complexity: shrinkage, sparsity, and why scaling suddenly matters.",
    "05-10": "Trees split the space into boxes; forests average many of them to cut variance.",
    "05-11": "Boosting fits the residual repeatedly - strong, and easy to tune dishonestly.",
    "05-12": "The full workflow on a real dataset, ending in error broken down by segment.",

    "06-01": "The majority-class baseline, and why accuracy is the wrong first question.",
    "06-02": "A linear score squashed into a probability, fitted by maximising likelihood.",
    "06-03": "What a model can and cannot separate, drawn in two dimensions.",
    "06-04": "Four counts generate every classification metric there is.",
    "06-05": "Precision and recall are a choice of denominator, and the choice is the business decision.",
    "06-06": "ROC measures ranking; PR measures ranking where the positives are rare.",
    "06-07": "The threshold is not 0.5 - it is wherever expected cost is lowest.",
    "06-08": "Most imbalance 'fixes' change the metric rather than the model.",
    "06-09": "A score is not a probability until it is calibrated, and decisions need probabilities.",
    "06-10": "Three different ideas of similarity: distance, independence, and margin.",
    "06-11": "Ensembles of trees, and the probabilities they produce need checking.",
    "06-12": "More than two classes, more than one label, and where the errors concentrate.",

    "07-01": "One splitter per data structure - grouped, stratified, time-aware.",
    "07-02": "Two curves that diagnose underfitting, overfitting and 'get more data'.",
    "07-03": "A fair comparison is the same splits, the same budget, and a reported spread.",
    "07-04": "Tune on the test set and your reported score is the maximum of many draws.",
    "07-05": "One number hides everything; slice the errors and the next experiment names itself.",
    "07-06": "What the model used is not what causes the outcome, and importance measures disagree.",
    "07-07": "A local explanation is a story about one prediction, and significance is not size.",

    "08-01": "Structure without labels means no score, so every check comes from outside the algorithm.",
    "08-02": "Distance is decided by your scaling and your columns, long before the algorithm runs.",
    "08-03": "k-means finds the k you asked for, in any data, always.",
    "08-04": "A dendrogram postpones the choice of k and does not remove it.",
    "08-05": "Density and mixtures: clusters that are not blobs, and points that belong to none.",
    "08-06": "Stability under resampling is the closest thing to validation clustering has.",
    "08-07": "PCA rotates to the directions of most variance - which is not the same as most meaning.",
    "08-08": "Neighbour embeddings distort distance by design, so never measure on a t-SNE plot.",

    "09-01": "Explaining, nowcasting and forecasting differ only in what you know at prediction time.",
    "09-02": "Level, trend and season, and why one year of data cannot separate them.",
    "09-03": "Every lag and rolling feature must be built on a complete index or it is off by a period.",
    "09-04": "Seasonal-naive is the baseline forecasts have to beat, and it usually is not beaten easily.",
    "09-05": "Backtesting: expanding windows, gaps, and the leak that makes a forecast look perfect.",
    "09-06": "Exponential smoothing: a weighted memory of the past, with three interpretable knobs.",
    "09-07": "ARIMA well enough to read a paper and ask the right question about it.",
    "09-08": "Turning a series into a supervised table, and putting an interval around the answer.",
    "09-09": "A forecast end to end, with error broken down by season and horizon.",

    "10-01": "A neuron is a weighted sum and a decision, computed by hand.",
    "10-02": "One forward pass with real numbers and printed shapes.",
    "10-03": "Activations decide what shapes are expressible; losses decide what is being optimised.",
    "10-04": "Backpropagation is the chain rule applied layer by layer, in NumPy.",
    "10-05": "The PyTorch training loop, where every line corresponds to something you already built.",
    "10-06": "Batch size, epochs, learning rate and initialisation - the knobs that decide whether it trains at all.",
    "10-07": "Optimisers and regularisation, and what each one actually changes.",
    "10-08": "Debugging: overfit one batch first, then read the loss curve.",
    "10-09": "Convolution is weight sharing plus locality - and that is the whole idea.",
    "10-10": "Sequences, the bottleneck they create, and what attention was invented to fix.",
    "10-11": "Self-attention and embeddings, built up from the parts you already have.",
    "10-12": "An honest map of transfer, self-supervision, generative and foundation models, with real prerequisites.",

    "11-01": "Text becomes numbers by counting, and TF-IDF is a weighting decision.",
    "11-02": "A text pipeline end to end, including the leak that text invites.",
    "11-03": "Embeddings capture similarity, including the similarities you did not want.",
    "11-04": "An image is a tensor, and a filter is a small pattern detector.",
    "11-05": "Augmentation and frozen features: how a laptop trains a useful vision model.",
    "11-06": "Popularity is the recommender baseline, and it is hard to beat.",
    "11-07": "Ranking metrics, cold start, and the feedback loop your model creates.",

    "12-01": "A few labels plus many unlabelled rows - and when pseudo-labels reinforce their own errors.",
    "12-02": "Learning as data arrives, and detecting when the world has moved.",
    "12-03": "Transfer and self-supervision revisited with code rather than description.",
    "12-04": "Predicting a distribution rather than a number, and saying how sure you are.",
    "12-05": "Explore versus exploit, and a tabular Q-learning agent small enough to read.",
    "12-06": "Graphs and federated learning: what the idea is and what it demands.",
    "12-07": "Causal inference and the honest map of everything this course did not cover.",

    "13-01": "Fairness definitions that cannot all hold at once, and proxies that carry what you removed.",
    "13-02": "Privacy, misuse and oversight as design constraints rather than afterthoughts.",
    "13-03": "Data cards and model cards: what the thing is for, and what it is not for.",
    "13-04": "One fitted object applied identically in training and serving, or the two will drift apart.",
    "13-05": "Tests for data and tests for models, built from the shape of the failure.",
    "13-06": "A run you can find again a year later, with its data and its code.",
    "13-07": "Batch and online inference, shadow deployment, and a rollback trigger written in advance.",
    "13-08": "Monitoring inputs, outputs and outcomes, and deciding in advance what triggers a retrain.",

    "14-01": "The whole course applied to one problem, with every decision written down.",
    "14-02": "A classification project with the metric and threshold argued from cost.",
    "14-03": "An unsupervised investigation reported as hypotheses rather than findings.",
    "14-04": "A small deep-learning or domain project, with a baseline it has to beat.",
    "14-05": "An open problem, starting from whether machine learning is appropriate at all.",
}

# Per-module prose: why the module exists, and what to do if short of time.
MODULE_PROSE = {
    "00": (
        "Orientation. No models are fitted here beyond a two-line baseline - the point is to know what "
        "the subject is, what it is not, and which question you are answering before any code is written.\n\n"
        "If you read only one chapter of this module, read **00-04**. Confusing prediction with cause is the "
        "most expensive mistake in applied machine learning, and it does not announce itself.",
        "Nothing. It is four short chapters and everything after them assumes the vocabulary.",
    ),
    "01": (
        "The optional bridge. Enough Python, NumPy, pandas and matplotlib that the rest of the course is one "
        "problem at a time rather than two - a new idea *and* a syntax fight.\n\n"
        "Every chapter here ends with a failure lab, because the mistakes these tools invite - a wrong axis, "
        "a chained assignment, a join that multiplies rows, an unseeded split - are exactly the mistakes that "
        "later produce a model that looks fine and is not.",
        "Take the diagnostic in **01-01** first. Score 9 or more and skip the module entirely; 6 to 8 and read "
        "only the chapters your failures point to.",
    ),
    "02": (
        "Data literacy. Most modelling disasters are data misunderstandings that were visible in the first "
        "hour, and this module is that hour.\n\n"
        "The order is deliberate: what a row is, where it came from, who is missing, what is broken, what is "
        "merely surprising, what appears when you look at two columns at once, and how to show it honestly. "
        "Only then does a real dataset arrive.",
        "**02-01** and **02-05** are the two that change how you work. 02-06 can wait until module 07 if you "
        "are impatient to model.",
    ),
    "03": (
        "The mathematics actually used, on a ladder from counting to gradients. Every idea here is also "
        "re-introduced later, immediately before the model that needs it - distances before kNN, gradients "
        "before gradient descent, likelihood before logistic regression.\n\n"
        "That repetition is deliberate. A single maths block early is the most reliable way to lose a near "
        "beginner, so this module is a first pass and a reference rather than a gate.",
        "**03-03** (uncertainty) and **03-08** (loss and gradients) are the two that later modules lean on "
        "hardest. The rest can be read as needed.",
    ),
    "04": (
        "The spine of the course. Framing, baselines, splitting, leakage, preprocessing, pipelines and "
        "reproducibility - the part that separates a working model from an impressive-looking one.\n\n"
        "Nine of the later modules name a chapter from here as a prerequisite. If you skip anything in this "
        "course, do not skip this module.",
        "Nothing. **04-05** (leakage) and **04-07** (pipelines) are the two most-cited chapters in the whole "
        "curriculum.",
    ),
    "05": (
        "Regression: predicting a number. The module builds from a constant to gradient boosting, and every "
        "step has to earn its place against the baseline from 05-01.\n\n"
        "The order is capability, then cost: fit a line, read the errors, add capacity, watch it overfit, pay "
        "to control it, then move to trees where capacity is cheap and interpretation is harder.",
        "**05-04** (metrics) and **05-08** (bias, variance, learning curves) are load-bearing for modules 06 "
        "and 07. 05-09 can be skimmed if you are not using regularised models.",
    ),
    "06": (
        "Classification: predicting a category. Half of this module is about *metrics and thresholds* rather "
        "than models, because that is where classification projects actually fail.\n\n"
        "Accuracy is dismantled in 06-04, rebuilt as precision and recall in 06-05, turned into a cost "
        "decision in 06-07, and only then do the model families arrive.",
        "**06-04** to **06-07** are the core. The model chapters (06-10, 06-11) can be read later; the metric "
        "chapters cannot.",
    ),
    "07": (
        "Evaluation and interpretation. How to compare models without fooling yourself, find where a model "
        "fails, and explain it without claiming more than you know.\n\n"
        "This module is where the habits from 01-06 (split-to-split noise) and 02-05 (error by segment) become "
        "formal machinery.",
        "**07-05** (error analysis) is the highest-value chapter in the module and the one practitioners use "
        "daily.",
    ),
    "08": (
        "Unsupervised learning: structure without labels. The defining property is that there is no score, so "
        "every check has to come from outside the algorithm.\n\n"
        "The module spends as much time on *how to be sceptical about a clustering* as on the algorithms "
        "themselves, because a clustering that is wrong produces exactly the same confident output as one "
        "that is right.",
        "**08-02** (distance and scaling) and **08-06** (stability) matter more than any individual "
        "algorithm.",
    ),
    "09": (
        "Time series. Every idea from module 04 returns with a harder constraint: the future must not leak "
        "into the past, in the features, in the split, or in the evaluation.\n\n"
        "Classical methods and machine-learning methods both appear, and the baselines in 09-04 are genuinely "
        "hard to beat.",
        "**09-01** (framing), **09-03** (lags) and **09-05** (backtesting) are the ones that prevent silent "
        "disasters. 09-07 (ARIMA) is marked optional.",
    ),
    "10": (
        "Neural networks, built up from one neuron. Backpropagation is implemented in NumPy before PyTorch "
        "appears, so the framework is a faster hand rather than a black box.\n\n"
        "Core chapters run on a laptop CPU. Anything needing a GPU is marked optional and says so.",
        "**10-01** to **10-05** are the mechanism. 10-09 onwards are intuition chapters that can be read "
        "without the earlier code if you are short of time - but they will mean less.",
    ),
    "11": (
        "Text, images and recommendations. Each domain starts with a baseline that is embarrassingly simple "
        "and often competitive, then adds the domain-specific machinery.\n\n"
        "The recurring lesson is that a well-framed simple model with good features usually beats a "
        "poorly-framed complex one.",
        "Pick the domain you need. The three tracks (NLP, vision, recommenders) are independent of each "
        "other.",
    ),
    "12": (
        "The rest of the field, surveyed honestly. Some chapters teach a method; others map a subject and "
        "state its real prerequisites rather than pretending a notebook creates mastery.\n\n"
        "**12-07** carries the advanced field map: what exists beyond this course, and what you would need to "
        "learn first.",
        "**12-02** (drift) and **12-07** (causality) are core. The other five are marked optional and can be "
        "read in any order.",
    ),
    "13": (
        "Responsible and production machine learning. Fairness, privacy, documentation, packaging, testing, "
        "deployment and monitoring - the work that starts when the model is finished.\n\n"
        "The recurring theme is that deploying a model is the beginning of the work, not the end: the world "
        "moves, and nothing in the model notices.",
        "**13-04** (packaging) and **13-08** (monitoring) are the two that decide whether a model survives "
        "contact with production.",
    ),
    "14": (
        "Capstones. Each one requires decisions and written justification rather than a recipe, and each is "
        "longer than a normal chapter.\n\n"
        "The final project starts one step before every other project in this course: deciding whether "
        "machine learning is appropriate at all.",
        "Nothing - but do them in order. 14-01 is guided and the guidance decreases from there.",
    ),
}
