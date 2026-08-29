# Getting started

You need about ten minutes and roughly 700 MB of disk.

## 1. Check your Python

You need Python 3.10, 3.11 or 3.12. In a terminal:

```bash
python3 --version
```

If that prints 3.13 or newer, or an error, install Python 3.11 (on macOS with Homebrew:
`brew install python@3.11`) and use `python3.11` instead of `python3` below.

## 2. Create an isolated environment

An environment is a private folder of libraries, so this course cannot break other
projects on your machine. From inside the `ml-course` folder:

```bash
python3.11 -m venv .venv
```

```bash
.venv/bin/pip install -r requirements.txt
```

## 3. Start Jupyter

```bash
.venv/bin/jupyter lab
```

Your browser opens a file list. Open
`notebooks/00_orientation/00-01_start_here.ipynb` and read from the top.

If you prefer VS Code: open this folder, open the notebook, and when VS Code asks for a
kernel choose the one inside `.venv`.

## 4. How to actually work through a notebook

- Run cells with **Shift+Enter**, in order, from the top.
- When a notebook says **Predict before running**, write your guess down before you run
  the cell. Being wrong on purpose is the fastest way to learn; skipping the guess is the
  slowest.
- Do the exercises before opening `solutions/`. The solutions explain reasoning, not just
  code, so they are worth reading even when you got the answer right.
- If a notebook misbehaves, restart the kernel and run from the top
  (*Kernel -> Restart Kernel and Run All Cells*). Notebooks in this course are written so
  that this always works; if it does not, that is a bug in the notebook.

## 5. Datasets

Small examples are built into the notebooks or generated as clearly-labelled synthetic
data, so you can start with no downloads at all. The one external dataset
(Seoul bike sharing) is documented in [data/README.md](data/README.md) with its source and
licence, and is only needed from module 02 onwards.

## 6. Checking a notebook runs (optional)

```bash
.venv/bin/python scripts/validate_notebooks.py notebooks/00_orientation/00-01_start_here.ipynb
```

Run with no arguments to check every notebook in the repo.
