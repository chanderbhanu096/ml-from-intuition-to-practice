"""Download the Seoul bike sharing dataset into data/raw/ and print its real schema.

Run it yourself when you want the data:

    python scripts/get_seoul_bike.py

It downloads from the UCI Machine Learning Repository, never overwrites an existing file,
and prints what actually arrived so you can check the schema against data/README.md
instead of trusting it.
"""

import io
import sys
import urllib.request
import zipfile
from pathlib import Path

URL = "https://archive.ics.uci.edu/static/public/560/seoul+bike+sharing+demand.zip"
RAW = Path(__file__).resolve().parents[1] / "data" / "raw"


def main() -> int:
    RAW.mkdir(parents=True, exist_ok=True)
    existing = list(RAW.glob("*.csv"))
    if existing:
        print(f"Already have: {[p.name for p in existing]}\nDelete them first to re-download.")
    else:
        print(f"Downloading {URL}")
        with urllib.request.urlopen(URL, timeout=120) as r:
            blob = r.read()
        with zipfile.ZipFile(io.BytesIO(blob)) as z:
            print("Archive contains:", z.namelist())
            z.extractall(RAW)
        existing = list(RAW.glob("*.csv"))

    for path in existing:
        print(f"\n=== {path.name} ===")
        # The file is not UTF-8; UCI ships it in a Latin-1 style encoding.
        import pandas as pd

        df = pd.read_csv(path, encoding="cp1252")
        print("rows, columns:", df.shape)
        print("columns:", list(df.columns))
        print(df.dtypes.to_string())
        print(df.head(3).to_string())
        print("\nCheck these against data/README.md and correct the README if they differ.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
