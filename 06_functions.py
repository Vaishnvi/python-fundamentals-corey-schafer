"""
Functions
=========
Corey Schafer - Python Tutorial for Beginners #8

Covers:
    * Defining functions and returning values
    * Positional vs keyword arguments and default values
    * *args and **kwargs for accepting any number of arguments
    * Unpacking a list/dict INTO a call with * and **
    * A small practical example: leap years and days in a month

Run:
    python 06_functions.py
"""


def hello_func(greeting, name="You"):
    """Return a greeting. `name` is optional and defaults to 'You'."""
    return f"{greeting}, {name}"


print(hello_func("Hello"))  # positional argument only -> default name
print(hello_func("Hello", name="Vaish"))  # keyword argument overrides the default


# ---------------------------------------------------------------------------
# *args and **kwargs
# ---------------------------------------------------------------------------
# *args   collects any extra POSITIONAL arguments into a tuple.
# **kwargs collects any extra KEYWORD arguments into a dict.
# The names `args` / `kwargs` are only a convention; the * and ** do the work.
def student_info(*args, **kwargs):
    print(args)  # tuple of positional values
    print(kwargs)  # dict of keyword names -> values


student_info("Math", "Art", name="John", age=22)

# Going the other way: unpack a list with * and a dict with ** when CALLING.
# Without the stars, the whole list would arrive as a single positional
# argument and the whole dict as a second one.
courses = ["Math", "Art"]
info = {"name": "John", "age": 22}

student_info(*courses, **info)


# ---------------------------------------------------------------------------
# Practical example: days in a month
# ---------------------------------------------------------------------------
# Index 0 is a placeholder so that month_days[1] is January, [2] February, ...
month_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


def is_leap(year):
    """Return True for leap years, False for non-leap years.

    A year is a leap year if it is divisible by 4, EXCEPT century years,
    which must also be divisible by 400 (so 1900 is not, but 2000 is).
    """
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


def days_in_month(year, month):
    """Return the number of days in `month` (1-12) of `year`."""
    if not 1 <= month <= 12:
        return "Invalid month"

    if month == 2 and is_leap(year):
        return 29

    return month_days[month]


print(is_leap(2017))  # False
print(is_leap(2020))  # True
print(days_in_month(2017, 2))  # 28


"""
Expected output
---------------
Hello, You
Hello, Vaish
('Math', 'Art')
{'name': 'John', 'age': 22}
('Math', 'Art')
{'name': 'John', 'age': 22}
False
True
28
"""
