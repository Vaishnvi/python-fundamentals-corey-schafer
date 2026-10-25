"""
Sorting Lists, Tuples and Objects
=================================
Corey Schafer - Python Tutorial

Two ways to sort:
    sorted(iterable)   -> returns a NEW sorted list; works on ANY iterable
    list.sort()        -> sorts the list IN PLACE and returns None; lists only

Both accept:
    reverse=True  -> descending order
    key=<func>    -> a function applied to each item to decide its sort position

Covers:
    * sorted() vs .sort()
    * Sorting tuples and dicts (dicts sort by their keys)
    * Custom ordering with key=, e.g. key=abs
    * Sorting objects by an attribute: named function, lambda, attrgetter

Run:
    python 13_sorting.py
"""

from operator import attrgetter

# ---------------------------------------------------------------------------
# Lists: sorted() vs .sort()
# ---------------------------------------------------------------------------
li = [9, 1, 8, 2, 7, 3, 6, 4, 5]

# s_li = sorted(li)             # ascending
s_li = sorted(li, reverse=True)  # descending
print(li)  # original list is untouched
print(s_li)

# li.sort()                      # ascending, in place
li.sort(reverse=True)  # descending, in place
print(li)  # the original list is now sorted

# ---------------------------------------------------------------------------
# Tuples and dicts
# ---------------------------------------------------------------------------
tup = (9, 1, 8, 2, 7, 3, 6, 4, 5)
# tup.sort()        # AttributeError - tuples are immutable, no .sort() method
tup_sort = sorted(tup)  # sorted() works and returns a LIST
print(tup_sort)

di = {"name": "Corey", "job": "programming", "age": None, "os": "Mac"}
s_di = sorted(di)  # iterating a dict yields its KEYS, so this sorts the keys
print(s_di)

# ---------------------------------------------------------------------------
# key= : sort by something other than the raw value
# ---------------------------------------------------------------------------
li = [-6, -5, -4, 1, 2, 3]
print(li)

s_li = sorted(li)  # numeric order
print(s_li)

s_abs_li = sorted(li, key=abs)  # order by absolute value, sign ignored
print(s_abs_li)


# ---------------------------------------------------------------------------
# Sorting objects
# ---------------------------------------------------------------------------
class Employee:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def __repr__(self):
        # __repr__ controls how the object is displayed when printed.
        return f"({self.name},{self.age},${self.salary})"


e1 = Employee("Carl", 37, 70000)
e2 = Employee("Sarah", 29, 80000)
e3 = Employee("John", 43, 90000)

employees = [e1, e2, e3]

# sorted(employees)  -> TypeError: Python has no idea how to compare two
# Employee objects. We must tell it WHAT to compare via key=.


# Option 1: a regular named function
def e_sort(emp):
    return emp.name


s_employees = sorted(employees, key=e_sort, reverse=True)
print(s_employees)

# Option 2: a lambda - handy for tiny one-off key functions
s_employees = sorted(employees, key=lambda e: e.name)
print(s_employees)

# Option 3: operator.attrgetter - cleanest when sorting by a plain attribute.
# (itemgetter is the equivalent for dicts / sequences.)
s_employees = sorted(employees, key=attrgetter("age"))
print(s_employees)


"""
Expected output
---------------
[9, 1, 8, 2, 7, 3, 6, 4, 5]
[9, 8, 7, 6, 5, 4, 3, 2, 1]
[9, 8, 7, 6, 5, 4, 3, 2, 1]
[1, 2, 3, 4, 5, 6, 7, 8, 9]
['age', 'job', 'name', 'os']
[-6, -5, -4, 1, 2, 3]
[-6, -5, -4, 1, 2, 3]
[1, 2, 3, -4, -5, -6]
[(Sarah,29,$80000), (John,43,$90000), (Carl,37,$70000)]
[(Carl,37,$70000), (John,43,$90000), (Sarah,29,$80000)]
[(Sarah,29,$80000), (Carl,37,$70000), (John,43,$90000)]
"""
