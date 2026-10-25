"""
Integers and Floats - Working with Numeric Data
===============================================
Corey Schafer - Python Tutorial for Beginners #3

Covers:
    * int vs float, and checking a value's type with type()
    * Arithmetic operators, including floor division // and exponent **
    * Built-in helpers abs() and round()
    * Comparison operators (which always produce a bool)
    * Casting strings to numbers, and why "100" + "200" is not 300

Run:
    python 02_numeric_data.py
"""

num = 3  # int   -> whole number
num2 = 3.14  # float -> number with a decimal point

print(type(num), type(num2))  # <class 'int'> <class 'float'>

# ---------------------------------------------------------------------------
# Arithmetic operators
# ---------------------------------------------------------------------------
print(3 + 2)  # 5    addition
print(3 / 2)  # 1.5  true division - ALWAYS returns a float in Python 3
print(3 // 2)  # 1    floor division - drops the decimal part
print(3**2)  # 9    exponent (3 squared)
print(3 % 2)  # 1    modulo - the remainder. Common use: n % 2 == 0 means n is even

# Order of operations follows normal maths. Use parentheses to be explicit:
#   3 * 2 + 1   -> 7
#   3 * (2 + 1) -> 9

# ---------------------------------------------------------------------------
# Built-in numeric helpers
# ---------------------------------------------------------------------------
print(abs(-3))  # 3    absolute value
print(round(3.75))  # 4    round to the nearest whole number
print(round(3.75, 1))  # 3.8  round to 1 decimal place

# ---------------------------------------------------------------------------
# Comparison operators -> evaluate to True or False
# ---------------------------------------------------------------------------
num_1 = 3
num_2 = 2

print(num_1 != num_2)  # True   not equal
print(num_1 > num_2)  # True   greater than
# The full set: ==   !=   <   >   <=   >=

# ---------------------------------------------------------------------------
# Casting: a string that LOOKS like a number is still a string
# ---------------------------------------------------------------------------
num_1 = "100"
num_2 = "200"

# `+` on two strings is concatenation, not addition.
print(num_1 + num_2)  # 100200

# Convert to int first. float() works the same way for decimal values.
num_1 = int(num_1)
num_2 = int(num_2)

print(num_1 + num_2)  # 300


"""
Expected output
---------------
<class 'int'> <class 'float'>
5
1.5
1
9
1
3
4
3.8
True
True
100200
300
"""
