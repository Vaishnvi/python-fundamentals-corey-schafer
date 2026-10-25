"""
Using try / except Blocks for Error Handling
============================================
Corey Schafer - Python Tutorial for Beginners: Try/Except

The full structure is:

    try:        code that might raise an exception
    except:     runs ONLY if an exception was raised (most specific first)
    else:       runs ONLY if NO exception was raised
    finally:    ALWAYS runs - ideal for releasing resources (files, DB connections)

Covers:
    * Catching a specific exception vs a generic Exception
    * Order of except clauses matters (specific before generic)
    * The else and finally clauses
    * Raising your own exception

Run:
    python 08_try_except.py
"""

from pathlib import Path

# Resolve paths relative to this file so the script works from any directory.
DATA_DIR = Path(__file__).resolve().parent / "data"

# ---------------------------------------------------------------------------
# 1. Missing file -> FileNotFoundError is caught by the FIRST matching except
# ---------------------------------------------------------------------------
try:
    f = open(DATA_DIR / "does_not_exist.txt")
    # var = bad_var   # a NameError here would fall through to the generic except
except FileNotFoundError as e:
    # `as e` gives us the exception object so we can print the real message.
    print(e)
except Exception as e:
    # Generic catch-all. Must come AFTER the specific handlers, otherwise it
    # would swallow everything and the specific ones would never run.
    print(e)
else:
    print(f.read())
    f.close()
finally:
    # Runs no matter what - clean up resources here.
    print("Executing Finally ...")

# ---------------------------------------------------------------------------
# 2. File exists and nothing goes wrong -> the else branch runs
# ---------------------------------------------------------------------------
try:
    f = open(DATA_DIR / "test_file.txt")
except FileNotFoundError as e:
    print(e)
except Exception as e:
    print(e)
else:
    print(f.read())
    f.close()
finally:
    print("Executing Finally ...")

# ---------------------------------------------------------------------------
# 3. Raising our own exception
# ---------------------------------------------------------------------------
# The file opens fine, but we decide its contents are unacceptable and raise
# manually. The generic `except Exception` catches it.
try:
    f = open(DATA_DIR / "corrupt_file.txt")
    if f.name.endswith("corrupt_file.txt"):
        raise Exception
except FileNotFoundError as e:
    print(e)
except Exception:
    print("Error!")
else:
    print(f.read())
    f.close()
finally:
    print("Executing Finally ...")


"""
Expected output
---------------
[Errno 2] No such file or directory: '.../data/does_not_exist.txt'
Executing Finally ...
Test File Contents!

Executing Finally ...
Error!
Executing Finally ...
"""
