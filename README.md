# Machine Learning, From Intuition to Practice

A chapter-by-chapter machine learning course in Jupyter notebooks, written for someone
who knows a little Python and nothing about ML.

The goal is **not** to memorise algorithms. The goal is that when you meet a problem
nobody has shown you before - in an exam, an interview, a bug, or a real project - you
already know which questions to ask:

> What is the actual problem? Is machine learning even the right tool?
> What does one row represent? What is the target? What will I actually know at
> prediction time? What is the simplest baseline? How should I split the data?
> Is there leakage? Which metric matches the real cost of a mistake? Which model family
> fits? Am I underfitting or overfitting? Where does the model fail? What do I try next?
> How honest am I being about uncertainty?

## How the course teaches

Every important idea is built in the same order:

1. a familiar human situation
2. a tiny table of 3-10 rows you can hold in your head
3. a prediction you make **before** running the code
4. a picture
5. one example worked out by hand, with real numbers
6. the notation, introduced only after the numbers
7. a small from-scratch implementation, when it helps
8. the standard library version
9. a realistic dataset
10. a **failure lab** where the method is deliberately broken, and diagnosed

Maths grows slowly, on a ladder from counting to gradients. No formula appears before
the numbers it summarises.

## Start here

New to the repo: read [GETTING_STARTED.md](GETTING_STARTED.md), then open
[notebooks/00_orientation/00-01_start_here.ipynb](notebooks/00_orientation/00-01_start_here.ipynb).

| File | What it is for |
|---|---|
| [GETTING_STARTED.md](GETTING_STARTED.md) | Install and run your first notebook |
| [CURRICULUM.md](CURRICULUM.md) | Every chapter, in order, with prerequisites |
| [PROGRESS.md](PROGRESS.md) | What is built, what is validated, what is next |
| [GLOSSARY.md](GLOSSARY.md) | Plain-language definitions of terms already introduced |
| [DECISIONS.md](DECISIONS.md) | Why this course chose these datasets, tools and orderings |
| [curriculum.yml](curriculum.yml) | The same chapter list, machine-readable |
| [data/README.md](data/README.md) | Every dataset: source, licence, target, unit of observation |

## Layout

```
notebooks/     the learner notebooks, grouped by module, numbered in learning order
solutions/     full worked solutions, mirroring the notebooks/ tree
assessments/   cumulative end-of-module assessments
data/          dataset documentation and (locally) raw files - raw data is not committed
scripts/       validation and dataset-download helpers
_template/     the notebook template every chapter follows
```

Notebook files are named `MM-CC_slug.ipynb`: module number, chapter number inside the
module, so the learning order is the sort order.

## Rules this course holds itself to

- one central idea per notebook, 30-60 minutes
- every notebook runs top to bottom from a fresh kernel (`scripts/validate_notebooks.py`)
- preprocessing is fitted on training data only; the test set is untouched until the end
- every model is compared against a baseline that a non-ML person could have built
- no claim that one model is universally best
- synthetic data is always labelled as synthetic
