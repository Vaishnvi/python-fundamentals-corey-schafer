"""
CSV Module - How to Read, Parse, and Write CSV Files
====================================================
Corey Schafer - Python Tutorial

Covers:
    * csv.reader  -> each row as a LIST, access columns by index
    * csv.writer  -> write rows from lists, with a custom delimiter
    * csv.DictReader -> each row as a DICT, access columns by header name
    * csv.DictWriter -> write rows from dicts, choosing which fields to keep

Input:   data/names.csv            (comma separated, header: first_name,last_name,email)
Outputs: output/new_names.csv      (same data, tab separated)
         output/new_names_no_email.csv

Run:
    python 09_csv_files.py
"""

import csv
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR / "data"
OUTPUT_DIR = BASE_DIR / "output"
OUTPUT_DIR.mkdir(exist_ok=True)

# NOTE: open CSV files with newline="" - the csv module handles line endings
# itself, and this prevents blank lines appearing between rows on Windows.

# ---------------------------------------------------------------------------
# 1. csv.reader - rows come back as lists
# ---------------------------------------------------------------------------
with open(DATA_DIR / "names.csv", "r", newline="") as csv_file:
    csv_reader = csv.reader(csv_file)

    next(csv_reader)  # skip the header row

    for line in csv_reader:
        print(line[2])  # third column -> email

# ---------------------------------------------------------------------------
# 2. csv.writer - copy the file using TAB as the delimiter
# ---------------------------------------------------------------------------
with open(DATA_DIR / "names.csv", "r", newline="") as csv_file:
    csv_reader = csv.reader(csv_file)

    with open(OUTPUT_DIR / "new_names.csv", "w", newline="") as new_file:
        csv_writer = csv.writer(new_file, delimiter="\t")

        for line in csv_reader:
            csv_writer.writerow(line)

# ---------------------------------------------------------------------------
# 3. Reading a file with a non-default delimiter
# ---------------------------------------------------------------------------
# If you forget delimiter="\t" here, each whole line is treated as ONE field.
with open(OUTPUT_DIR / "new_names.csv", "r", newline="") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter="\t")

    for line in csv_reader:
        print(line)

# ---------------------------------------------------------------------------
# 4. csv.DictReader - rows come back as dicts keyed by the header
# ---------------------------------------------------------------------------
# Much more readable than line[2]: the header row is consumed automatically.
with open(OUTPUT_DIR / "new_names.csv", "r", newline="") as csv_file:
    csv_reader = csv.DictReader(csv_file, delimiter="\t")

    for line in csv_reader:
        print(line["email"])

# ---------------------------------------------------------------------------
# 5. csv.DictWriter - write only the columns we care about
# ---------------------------------------------------------------------------
with open(DATA_DIR / "names.csv", "r", newline="") as csv_file:
    csv_reader = csv.DictReader(csv_file)

    with open(OUTPUT_DIR / "new_names_no_email.csv", "w", newline="") as new_file:
        field_names = ["first_name", "last_name"]
        csv_writer = csv.DictWriter(new_file, fieldnames=field_names, delimiter="\t")

        csv_writer.writeheader()  # DictWriter does NOT write the header for you

        for line in csv_reader:
            # DictWriter raises ValueError for keys not in `fieldnames`, so drop
            # the email column before writing the row.
            del line["email"]
            csv_writer.writerow(line)


"""
Expected output (abridged - 44 rows in each block)
--------------------------------------------------
john-doe@bogusemail.com
maryjacobs@bogusemail.com
...
['first_name', 'last_name', 'email']
['John', 'Doe', 'john-doe@bogusemail.com']
['Mary', 'Smith-Robinson', 'maryjacobs@bogusemail.com']
...
john-doe@bogusemail.com
maryjacobs@bogusemail.com
...
"""
