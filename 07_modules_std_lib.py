"""
Import Modules and Exploring the Standard Library
=================================================
Corey Schafer - Python Tutorial for Beginners #9

Covers:
    * The different import styles and how to pick one
    * How Python finds modules (sys.path)
    * A quick tour of useful standard-library modules:
      random, math, datetime, calendar, os

Run (from this folder, so that my_module.py can be found):
    python 07_modules_std_lib.py
"""

# ---------------------------------------------------------------------------
# Import styles
# ---------------------------------------------------------------------------
# import my_module                  -> use as my_module.find_index(...)
# import my_module as mm            -> use as mm.find_index(...)
# from my_module import find_index  -> use as find_index(...)
# from my_module import *           -> imports EVERYTHING; avoid, it hides
#                                      where names came from
import calendar
import datetime
import math
import os
import random
import sys

from my_module import find_index, test

# import antigravity   # an easter egg: opens an xkcd comic in your browser

courses = ["History", "Math", "Physics", "Compsci"]

# ---------------------------------------------------------------------------
# Using our own module
# ---------------------------------------------------------------------------
index = find_index(courses, "History")
print(index)  # 0
print(test)  # Test string

# Python searches these directories, in order, when it imports a module.
# The script's own directory is always first, which is how my_module is found.
# Uncomment to inspect:
# print(sys.path)

# ---------------------------------------------------------------------------
# Standard-library tour
# ---------------------------------------------------------------------------
# random: pick a random item
random_course = random.choice(courses)
print(random_course)

# math: trigonometry and friends (angles are in radians)
rads = math.radians(90)
print(rads)  # 1.5707963267948966
print(math.sin(rads))  # 1.0

# datetime: dates and times
today = datetime.date.today()
print(today)  # e.g. 2026-10-23

# calendar: calendar maths
print(calendar.isleap(2017))  # False

# os: talk to the operating system
print(os.getcwd())  # current working directory
print(os.__file__)  # where the os module itself lives on disk


"""
Expected output (random course, date and paths will differ)
-----------------------------------------------------------
Imported my_module
0
Test string
Compsci
1.5707963267948966
1.0
2026-10-23
False
/path/to/python-fundamentals-corey-schafer
/path/to/python3.x/os.py
"""
