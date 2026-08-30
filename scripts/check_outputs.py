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

PATTERNS = [
    (re.compile(r"%%"), "literal '%%' in output - the print string has no % operator"),
    (re.compile(r"np\.(float|int|bool)\d*\("), "numpy scalar repr leaked into output"),
    (re.compile(r"\b-0\.0+\b"), "negative zero in output"),
    (re.compile(r"\b(nan|inf|-inf)\b"), "nan/inf in output"),
]


def scan(path):
    notebook = json.load(open(path))
    problems = []
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
    return problems


if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    total = 0
    for path in sys.argv[1:]:
        found = scan(path)
        total += len(found)
        for index, message in found:
            print("%s  cell %d: %s" % (path, index, message))
    print("clean" if total == 0 else "%d issue(s)" % total)
    sys.exit(1 if total else 0)
