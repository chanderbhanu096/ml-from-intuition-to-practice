# Data

Nothing in this folder is committed except this file. Raw data stays in `data/raw/`, which
is git-ignored.

Every dataset used anywhere in the course must be documented here with: verified source,
licence, target, unit of observation, what a timestamp means, known limitations, and how to
retrieve it.

---

## 1. Tiny hand-written tables (modules 00 onwards)

**Status:** built into the notebooks.
Three to ten rows, typed directly into the notebook so you can check every calculation by
hand. These are *illustrations*, not evidence: no conclusion about the real world is ever
drawn from them.

---

## 2. Synthetic datasets (labelled as synthetic wherever used)

**Status:** generated in the notebook with a fixed random seed.
Used when a chapter needs a specific, controllable property - a known true relationship, a
planted outlier, a deliberate leak, a drift after a certain date. The point of synthetic
data is that we know the right answer in advance and can check whether the method finds it.

Every synthetic dataset in this course is created by visible code in the notebook that uses
it, with `rng = np.random.default_rng(seed)`, and is labelled **SYNTHETIC** in the text.
Never quote a number from synthetic data as a fact about the world.

---

## 3. scikit-learn built-in datasets (modules 05 onwards)

**Status:** shipped with scikit-learn, no download.
Used where a small, well-understood, real dataset is enough (e.g. `load_diabetes`,
`load_breast_cancer`, `fetch_california_housing` - the last one does download, and the
notebook that uses it says so).
Their documentation, including collection caveats, is in the scikit-learn user guide under
"Toy datasets" and "Real world datasets". Several of them carry serious ethical caveats
(the Boston housing dataset was removed from scikit-learn for this reason); where a caveat
exists, the notebook states it rather than quietly using the data.

---

## 4. Seoul bike sharing demand - the recurring case study

**Status in this repository: NOT PRESENT.** No file has been downloaded, so nothing below
about its contents has been verified here. Treat the schema note as *expected*, and confirm
it against the real file before relying on it. No notebook asserts a column name, statistic
or result from this dataset until the file exists.

- **Expected source:** UCI Machine Learning Repository, "Seoul Bike Sharing Demand"
  (dataset 560), <https://archive.ics.uci.edu/dataset/560/seoul+bike+sharing+demand>.
  Originally published by the Seoul Metropolitan Government open data portal.
- **Expected licence:** Creative Commons Attribution 4.0 International (CC BY 4.0), as
  stated on the UCI dataset page. **Verify this on the page before redistributing anything.**
- **Retrieval:** `python scripts/get_seoul_bike.py` downloads the archive into `data/raw/`
  and prints the real schema, row count and date range. It does not overwrite an existing
  file. Run it yourself - the course never downloads anything without you asking.
- **Unit of observation (expected):** one row = one hour, at one city-wide level, for the
  city of Seoul. Not one bike, not one rental, not one station.
- **Target (for this course):** the number of bikes rented in that hour. A count: whole
  numbers, never negative.
- **Meaning of time:** the timestamp is the hour the rentals happened, so the weather in
  the same row is *observed* weather for that hour. This matters enormously: using it to
  predict the future means assuming a perfect weather forecast. Module 04 and module 09
  make this the centre of the leakage discussion.
- **Known limitations (expected, to confirm):** roughly one year of data, so seasonal
  effects are observed only once and cannot be separated from "things that happened that
  year"; a single city, so nothing generalises to other cities without evidence; the count
  is capped by how many bikes exist, so very high demand may be censored rather than
  measured; days when the system was not operating are recorded and must be handled
  deliberately, not silently dropped.
- **What it is not suitable for:** binary classification (there is no natural binary
  target), causal claims about weather policy, or anything about individual riders - there
  is no person-level data here, by design.

### The prediction contract - answer this before every Seoul bike exercise

1. Are we **explaining** this hour's demand, **nowcasting** it, or **forecasting** a future
   hour?
2. What is the prediction time, and what is the horizon?
3. Which of these columns would genuinely be known at that moment?
4. Are we treating observed weather as if it were a forecast? (Usually yes, by accident.)

---

## Rules for adding a dataset

Before a new dataset enters the course it must have, in this file: verified source URL,
licence, target, unit of observation, time semantics, known limitations, and retrieval
method. No secrets, no personal data, no restricted data, no large raw files in git.
