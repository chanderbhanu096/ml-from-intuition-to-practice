"""Build the animated figures that the chapters embed in their markdown cells.

    python scripts/build_animations.py            # every chapter
    python scripts/build_animations.py 05-11      # one chapter

Animations are written to assets/<module>/<chapter>/ and referenced from markdown
with a plain <img> tag, so they render in Jupyter, on GitHub and in nbconvert's
HTML without the reader executing anything. They are built once, here, and
committed; the notebooks never generate them.

Two formats, chosen by what is being shown:

  .gif  for anything driven by data - a fitted curve improving, an error curve
        drawing itself. Written by matplotlib's Pillow writer.
  .svg  for schematics - boxes, arrows, things appearing in an order. Hand
        written with SMIL, a few kilobytes, and sharp at any zoom.

Keep each GIF under about 400 KB. The lever that matters is the frame count,
then the figure size; dpi below 80 makes the text soft.
"""

import sys
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt                                   # noqa: E402
import numpy as np                                                # noqa: E402
import pandas as pd                                               # noqa: E402
from matplotlib.animation import FuncAnimation, PillowWriter      # noqa: E402
from matplotlib.colors import to_rgb                              # noqa: E402
from sklearn.model_selection import train_test_split              # noqa: E402
from sklearn.tree import DecisionTreeRegressor                    # noqa: E402

ROOT = Path(__file__).resolve().parents[1]
GREY, BLUE, GREEN, RED, DARK = "#b0b0b0", "#2c5f9e", "#1f6f4a", "#c0392b", "#333333"


def _save(animation, relpath, fps):
    out = ROOT / relpath
    out.parent.mkdir(parents=True, exist_ok=True)
    animation.save(out, writer=PillowWriter(fps=fps))
    plt.close("all")
    print("wrote %s (%.0f KB)" % (relpath, out.stat().st_size / 1024))


def _write_text(text, relpath):
    out = ROOT / relpath
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(text.strip() + "\n")
    print("wrote %s (%.0f KB)" % (relpath, out.stat().st_size / 1024))


# ---------------------------------------------------------------- 05-11 data
def _curve_data():
    """The same 400 rows the 05-11 notebook builds, so the animation and the
    chapter's static figures are showing one dataset and not two."""
    def true_curve(x):
        return np.sin(1.2 * x) * 3 + 0.5 * x

    rng = np.random.default_rng(7)
    x = rng.uniform(-4, 4, 400)
    y = true_curve(x) + rng.normal(0, 1.5, 400)
    fit_x, held_x, fit_y, held_y = train_test_split(x, y, test_size=0.5, random_state=0)
    return true_curve, fit_x, fit_y, held_x, held_y


def _boost_history(fit_x, fit_y, held_x, held_y, grid, rate, rounds, depth=2):
    """Run the loop once and keep what every frame needs: the fitted curve on a
    grid, and the training and held-out RMSE, after each round."""
    on_fit = np.full(len(fit_y), fit_y.mean())
    on_held = np.full(len(held_y), fit_y.mean())
    on_grid = np.full(len(grid), fit_y.mean())
    curves, residuals, train_rmse, held_rmse = [on_grid.copy()], [fit_y - on_fit], [], []
    train_rmse.append(float(np.sqrt(((fit_y - on_fit) ** 2).mean())))
    held_rmse.append(float(np.sqrt(((held_y - on_held) ** 2).mean())))
    for _ in range(rounds):
        tree = DecisionTreeRegressor(max_depth=depth, random_state=0).fit(
            fit_x.reshape(-1, 1), fit_y - on_fit)
        on_fit = on_fit + rate * tree.predict(fit_x.reshape(-1, 1))
        on_held = on_held + rate * tree.predict(held_x.reshape(-1, 1))
        on_grid = on_grid + rate * tree.predict(grid.reshape(-1, 1))
        curves.append(on_grid.copy())
        residuals.append(fit_y - on_fit)
        train_rmse.append(float(np.sqrt(((fit_y - on_fit) ** 2).mean())))
        held_rmse.append(float(np.sqrt(((held_y - on_held) ** 2).mean())))
    return curves, residuals, np.array(train_rmse), np.array(held_rmse)


