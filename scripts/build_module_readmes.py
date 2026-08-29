"""Generate notebooks/<module>/README.md for every module, from curriculum.yml.

    python scripts/build_module_readmes.py

Chapter tables, status marks and hour counts are derived from curriculum.yml, so
re-running this after a chapter is completed keeps every module README current.
The prose lives in scripts/module_content.py.
"""

import sys
from pathlib import Path

import yaml

sys.path.insert(0, str(Path(__file__).parent))
from module_content import MODULE_PROSE, ONE_IDEA          # noqa: E402

ROOT = Path(__file__).resolve().parents[1]
LEVEL = {"core": "Core", "applied": "Applied", "optional": "Optional"}

# Algorithms and methods introduced by chapter, for the "what you will be able to run" table.
ALGORITHMS = {
    "00-01": ["`DummyRegressor` (the constant baseline)"],
    "04-02": ["`DummyRegressor`, `DummyClassifier`"],
    "05-02": ["Ordinary least squares, by hand and via `LinearRegression`"],
    "05-03": ["Multiple linear regression"],
    "05-06": ["Gradient descent, from scratch"],
    "05-07": ["`PolynomialFeatures`, interaction terms"],
    "05-09": ["`Ridge`, `Lasso`, `ElasticNet`"],
    "05-10": ["`DecisionTreeRegressor`, `RandomForestRegressor`"],
    "05-11": ["`HistGradientBoostingRegressor`"],
    "06-02": ["`LogisticRegression`"],
    "06-09": ["Platt scaling, isotonic regression (`CalibratedClassifierCV`)"],
    "06-10": ["`KNeighborsClassifier`, `GaussianNB`/`MultinomialNB`, `SVC` (linear and kernel)"],
    "06-11": ["`DecisionTreeClassifier`, `RandomForestClassifier`, `HistGradientBoostingClassifier`"],
    "06-12": ["One-vs-rest, one-vs-one, multilabel wrappers"],
    "07-06": ["Permutation importance, partial dependence"],
    "07-07": ["SHAP values"],
    "08-03": ["`KMeans`"],
    "08-04": ["`AgglomerativeClustering`, dendrograms"],
    "08-05": ["`DBSCAN`, `GaussianMixture`"],
    "08-07": ["`PCA`"],
    "08-08": ["`TSNE`, UMAP (discussed), `IsolationForest`, `LocalOutlierFactor`"],
    "09-06": ["Exponential smoothing (Holt-Winters)"],
    "09-07": ["ARIMA / SARIMA (literacy)"],
    "09-08": ["Supervised reframing with lag features; prediction intervals"],
    "10-04": ["A multilayer perceptron and backpropagation, from scratch in NumPy"],
    "10-05": ["PyTorch `nn.Module`, the training loop"],
    "10-07": ["SGD, Adam, weight decay, dropout, early stopping"],
    "10-09": ["Convolutional layers, pooling"],
    "10-10": ["Recurrent layers, attention"],
    "10-11": ["Self-attention, transformer blocks, embeddings"],
    "11-01": ["`CountVectorizer`, `TfidfVectorizer`"],
    "11-03": ["Pre-trained word/sentence embeddings"],
    "11-05": ["Transfer learning from a pre-trained vision model"],
    "11-06": ["Popularity baseline, content-based similarity, collaborative filtering, matrix factorisation"],
    "12-01": ["Pseudo-labelling, uncertainty sampling"],
    "12-02": ["`partial_fit` / `SGDClassifier`, drift detection"],
    "12-05": ["Epsilon-greedy and UCB bandits, tabular Q-learning"],
    "12-06": ["Message passing (intuition), federated averaging (intuition)"],
}


def render(module, chapters):
    mid, name = module["id"], module["name"]
    done = [c for c in chapters if c["status"] == "complete"]
    hours = sum(c["minutes"] for c in chapters) / 60
    intro, skip = MODULE_PROSE[mid]

    prereqs = sorted({p for c in chapters for p in c["prereqs"] if not p.startswith(mid)})
    levels = sorted({LEVEL[c["level"]] for c in chapters})

    out = [f"# Module {mid} · {name}", ""]
    out += [f"> {module['goal']}", ""]
    out += [f"**{len(done)} of {len(chapters)} chapters complete** · ~{hours:.0f} learner-hours · "
            f"{', '.join(levels)}", ""]
    out += ["---", "", "## What this module is for", "", intro, ""]

    out += ["## Before you start", ""]
    out += [f"- **Needs:** {', '.join(prereqs) if prereqs else 'nothing but the previous module'}"]
    unlocks = sorted({c2["id"] for m2 in ALL_MODULES for c2 in m2["chapters"]
                      for p in c2["prereqs"] if p.startswith(mid) and not c2["id"].startswith(mid)})
    out += [f"- **Unlocks:** {', '.join(unlocks) if unlocks else 'the end of the course'}"]
    out += [f"- **If you are short of time:** {skip}", ""]

    algos = [(c["id"], a) for c in chapters for a in ALGORITHMS.get(c["id"], [])]
    if algos:
        out += ["## Algorithms and methods introduced here", "",
                "| Chapter | What you will be able to run |", "|---|---|"]
        out += [f"| {cid} | {a} |" for cid, a in algos]
        out += [""]

    out += ["## Chapters", "",
            "| | Chapter | Level | Time | The one idea |", "|---|---|---|---|---|"]
    for c in chapters:
        tick = "x" if c["status"] == "complete" else " "
        link = f"[{c['id']}]({Path(c['path']).name})" if c["status"] == "complete" else c["id"]
        out += [f"| `[{tick}]` | **{link}** {c['title']} | {LEVEL[c['level']]} | {c['minutes']}m | "
                f"{ONE_IDEA.get(c['id'], '')} |"]
    out += [""]

    datasets = sorted({c["dataset"] for c in chapters})
    label = {"tiny": "hand-typed tables you can check with a pen", "synthetic": "generated data with a known truth",
             "sklearn": "datasets shipped with scikit-learn", "best_fit": "whichever dataset shows the idea most clearly",
             "seoul_bike": "Seoul bike sharing (see `data/README.md`)", "none": "no dataset"}
    out += ["## Data used", "",
            *[f"- {label.get(d, d)}" for d in datasets], "",
            "Synthetic data is always labelled **SYNTHETIC** in the notebook, and is used where knowing the",
            "true answer in advance is the only way to check whether a method finds it.", ""]

    solutions = f"../../solutions/{Path(module['dir']).name}/"
    out += ["## Where things are", "",
            f"- Learner notebooks: this folder",
            f"- Worked solutions: [`{solutions}`]({solutions})",
            "- Full curriculum with prerequisites: [`../../CURRICULUM.md`](../../CURRICULUM.md)",
            "- Terms introduced so far: [`../../GLOSSARY.md`](../../GLOSSARY.md)", "",
            "---", "",
            "*This file is generated by `scripts/build_module_readmes.py` from `curriculum.yml`. "
            "Edit the prose in `scripts/module_content.py` and re-run.*", ""]
    return "\n".join(out)


plan = yaml.safe_load((ROOT / "curriculum.yml").read_text())
ALL_MODULES = plan["modules"]

for module in ALL_MODULES:
    target = ROOT / module["dir"] / "README.md"
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(render(module, module["chapters"]))
    print("wrote", target.relative_to(ROOT))
