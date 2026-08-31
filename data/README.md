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

## 3a. California housing (1990 US census) - used in 02-08 and 05-12

**Status:** fetched by `sklearn.datasets.fetch_california_housing`, cached in `~/scikit_learn_data`
(about 360 KB). **Not committed to this repository.** The first call needs a network connection;
later calls are offline.

| Field | Value |
|---|---|
| **Source** | StatLib, Carnegie Mellon: `https://lib.stat.cmu.edu/datasets/houses.zip` |
| **Reference** | Pace, R. Kelley and Ronald Barry, *Sparse Spatial Autoregressions*, Statistics and Probability Letters 33:291-297, 1997 |
| **Origin** | Derived from the 1990 United States census |
| **Licence** | **Not stated.** No licence accompanies the file. The underlying 1990 census aggregates are US federal government output; the derived file's terms are unknown. Verify before any use outside coursework |
| **Unit of observation** | One census block group - the smallest area for which the Census Bureau publishes sample data, typically 600-3,000 people |
| **Rows / columns** | 20,640 rows, 8 features and 1 target, all numeric |
| **Censoring (verified 2026-09-01)** | **The target is capped.** 965 rows (4.68%) sit at exactly 5.00001, the file's maximum, against 32 rows in the whole band from 4.9 to 5.0. `HouseAge` is capped the same way: 1,025 training rows at exactly 52 against 41 at 51. Anything above either limit was recorded at the limit, so those values are bounds and not measurements. 05-12 is built on this |
| **Target** | `MedHouseVal` - median house value for the block group, in hundreds of thousands of dollars |
| **Time meaning** | None. A single 1990 snapshot; no dates, no seasonality, no ordering |
| **Retrieval** | `fetch_california_housing(as_frame=True).frame` |

**Verified limitations** (each one established by executed code in 02-08, not assumed):

1. A row is a block group, not a house or a household. The target is already a median over houses,
   so a model fitted here predicts an area's median and never a house price.
2. Three different denominators appear in one row: per block group (`Population`), per household
   (`MedInc`, `AveRooms`, `AveBedrms`, `AveOccup`), per house (`MedHouseVal`).
3. `MedHouseVal` is censored at $500,001 - 965 rows, 4.68% - and the censored rows are the richest
   block groups (mean `MedInc` 7.83 against 3.68). No model trained here can predict above the cap,
   and any mean of the target is an underestimate.
4. `HouseAge` is censored at 52 (1,273 rows, 6.17%); `MedInc` at 15.0001 (49 rows).
5. 79 rows have `AveRooms > 20` or `AveOccup > 20`, produced by block groups with very few
   households or by group quarters. Leaving them in suppresses two relationships: r(`AveOccup`,
   target) is -0.024 with them and -0.242 without; r(`AveRooms`, target) is 0.152 and 0.274.
6. No city or region column. Pooled correlations can reverse within regions: r(`HouseAge`, target) is
   +0.106 statewide but negative in six of eight geographic clusters.
7. No missing values and no duplicate rows. This is stated because it is true and because it is not
   reassuring - every defect above survives both checks.
8. The documentation does not say how house value was measured (self-reported, assessed, or from
   sales).
9. 1990, California only. Geographic patterns in US housing value of this era reflect historical
   policy including mortgage redlining; module 13 returns to what that means for building on it.

---

## 4. Named public datasets - chosen per chapter

**Policy (D-14):** each chapter uses whichever dataset shows its idea most clearly. There is no
single recurring case study, because several methods only reveal their character on data with the
right shape - class imbalance, heavy tails, genuine clusters, a real seasonal cycle, text.

**The rule that does not move:** before a dataset is used anywhere in this course, this file must
record its verified source, licence, target, unit of observation, time semantics, known limitations
and retrieval method. A dataset with no entry here is not used.

---

## 5. Seoul bike sharing demand - available, no longer required

**Status in this repository: NOT PRESENT, and nothing depends on it.** Since D-14 no chapter
requires this dataset; it remains documented because it is a good fit for demand forecasting if you
want it.

**Original status note:** No file has been downloaded, so nothing below
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

## 6. Rules for adding a dataset

Before a new dataset enters the course it must have, in this file: verified source URL,
licence, target, unit of observation, time semantics, known limitations, and retrieval
method. No secrets, no personal data, no restricted data, no large raw files in git.
