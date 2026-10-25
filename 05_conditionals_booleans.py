"""
Conditionals and Booleans - if, else, elif
==========================================
Corey Schafer - Python Tutorial for Beginners #6

Covers:
    * if / elif / else
    * Comparison operators and the difference between == and `is`
    * Combining conditions with and / or / not
    * Which values Python treats as False ("falsy")

Run:
    python 05_conditionals_booleans.py
"""

language = "Python"

# The condition after `if` is any expression that evaluates to True or False.
if language == "Python":
    print("Conditional was true")

# ---------------------------------------------------------------------------
# if / elif / else chain - only the FIRST matching branch runs
# ---------------------------------------------------------------------------
language = "Java"

if language == "Python":
    print("Language is Python")
elif language == "Java":
    print("Language is Java")
elif language == "JavaScript":
    print("Language is JavaScript")
else:
    print("No match")

# ---------------------------------------------------------------------------
# Comparison operators
# ---------------------------------------------------------------------------
#   ==   equal                 !=   not equal
#   >    greater than          <    less than
#   >=   greater or equal      <=   less or equal
#   is   same OBJECT (identity, not just equal value)

a = [1, 2, 3]
b = [1, 2, 3]
print(a == b)  # True  - same contents
print(a is b)  # False - two different list objects in memory

b = a
print(a is b)  # True  - both names now point to the same object

# ---------------------------------------------------------------------------
# Boolean operators: and / or / not
# ---------------------------------------------------------------------------
user = "Admin"
logged_in = False

if user == "Admin" and logged_in:
    print("Admin Page")
else:
    print("Bad Creds")

if user == "Admin" or logged_in:
    print("Admin Page")
else:
    print("Bad Creds")

if not logged_in:
    print("Please Log In")
else:
    print("Welcome")

# ---------------------------------------------------------------------------
# Truthiness: these values all evaluate to False
# ---------------------------------------------------------------------------
#   False, None, 0, 0.0, "" (empty string), [] (empty list), () (empty tuple),
#   {} (empty dict), set() (empty set)
# Everything else is truthy.
condition = []

if condition:
    print("Evaluated to True")
else:
    print("Evaluated to False")


"""
Expected output
---------------
Conditional was true
Language is Java
True
False
True
Bad Creds
Admin Page
Please Log In
Evaluated to False
"""
