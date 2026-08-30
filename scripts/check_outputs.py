"""Scan an EXECUTED notebook's outputs for signs of formatting mistakes.

Usage:  python scripts/check_outputs.py executed.ipynb [more.ipynb ...]

Catches things that execute cleanly but read wrongly:
  - a literal "%%" reaching the output (a print string with no % operator)
  - numpy scalar reprs leaking into printed text
  - "nan", "inf" or a negative zero appearing in output
"""
import json
import re
import sys

# Definite mistakes: these fail the check.
PATTERNS = [
    (re.compile(r"%%"), "literal '%%' in output - the print string has no % operator"),
    (re.compile(r"np\.(float|int|bool)\d*\("), "numpy scalar repr leaked into output"),
    (re.compile(r"-0\.0+\b"), "negative zero in output"),
]

# Worth a look, often deliberate (several chapters demonstrate NaN on purpose).
NOTES = [
    (re.compile(r"\b(nan|inf|-inf)\b"), "nan/inf in output - intended?"),
]


def scan(path):
    notebook = json.load(open(path))
    problems, notes = [], []
    for index, cell in enumerate(notebook["cells"]):
        if cell["cell_type"] != "code":
            continue
        text = ""
        for output in cell.get("outputs", []):
            if output["output_type"] == "stream":
                text += "".join(output["text"])
            elif "text/plain" in output.get("data", {}):
                text += "".join(output["data"]["text/plain"])
            elif output["output_type"] == "error":
                problems.append((index, "ERROR: %s: %s" % (output["ename"], output["evalue"])))
        for pattern, message in PATTERNS:
            if pattern.search(text):
                problems.append((index, message))
        for pattern, message in NOTES:
            if pattern.search(text):
                notes.append((index, message))
    return problems, notes


if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    total, note_count = 0, 0
    for path in sys.argv[1:]:
        found, notes = scan(path)
        total += len(found)
        note_count += len(notes)
        for index, message in found:
            print("FAIL %s  cell %d: %s" % (path, index, message))
        for index, message in notes:
            print("note %s  cell %d: %s" % (path, index, message))
    print("clean" if total == 0 else "%d issue(s)" % total, "(%d note(s))" % note_count)
    sys.exit(1 if total else 0)
