# Python Fundamentals — Corey Schafer Tutorial Notes

Annotated, runnable notes from working through [Corey Schafer's](https://www.youtube.com/@coreyms)
Python beginner and intermediate tutorial series. Every script is self-contained,
heavily commented, and ends with the expected output so you can read it like a
worked example without running it.

## Contents

| # | File | Topic |
|---|------|-------|
| 01 | [`01_strings_text_data.py`](01_strings_text_data.py) | Strings: indexing, slicing, methods, f-strings, `dir()` / `help()` |
| 02 | [`02_numeric_data.py`](02_numeric_data.py) | Integers and floats: arithmetic, `//`, `**`, `%`, `round()`, casting |
| 03 | [`03_lists_tuples_sets.py`](03_lists_tuples_sets.py) | Lists, tuples, sets: methods, mutability, aliasing, set algebra |
| 04 | [`04_dictionaries.py`](04_dictionaries.py) | Dicts: `[]` vs `.get()`, `update`, `pop`, `del`, iterating `.items()` |
| 05 | [`05_conditionals_booleans.py`](05_conditionals_booleans.py) | `if` / `elif` / `else`, `==` vs `is`, `and` / `or` / `not`, truthiness |
| 06 | [`06_functions.py`](06_functions.py) | Functions, default args, `*args` / `**kwargs`, unpacking into calls |
| 07 | [`07_modules_std_lib.py`](07_modules_std_lib.py) | Import styles, `sys.path`, tour of `random`, `math`, `datetime`, `calendar`, `os` |
| 08 | [`08_try_except.py`](08_try_except.py) | `try` / `except` / `else` / `finally`, specific vs generic handlers, `raise` |
| 09 | [`09_csv_files.py`](09_csv_files.py) | `csv.reader` / `writer` / `DictReader` / `DictWriter`, custom delimiters |
| 10 | [`10_json_data.py`](10_json_data.py) | `json.load(s)` / `dump(s)`, pretty-printing, fetching JSON from a web API |
| 11 | [`11_slicing_lists_strings.py`](11_slicing_lists_strings.py) | `[start:stop:step]`, negative indexes, reversing with `[::-1]` |
| 12 | [`12_comprehensions.py`](12_comprehensions.py) | List / dict / set comprehensions and generator expressions |
| 13 | [`13_sorting.py`](13_sorting.py) | `sorted()` vs `.sort()`, `key=`, sorting objects with lambda / `attrgetter` |
| 14 | [`14_sets.py`](14_sets.py) | Set methods: `add`, `update`, `discard`, intersection / difference / symmetric difference |
| 15 | [`15_generators.py`](15_generators.py) | `yield`, generator objects, `next()`, memory benefits |
| 16 | [`16_itertools.py`](16_itertools.py) | `count`, `cycle`, `repeat`, combinatorics, `chain`, `islice`, `groupby`, `tee`, … |

Supporting files:

- `my_module.py` — tiny module imported by `07_modules_std_lib.py`
- `data/` — input files used by the scripts (`names.csv`, `states.json`, `test.log`, …)
- `output/` — created at runtime by scripts 09 and 10; ignored by git

## Running

Requires Python 3.6+ (f-strings). No third-party packages.

```bash
git clone https://github.com/Vaishnvi/python-fundamentals-corey-schafer.git
cd python-fundamentals-corey-schafer
python 01_strings_text_data.py
```

Scripts resolve their data paths relative to their own location, so they can be
run from any working directory. The only exception is `07_modules_std_lib.py`,
which imports `my_module.py` and therefore needs to be run from the repo root
(or with the repo root on `PYTHONPATH`).

`10_json_data.py` makes one live request to the free
[Frankfurter](https://frankfurter.dev) exchange-rate API. If you are offline it
prints a message and skips that section instead of failing.

## Conventions used in the notes

- A module docstring at the top of each file summarises what the lesson covers.
- `# ----` banners separate the sub-topics within a lesson.
- Inline `# ...` comments on a line show the value that line prints.
- A closing docstring reproduces the expected output (long outputs are abridged).