def build_05_11():
    out_dir = "assets/05_regression/05-11"
    true_curve, fit_x, fit_y, held_x, held_y = _curve_data()
    grid = np.linspace(-4, 4, 300)

    # --- 1. the mechanism: the fit climbing while the residuals collapse -----
    frames = [0, 1, 2, 3, 4, 5, 6, 8, 10, 13, 16, 20, 25, 30, 40, 50, 60]
    curves, residuals, _, _ = _boost_history(fit_x, fit_y, held_x, held_y, grid,
                                             rate=0.3, rounds=max(frames))

    fig, (top, bottom) = plt.subplots(2, 1, figsize=(7.2, 6.0), sharex=True,
                                      gridspec_kw={"height_ratios": [1.35, 1]})
    top.scatter(fit_x, fit_y, s=11, color=GREY, zorder=1)
    top.plot(grid, true_curve(grid), lw=1.8, ls="--", color=DARK, zorder=2,
             label="the curve we are trying to find")
    fitted_line, = top.plot([], [], lw=2.6, color=GREEN, zorder=3, label="the ensemble so far")
    top.set_ylim(fit_y.min() - 1, fit_y.max() + 1)
    top.set_ylabel("y")
    top.legend(loc="upper left", fontsize=9)
    # a full-length placeholder, so tight_layout reserves the room the titles need
    round_text = top.set_title("round 60 of 60  -  learning rate 0.30, depth-2 trees")

    residual_dots = bottom.scatter(fit_x, residuals[0], s=11, color=RED)
    bottom.axhline(0, color=DARK, lw=1.2)
    bottom.set_ylim(-9, 9)
    bottom.set_xlabel("x")
    bottom.set_ylabel("what is left over")
    residual_text = bottom.set_title("the residuals the next tree will be fitted to  (spread 0.00)")
    fig.tight_layout()

    def draw(index):
        step = frames[index]
        fitted_line.set_data(grid, curves[step])
        residual_dots.set_offsets(np.column_stack([fit_x, residuals[step]]))
        round_text.set_text("round %d of 60  -  learning rate 0.30, depth-2 trees" % step)
        residual_text.set_text("the residuals the next tree will be fitted to  "
                               "(spread %.2f)" % residuals[step].std())
        return fitted_line, residual_dots

    _save(FuncAnimation(fig, draw, frames=len(frames), blit=False, repeat=True),
          out_dir + "/boosting_rounds.gif", fps=1.6)

    # --- 2. the warning: wigglier and wigglier while the red line turns ------
    frames = [1, 2, 4, 7, 12, 20, 33, 55, 90, 150, 250, 400, 600, 800]
    curves, _, train_rmse, held_rmse = _boost_history(fit_x, fit_y, held_x, held_y, grid,
                                                      rate=0.1, rounds=max(frames))
    best = int(np.argmin(held_rmse))

    fig, (left, right) = plt.subplots(1, 2, figsize=(10.6, 4.3))
    left.scatter(fit_x, fit_y, s=10, color=GREY, zorder=1)
    left.plot(grid, true_curve(grid), lw=1.8, ls="--", color=DARK, zorder=2)
    wiggly_line, = left.plot([], [], lw=2.4, color=GREEN, zorder=3)
    left.set_ylim(fit_y.min() - 1, fit_y.max() + 1)
    left.set_xlabel("x")
    left.set_ylabel("y")
    left_title = left.set_title("")

    right.plot(np.arange(len(train_rmse)), train_rmse, lw=1.2, color="#dddddd")
    right.plot(np.arange(len(held_rmse)), held_rmse, lw=1.2, color="#f0d0cc")
    train_line, = right.plot([], [], lw=2.2, color=BLUE, label="training")
    held_line, = right.plot([], [], lw=2.2, color=RED, label="held out")
    here = right.scatter([], [], s=55, color=RED, zorder=5)
    right.axvline(best, color=GREEN, lw=1.4, ls="--")
    right.text(best * 1.35, 2.45, "best round: %d" % best, fontsize=9, color=GREEN)
    right.set_xscale("log")
    right.set_xlim(1, 800)
    right.set_ylim(0.3, 2.7)
    right.set_xlabel("round (log scale)")
    right.set_ylabel("RMSE")
    right.legend(loc="lower left", fontsize=9)
    right.set_title("the training error never warns you")
    fig.tight_layout()

    def draw(index):
        step = frames[index]
        wiggly_line.set_data(grid, curves[step])
        left_title.set_text("round %d  -  learning rate 0.10" % step)
        span = np.arange(step + 1)
        train_line.set_data(span, train_rmse[:step + 1])
        held_line.set_data(span, held_rmse[:step + 1])
        here.set_offsets([[max(step, 1), held_rmse[step]]])
        return wiggly_line, train_line, held_line, here

    _save(FuncAnimation(fig, draw, frames=len(frames), blit=False, repeat=True),
          out_dir + "/overfitting.gif", fps=1.3)

    # --- 3. the schematic, as an animated SVG -------------------------------
    _write_text(_forest_vs_boosting_svg(), out_dir + "/forest_vs_boosting.svg")


