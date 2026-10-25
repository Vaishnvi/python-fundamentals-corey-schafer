"""
Comprehensions - List, Dict, Set and Generator Expressions
==========================================================
Corey Schafer - Python Tutorial

A comprehension builds a collection in a single readable expression. Each
example below shows the explicit for-loop first, then the equivalent
comprehension, so you can see how one maps onto the other.

General shape:
    [ <expression>  for <item> in <iterable>  if <condition> ]

Covers:
    * List comprehensions, with a transform and with a filter
    * Nested loops inside a comprehension
    * Dict comprehensions (with zip)
    * Set comprehensions
    * Generator expressions vs generator functions

Run:
    python 12_comprehensions.py
"""

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# ---------------------------------------------------------------------------
# 1. Copy every item   "I want n for each n in nums"
# ---------------------------------------------------------------------------
my_list = []
for n in nums:
    my_list.append(n)
print(my_list)

my_list = [n for n in nums]
print(my_list)

# ---------------------------------------------------------------------------
# 2. Transform every item   "I want n*n for each n in nums"
# ---------------------------------------------------------------------------
my_list = []
for n in nums:
    my_list.append(n * n)
print(my_list)

my_list = [n * n for n in nums]
print(my_list)

# The functional equivalent uses map() + a lambda. The comprehension is
# generally considered more readable in Python.
# my_list = list(map(lambda n: n * n, nums))

# ---------------------------------------------------------------------------
# 3. Filter items   "I want n for each n in nums if n is even"
# ---------------------------------------------------------------------------
my_list = []
for n in nums:
    if n % 2 == 0:
        my_list.append(n)
print(my_list)

my_list = [n for n in nums if n % 2 == 0]
print(my_list)

# Functional equivalent with filter():
# my_list = list(filter(lambda n: n % 2 == 0, nums))

# ---------------------------------------------------------------------------
# 4. Nested loops   "I want a (letter, num) pair for each letter and each num"
# ---------------------------------------------------------------------------
my_list = []
for letter in "abcd":
    for num in range(4):
        my_list.append((letter, num))
print(my_list, "\n")

# The for-clauses appear in the SAME order as the nested loops.
my_list = [(letter, num) for letter in "abcd" for num in range(4)]
print(my_list)

# ---------------------------------------------------------------------------
# 5. Dict comprehension   "I want a dict {name: hero} for each pair"
# ---------------------------------------------------------------------------
names = ["Bruce", "Clark", "Peter", "Logan", "Tony"]
heros = ["Batman", "Superman", "Spiderman", "Wolverine", "Ironman"]

# zip() pairs items up position by position. It is lazy, so printing it shows
# only a zip object; iterate over it (or call list()) to see the pairs.
print(zip(names, heros))

my_dict = {}
for name, hero in zip(names, heros):
    my_dict[name] = hero
print(my_dict)

# Filters work in dict comprehensions too.
my_dict = {name: hero for name, hero in zip(names, heros) if name != "Peter"}
print(my_dict)

# ---------------------------------------------------------------------------
# 6. Set comprehension   "I want a set of the unique values in nums"
# ---------------------------------------------------------------------------
nums = [1, 1, 2, 1, 3, 4, 3, 5, 5, 6, 7, 8, 7, 9, 9]

my_set = set()
for n in nums:
    my_set.add(n)
print(my_set)

my_set = {n for n in nums}
print(my_set)

# ---------------------------------------------------------------------------
# 7. Generator expression   "I want to yield n*n for each n in nums"
# ---------------------------------------------------------------------------
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def gen_func(nums):
    for n in nums:
        yield n * n


my_gen = gen_func(nums)

for i in my_gen:
    print(i)

# Same thing with a generator EXPRESSION: just use ( ) instead of [ ].
# Nothing is computed until you iterate - see 15_generators.py for why that matters.
my_gen = (n * n for n in nums)
for i in my_gen:
    print(i)


"""
Expected output
---------------
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
[2, 4, 6, 8, 10]
[2, 4, 6, 8, 10]
[('a', 0), ('a', 1), ('a', 2), ('a', 3), ('b', 0), ..., ('d', 3)]

[('a', 0), ('a', 1), ('a', 2), ('a', 3), ('b', 0), ..., ('d', 3)]
<zip object at 0x...>
{'Bruce': 'Batman', 'Clark': 'Superman', 'Peter': 'Spiderman', 'Logan': 'Wolverine', 'Tony': 'Ironman'}
{'Bruce': 'Batman', 'Clark': 'Superman', 'Logan': 'Wolverine', 'Tony': 'Ironman'}
{1, 2, 3, 4, 5, 6, 7, 8, 9}
{1, 2, 3, 4, 5, 6, 7, 8, 9}
1
4
9
...
100
1
4
9
...
100
"""
