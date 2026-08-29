"""Run notebooks from a fresh kernel and report failures.

    python scripts/validate_notebooks.py                  # every notebook in the repo
    python scripts/validate_notebooks.py notebooks/00_orientation  # one folder
    python scripts/validate_notebooks.py path/to/one.ipynb

A notebook passes if it is valid JSON, executes top to bottom in a clean kernel with no
exception, and finishes inside the timeout. Execution happens in the notebook's own folder
so relative paths behave the same as they do for a learner.
"""

import sys
import time
from pathlib import Path

import nbformat
from nbclient import NotebookClient
from nbclient.exceptions import CellExecutionError

ROOT = Path(__file__).resolve().parents[1]
TIMEOUT = 600  # seconds per cell


def notebooks(args: list[str]) -> list[Path]:
    targets = [Path(a) for a in args] or [ROOT / "notebooks", ROOT / "solutions", ROOT / "assessments"]
    found: list[Path] = []
    for t in targets:
        t = t if t.is_absolute() else Path.cwd() / t
        found += [t] if t.is_file() else sorted(t.rglob("*.ipynb"))
    return [p for p in found if ".ipynb_checkpoints" not in p.parts]


def run(path: Path) -> tuple[bool, str, float]:
    start = time.time()
    try:
        nb = nbformat.read(path, as_version=4)
        NotebookClient(nb, timeout=TIMEOUT, kernel_name="python3", resources={"metadata": {"path": str(path.parent)}}).execute()
    except CellExecutionError as e:
        return False, str(e).strip().splitlines()[-1], time.time() - start
    except Exception as e:  # invalid JSON, missing kernel, timeout
        return False, f"{type(e).__name__}: {e}", time.time() - start
    return True, "", time.time() - start


def main() -> int:
    found = notebooks(sys.argv[1:])
    if not found:
        print("No notebooks found.")
        return 0
    failures = 0
    for path in found:
        ok, msg, secs = run(path)
        rel = path.relative_to(ROOT) if path.is_relative_to(ROOT) else path
        print(f"{'PASS' if ok else 'FAIL'}  {secs:5.1f}s  {rel}")
        if not ok:
            failures += 1
            print(f"      {msg}")
    print(f"\n{len(found) - failures}/{len(found)} passed")
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