def _forest_vs_boosting_svg():
    """Four trees appearing at once on the left, one after another on the right.

    SMIL rather than CSS, because SMIL keeps animating when the file is loaded
    through an <img> tag and CSS animations in an external SVG do not always.
    """
    cycle = 8.0
    parts = []
    for index in range(4):
        x = 30 + index * 105
        # the forest: all four fade in together, then hold
        parts.append(
            '<g opacity="0"><rect x="%d" y="150" width="86" height="46" rx="4" fill="#fff" '
            'stroke="%s" stroke-width="2"/>'
            '<text x="%d" y="178" text-anchor="middle" font-size="14" fill="%s">tree %d</text>'
            '<animate attributeName="opacity" values="0;1;1;1" keyTimes="0;0.14;0.9;1" '
            'dur="%.1fs" repeatCount="indefinite"/></g>'
            % (x, BLUE, x + 43, BLUE, index + 1, cycle))
    forest = "".join(parts)

    parts = []
    for index in range(4):
        x = 30 + index * 105
        start = 0.06 + index * 0.19          # each waits for the one before it
        parts.append(
            '<g opacity="0"><rect x="%d" y="150" width="86" height="46" rx="4" fill="#fff" '
            'stroke="%s" stroke-width="2"/>'
            '<text x="%d" y="172" text-anchor="middle" font-size="14" fill="%s">tree %d</text>'
            '<text x="%d" y="188" text-anchor="middle" font-size="10" fill="%s">%s</text>'
            '<animate attributeName="opacity" values="0;0;1;1;1" '
            'keyTimes="0;%.2f;%.2f;0.94;1" dur="%.1fs" repeatCount="indefinite"/></g>'
            % (x, GREEN, x + 43, GREEN, index + 1, x + 43, GREEN,
               "the first guess" if index == 0 else "fixes tree %d" % index,
               start, start + 0.06, cycle))
        if index < 3:
            parts.append(
                '<g opacity="0"><line x1="%d" y1="173" x2="%d" y2="173" stroke="%s" '
                'stroke-width="2" marker-end="url(#tip)"/>'
                '<animate attributeName="opacity" values="0;0;1;1;1" '
                'keyTimes="0;%.2f;%.2f;0.94;1" dur="%.1fs" repeatCount="indefinite"/></g>'
                % (x + 88, x + 101, GREEN, start + 0.10, start + 0.16, cycle))
    boosting = "".join(parts)

    return '''
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 900 260" width="900" height="260"
     font-family="-apple-system, Segoe UI, Helvetica, Arial, sans-serif">
  <defs>
    <marker id="tip" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="5" markerHeight="5"
            orient="auto"><path d="M0,0 L10,5 L0,10 z" fill="%(green)s"/></marker>
  </defs>
  <!-- an explicit white ground: the notebook may be on a dark theme, and dark
       grey text on a transparent background disappears there -->
  <rect width="900" height="260" fill="#ffffff"/>

  <text x="225" y="34" text-anchor="middle" font-size="17" fill="%(blue)s">A forest</text>
  <text x="225" y="56" text-anchor="middle" font-size="12" fill="%(dark)s">all at once, then averaged</text>
  <text x="675" y="34" text-anchor="middle" font-size="17" fill="%(green)s">Boosting</text>
  <text x="675" y="56" text-anchor="middle" font-size="12" fill="%(dark)s">one at a time, each fixing the last</text>
  <line x1="450" y1="20" x2="450" y2="240" stroke="#dddddd" stroke-width="1"/>

  <g transform="translate(-15,0)">%(forest)s</g>
  <g transform="translate(435,0)">%(boosting)s</g>

  <text x="225" y="228" text-anchor="middle" font-size="12" fill="%(blue)s">
    shuffle them and nothing changes</text>
  <text x="675" y="228" text-anchor="middle" font-size="12" fill="%(green)s">
    shuffle them and the model is meaningless</text>
</svg>
''' % {"forest": forest, "boosting": boosting, "blue": BLUE, "green": GREEN, "dark": DARK}


