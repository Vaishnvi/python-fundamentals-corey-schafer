"""
Sets - Set Methods and Operations
=================================
Corey Schafer - Python Tutorial

A set is an unordered collection of UNIQUE, hashable values. Two things make
sets worth knowing:
    1. Membership tests (`x in s`) are O(1) on average, vs O(n) for a list.
    2. Set algebra - intersection, difference, union - is built in.

Covers:
    * Creating sets (and the {} gotcha)
    * add / update / remove / discard
    * intersection, difference, symmetric_difference
    * De-duplicating a list
    * A realistic example comparing groups of people

Run:
    python 14_sets.py
"""

# ---------------------------------------------------------------------------
# Creating and modifying sets
# ---------------------------------------------------------------------------
# s1 = set([1, 2, 3, 4, 5])    # from any iterable
s1 = {1, 2, 3, 4, 5}  # set literal
# GOTCHA: {} is an empty DICT. For an empty set you must write set().
print(s1)

s1.add(6)  # add ONE value
print(s1)

s2 = {7, 8, 9, 10}
s1.update([7, 8, 9], s2)  # add every value from one or more iterables
print(s1)

s1.remove(5)  # remove a value; KeyError if it is not present
print(s1)

# s1.remove(11)   # KeyError!
s1.discard(11)  # like remove(), but silently does nothing if absent
print(s1)

# ---------------------------------------------------------------------------
# Set algebra
# ---------------------------------------------------------------------------
s1 = {1, 2, 3}
s2 = {2, 3, 4}
s3 = {3, 4, 5}

# intersection -> values present in ALL of the sets
s4 = s1.intersection(s2)  # {2, 3}
print(s4)

s4 = s1.intersection(s2, s3)  # {3}  - can take several sets at once
print(s4)

# difference -> values in the FIRST set that are NOT in the others.
# Order matters: s1 - s2 is not the same as s2 - s1.
s5 = s1.difference(s2)  # {1}
print(s5)

s5 = s2.difference(s1)  # {4}
print(s5)

s5 = s2.difference(s1, s3)  # set()  - nothing in s2 is missing from both
print(s5)

s5 = s3.difference(s1, s2)  # {5}
print(s5)

# symmetric_difference -> values in EITHER set but NOT in both
s5 = s1.symmetric_difference(s2)  # {1, 4}
print(s5)

s5 = s2.symmetric_difference(s1)  # {1, 4}  - symmetric, so order doesn't matter
print(s5)

# Operator shorthand for the same operations:
#   s1 & s2   intersection        s1 | s2   union
#   s1 - s2   difference          s1 ^ s2   symmetric_difference

# ---------------------------------------------------------------------------
# De-duplicating a list
# ---------------------------------------------------------------------------
# Converting to a set drops duplicates; convert back if you need a list.
# NOTE: original ordering is not preserved.
l1 = [1, 2, 3, 1, 2, 3]
l2 = list(set(l1))
print(l2)

# ---------------------------------------------------------------------------
# Realistic example
# ---------------------------------------------------------------------------
employees = ["Corey", "Jim", "Steven", "April", "Judy", "Jenn", "John", "Jane"]
gym_members = ["April", "John", "Corey"]
developers = ["Judy", "Corey", "Steven", "Jane", "April"]

# Who is BOTH a gym member and a developer?
res = set(gym_members).intersection(developers)
print(res)

# Which employees are NEITHER gym members NOR developers?
res = set(employees).difference(gym_members, developers)
print(res)

# Membership test. This works on a list, but it has to scan every element.
if "Corey" in developers:
    print("Found")

# Rule of thumb: if you do lots of `in` checks on a big collection, make it a set.
#   list -> O(n) per lookup
#   set  -> O(1) per lookup


"""
Expected output (set ordering may vary)
---------------------------------------
{1, 2, 3, 4, 5}
{1, 2, 3, 4, 5, 6}
{1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
{1, 2, 3, 4, 6, 7, 8, 9, 10}
{1, 2, 3, 4, 6, 7, 8, 9, 10}
{2, 3}
{3}
{1}
{4}
set()
{5}
{1, 4}
{1, 4}
[1, 2, 3]
{'April', 'Corey'}
{'Jim', 'Jenn'}
Found
"""