SPLIT_SVG = r"""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 900 300" width="900" height="300"
     font-family="-apple-system, Segoe UI, Helvetica, Arial, sans-serif">
  <rect width="900" height="300" fill="#ffffff"/>
  <defs>
    <marker id="tip2" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="5" markerHeight="5"
            orient="auto"><path d="M0,0 L10,5 L0,10 z" fill="%(blue)s"/></marker>
    <marker id="tip3" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="5" markerHeight="5"
            orient="auto"><path d="M0,0 L10,5 L0,10 z" fill="%(green)s"/></marker>
  </defs>

  <text x="450" y="28" text-anchor="middle" font-size="16" fill="%(dark)s">20,640 rows, split once, before looking at anything</text>

  <rect x="40" y="50" width="480" height="34" rx="4" fill="#eef3f9" stroke="%(blue)s" stroke-width="2"/>
  <text x="280" y="72" text-anchor="middle" font-size="13" fill="%(blue)s">fit  -  12,384 rows  -  the model learns from these</text>
  <rect x="528" y="50" width="160" height="34" rx="4" fill="#eef7f1" stroke="%(green)s" stroke-width="2"/>
  <text x="608" y="72" text-anchor="middle" font-size="13" fill="%(green)s">watch  -  4,128</text>
  <rect x="696" y="50" width="164" height="34" rx="4" fill="#fdeeec" stroke="%(red)s" stroke-width="2"/>
  <text x="778" y="72" text-anchor="middle" font-size="13" fill="%(red)s">test  -  4,128</text>

  <path d="M 280 92 C 280 132, 608 132, 608 92" fill="none" stroke="%(blue)s" stroke-width="2"
        marker-end="url(#tip2)"/>
  <rect x="408" y="117" width="72" height="15" fill="#ffffff"/>
  <text x="444" y="129" text-anchor="middle" font-size="12" fill="%(blue)s">fit a model</text>
  <path d="M 608 150 C 608 196, 280 196, 280 150" fill="none" stroke="%(green)s" stroke-width="2"
        marker-end="url(#tip3)"/>
  <text x="444" y="208" text-anchor="middle" font-size="12" fill="%(green)s">score it, change something, go again</text>
  <circle r="7" fill="%(blue)s">
    <animateMotion dur="%(cycle).1fs" repeatCount="indefinite"
      path="M 280 92 C 280 132, 608 132, 608 92 L 608 150 C 608 196, 280 196, 280 150 Z"/>
  </circle>

  <g>
    <rect x="696" y="98" width="164" height="104" rx="6" fill="#ffffff" stroke="%(red)s"
          stroke-width="2" stroke-dasharray="6 4"/>
    <text x="778" y="128" text-anchor="middle" font-size="12.5" fill="%(red)s">SEALED</text>
    <text x="778" y="150" text-anchor="middle" font-size="11" fill="%(red)s">not looked at,</text>
    <text x="778" y="167" text-anchor="middle" font-size="11" fill="%(red)s">not fitted on,</text>
    <text x="778" y="184" text-anchor="middle" font-size="11" fill="%(red)s">not tuned against</text>
    <animate attributeName="opacity" values="1;1;1;0" keyTimes="0;0.78;0.86;1"
             dur="%(cycle).1fs" repeatCount="indefinite"/>
  </g>
  <g opacity="0">
    <rect x="696" y="98" width="164" height="104" rx="6" fill="#fdeeec" stroke="%(red)s" stroke-width="2"/>
    <text x="778" y="138" text-anchor="middle" font-size="13" fill="%(red)s">opened once</text>
    <text x="778" y="162" text-anchor="middle" font-size="13" fill="%(red)s">RMSE 0.4574</text>
    <text x="778" y="184" text-anchor="middle" font-size="11" fill="%(red)s">and never again</text>
    <animate attributeName="opacity" values="0;0;1;1" keyTimes="0;0.86;0.92;1"
             dur="%(cycle).1fs" repeatCount="indefinite"/>
  </g>

  <text x="450" y="252" text-anchor="middle" font-size="12.5" fill="%(dark)s">
    Every choice you make - which model, which depth, how many rounds - is paid for out of the green box.</text>
  <text x="450" y="276" text-anchor="middle" font-size="12.5" fill="%(dark)s">
    The red box buys one number, at the end, and buys nothing else.</text>
</svg>
"""


# ---------------------------------------------------------------- 05-12 data
def _california():
    """The same split 05-12 makes: 80% train, of which a quarter is held back to
    choose between models, and a 20% test set opened exactly once."""
    from sklearn.datasets import fetch_california_housing
    from sklearn.model_selection import train_test_split as split
    frame = fetch_california_housing(as_frame=True).frame
    features = [c for c in frame.columns if c != "MedHouseVal"]
    train, test = split(frame, test_size=0.2, random_state=0)
    fit, watch = split(train, test_size=0.25, random_state=0)
    return features, fit, watch, test


def build_05_12():
    from sklearn.dummy import DummyRegressor
    from sklearn.ensemble import HistGradientBoostingRegressor, RandomForestRegressor
    from sklearn.linear_model import LinearRegression
    from sklearn.tree import DecisionTreeRegressor

    out_dir = "assets/05_regression/05-12"
    features, fit, watch, test = _california()
    CAP = 5.00001

    # --- 1. the ladder, and the one part of it that never improves ----------
    ladder = [
        ("the mean of the training target", DummyRegressor(strategy="mean")),
        ("linear regression", LinearRegression()),
        ("one tree, depth 8", DecisionTreeRegressor(max_depth=8, random_state=0)),
        ("a forest of 200 trees", RandomForestRegressor(n_estimators=200, random_state=0,
                                                        n_jobs=-1)),
        ("boosting, 400 rounds", HistGradientBoostingRegressor(max_iter=400, learning_rate=0.1,
                                                               random_state=0)),
    ]
    shown = test.sample(2500, random_state=1)
    actual = shown["MedHouseVal"].to_numpy()
    capped = actual >= CAP - 1e-9
    predictions, scores = [], []
    for _, model in ladder:
        model.fit(fit[features], fit["MedHouseVal"])
        guess = model.predict(shown[features])
        predictions.append(guess)
        scores.append(float(np.sqrt(((actual - guess) ** 2).mean())))

    fig, ax = plt.subplots(figsize=(6.6, 6.0))
    ax.plot([0, 5.5], [0, 5.5], lw=1.6, ls="--", color=DARK, zorder=1)
    loose = ax.scatter([], [], s=8, color=GREY, zorder=2,
                       label="{:,} ordinary rows".format((~capped).sum()))
    stuck = ax.scatter([], [], s=16, color=RED, zorder=3,
                       label="{:,} rows recorded at the ceiling".format(capped.sum()))
    ax.axhline(5.0, lw=1.2, color=RED, alpha=0.45, zorder=1)
    ax.text(0.12, 5.09, "nothing above this line was ever recorded", fontsize=9, color=RED)
    ax.set_xlim(0, 5.6)
    ax.set_ylim(0, 5.8)
    ax.set_xlabel("prediction (100,000s of dollars)")
    ax.set_ylabel("the value recorded for the block group")
    ax.legend(loc="lower right", fontsize=9)
    title = ax.set_title("the mean of the training target - RMSE 0.0000")
    fig.tight_layout()

    def draw(step):
        # one frame per model, held a long time - Pillow collapses identical
        # consecutive GIF frames, so repeating a frame to slow it down does nothing
        guess = predictions[step]
        loose.set_offsets(np.column_stack([guess[~capped], actual[~capped]]))
        stuck.set_offsets(np.column_stack([guess[capped], actual[capped]]))
        title.set_text("%s - RMSE %.4f" % (ladder[step][0], scores[step]))
        return loose, stuck

    _save(FuncAnimation(fig, draw, frames=len(ladder), blit=False, repeat=True),
          out_dir + "/model_ladder.gif", fps=0.55)

    # --- 2. one number fanning out into the segments it was hiding ----------
    best = ladder[-1][1]
    error = best.predict(test[features]) - test["MedHouseVal"].to_numpy()
    overall = float(np.sqrt((error ** 2).mean()))

    at_cap = (test["MedHouseVal"] >= CAP - 1e-9).to_numpy()
    bands = pd.qcut(test["MedInc"], 5, labels=["lowest", "low", "middle", "high", "highest"])
    groups = [("not at\nthe ceiling", error[~at_cap], BLUE),
              ("AT THE\nCEILING", error[at_cap], RED)]
    for name in ["lowest", "low", "middle", "high", "highest"]:
        groups.append((name + "\nincome", error[(bands == name).to_numpy()], GREEN))
    heights = [float(np.sqrt((e ** 2).mean())) for _, e, _ in groups]

    # keep the pixel width even: 9.2in rounds to 919 px, and an odd-width buffer
    # comes out of the GIF writer sheared
    fig, ax = plt.subplots(figsize=(9.0, 4.8))
    positions = np.arange(len(groups)) + 1.0
    bars = ax.bar(np.zeros(len(groups)), np.full(len(groups), overall), width=0.72,
                  color=DARK)
    # the bars start stacked as one neutral column and take on their segment
    # colour as they separate, so frame one does not look like a segment already
    target_rgb = [np.array(to_rgb(c)) for _, _, c in groups]
    start_rgb = np.array(to_rgb("#8a8a8a"))
    ax.axhline(overall, lw=1.3, ls=":", color=DARK)
    ax.text(-0.6, max(heights) * 1.10, "the single number everyone quotes: %.4f" % overall,
            fontsize=10, color=DARK, ha="left")
    ax.set_xlim(-0.8, len(groups) + 0.7)
    ax.set_ylim(0, max(heights) * 1.2)
    ax.set_ylabel("RMSE on the test set")
    ax.set_xticks([])
    label_art = [ax.text(0, -0.02 * max(heights), "", ha="center", va="top", fontsize=8.5,
                         color=c) for _, _, c in groups]
    value_art = [ax.text(0, 0, "", ha="center", va="bottom", fontsize=8.5, color=c,
                         bbox=dict(boxstyle="round,pad=0.12", facecolor="white",
                                   edgecolor="none"))
                 for _, _, c in groups]
    ax.set_title("one test set, one model, seven honest answers")
    fig.subplots_adjust(bottom=0.18, top=0.9, left=0.08, right=0.98)

    def draw(frame):
        share = min(frame / 14.0, 1.0)
        share = share * share * (3 - 2 * share)              # ease in and out
        for index, bar in enumerate(bars):
            x = share * positions[index]
            height = overall + share * (heights[index] - overall)
            bar.set_x(x - bar.get_width() / 2)
            bar.set_height(height)
            bar.set_color(tuple(start_rgb + share * (target_rgb[index] - start_rgb)))
            label_art[index].set_position((x, -0.015 * max(heights)))
            value_art[index].set_position((x, height + 0.008))
            showing = "" if share < 0.55 else groups[index][0]
            label_art[index].set_text(showing)
            value_art[index].set_text("" if share < 0.55 else "%.3f" % heights[index])
        return bars

    _save(FuncAnimation(fig, draw, frames=20, blit=False, repeat=True),
          out_dir + "/segment_split.gif", fps=6)

    # --- 3. the three-way split, and what each part is allowed to do --------
    _write_text(_three_way_split_svg(), out_dir + "/three_way_split.svg")


def _three_way_split_svg():
    # The test set sits sealed while the other two are used over and over.
    return SPLIT_SVG % {"blue": BLUE, "green": GREEN, "red": RED, "dark": DARK, "cycle": 9.0}


BUILDERS = {"05-11": build_05_11, "05-12": build_05_12}


if __name__ == "__main__":
    wanted = sys.argv[1:] or sorted(BUILDERS)
    for chapter in wanted:
        if chapter not in BUILDERS:
            raise SystemExit("no animations defined for %s" % chapter)
        BUILDERS[chapter]()
