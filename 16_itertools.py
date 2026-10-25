"""
Itertools Module - Iterator Functions for Efficient Looping
===========================================================
Corey Schafer - Python Tutorial

itertools is a collection of fast, memory-efficient building blocks that
return ITERATORS (lazy - values are produced only when requested).

Infinite iterators:        count, cycle, repeat
Combinatoric iterators:    combinations, permutations, product,
                           combinations_with_replacement
Terminating iterators:     chain, islice, compress, filterfalse, accumulate,
                           groupby, tee, zip_longest, starmap

Run:
    python 16_itertools.py
"""

import itertools
import operator
from pathlib import Path

DATA_DIR = Path(__file__).resolve().parent / "data"

# ---------------------------------------------------------------------------
# count(start, step) - infinite counter
# ---------------------------------------------------------------------------
counter = itertools.count(start=5, step=-5)

print(next(counter))  # 5
print(next(counter))  # 0
print(next(counter))  # -5
print(next(counter))  # -10

# A classic use: pair every item with an index, without knowing the length.
# zip() stops at the shortest input, so the infinite count() is harmless.
data = [100, 200, 300, 400]

daily_data = list(zip(itertools.count(), data))
print(daily_data)  # [(0, 100), (1, 200), (2, 300), (3, 400)]

# With range(10) the extra indexes 4-9 are simply dropped...
daily_data = list(zip(range(10), data))
print(daily_data)

# ...unless you use zip_longest, which pads the shorter input with None.
daily_data = list(itertools.zip_longest(range(10), data))
print(daily_data)

# ---------------------------------------------------------------------------
# cycle(iterable) - loop over the values forever
# ---------------------------------------------------------------------------
counter = itertools.cycle([1, 2, 3])
print(next(counter))  # 1
print(next(counter))  # 2
print(next(counter))  # 3
print(next(counter))  # 1  <- wraps around

# Handy for toggling state
counter = itertools.cycle(["On", "Off"])
print(next(counter))  # On
print(next(counter))  # Off
print(next(counter))  # On
print(next(counter))  # Off

# ---------------------------------------------------------------------------
# repeat(value, times) - the same value over and over
# ---------------------------------------------------------------------------
counter = itertools.repeat(2, times=3)
print(next(counter))  # 2
print(next(counter))  # 2
print(next(counter))  # 2
# print(next(counter))   # StopIteration - only 3 were requested

# Without `times` it repeats forever, which pairs nicely with map():
# pow(0, 2), pow(1, 2), pow(2, 2), ...  -> map stops when range(10) does.
squares = map(pow, range(10), itertools.repeat(2))
print(list(squares))

# starmap() unpacks each tuple into the function's arguments: pow(*(0, 2)) ...
squares = itertools.starmap(pow, [(0, 2), (1, 2), (2, 2)])
print(list(squares))

# ---------------------------------------------------------------------------
# Combinatorics
# ---------------------------------------------------------------------------
letters = ["a", "b", "c", "d"]
numbers = [0, 1, 2, 3]
names = ["Corey", "Nicole"]

# combinations: order does NOT matter -> ('a','b') and ('b','a') count once
result = itertools.combinations(letters, 2)

print("Combinations:")
for item in result:
    print(item)

# permutations: order DOES matter -> ('a','b') and ('b','a') are both included
result = itertools.permutations(letters, 2)

print("Permutations:")
for item in result:
    print(item)

# product: cartesian product, values CAN repeat. repeat=4 means "pick 4 times
# from `numbers`", i.e. every 4-digit code using digits 0-3 (256 of them).
print("Product:")
result = itertools.product(numbers, repeat=4)
for item in result:
    print(item)

# combinations_with_replacement: like combinations, but a value may be reused
print("combinations_with_replacement:")
result = itertools.combinations_with_replacement(numbers, 4)
for item in result:
    print(item)

# ---------------------------------------------------------------------------
# chain(*iterables) - iterate several iterables back to back
# ---------------------------------------------------------------------------
# letters + numbers + names would build a brand-new combined list in memory.
# chain() just walks through each one in turn without copying anything.
combined = itertools.chain(letters, numbers, names)

for item in combined:
    print(item)

# ---------------------------------------------------------------------------
# islice(iterable, start, stop, step) - slicing for iterators
# ---------------------------------------------------------------------------
# Regular slicing needs a sequence. islice works on ANY iterator, lazily.
result = itertools.islice(range(10), 5, 10, 2)

for item in result:
    print(item)  # 5, 7, 9

# Practical use: read only the first 3 lines of a (potentially huge) file
# without loading the rest.
with open(DATA_DIR / "test.log", "r") as f:
    header = itertools.islice(f, 3)

    for line in header:
        print(line, end="")

# ---------------------------------------------------------------------------
# compress(data, selectors) - keep items whose selector is truthy
# ---------------------------------------------------------------------------
selectors = [True, True, False, True]
result = itertools.compress(letters, selectors)

for item in result:
    print(item)  # a, b, d


# ---------------------------------------------------------------------------
# filter vs filterfalse
# ---------------------------------------------------------------------------
def lt_2(n):
    """Return True if n is less than 2."""
    return n < 2


# Built-in filter keeps items where the function returns True...
result = filter(lt_2, numbers)
for item in result:
    print(item)  # 0, 1

# ...filterfalse keeps the ones where it returns False.
result = itertools.filterfalse(lt_2, numbers)
for item in result:
    print(item)  # 2, 3

# ---------------------------------------------------------------------------
# accumulate(iterable, func=operator.add) - running totals
# ---------------------------------------------------------------------------
result = itertools.accumulate(numbers)
for item in result:
    print(item)  # 0, 1, 3, 6  (running sum)

# Any 2-argument function works, e.g. a running product.
result = itertools.accumulate(numbers, operator.mul)
for item in result:
    print(item)  # 0, 0, 0, 0  (first value is 0, so everything stays 0)

# ---------------------------------------------------------------------------
# groupby(iterable, key) - group CONSECUTIVE items sharing a key
# ---------------------------------------------------------------------------
# IMPORTANT: groupby only groups items that are next to each other, so the
# data must already be SORTED by the grouping key or you get fragmented groups.
people = [
    {"name": "John Doe", "city": "Gotham", "state": "NY"},
    {"name": "Jane Doe", "city": "Kings Landing", "state": "NY"},
    {"name": "Corey Schafer", "city": "Boulder", "state": "CO"},
    {"name": "Al Einstein", "city": "Denver", "state": "CO"},
    {"name": "John Henry", "city": "Hinton", "state": "WV"},
    {"name": "Randy Moss", "city": "Rand", "state": "WV"},
    {"name": "Nicole K", "city": "Asheville", "state": "NC"},
    {"name": "Jim Doe", "city": "Charlotte", "state": "NC"},
    {"name": "Jane Taylor", "city": "Faketown", "state": "NC"},
]


def get_state(person):
    return person["state"]


person_group = itertools.groupby(people, key=get_state)

# Each iteration yields (key, group) where `group` is itself an iterator.
for key, group in person_group:
    print(key, group)
    for person in group:
        print(person)
    print()

# ---------------------------------------------------------------------------
# tee(iterable, n=2) - split one iterator into n independent copies
# ---------------------------------------------------------------------------
# Useful when you need to walk the same lazy data twice. Once you tee an
# iterator, stop using the original - advancing it would desynchronise the copies.
squares = (n * n for n in range(5))
copy1, copy2 = itertools.tee(squares)

print(list(copy1))  # [0, 1, 4, 9, 16]
print(list(copy2))  # [0, 1, 4, 9, 16]  - the second copy is unaffected


"""
Expected output (abridged)
--------------------------
5
0
-5
-10
[(0, 100), (1, 200), (2, 300), (3, 400)]
[(0, 100), (1, 200), (2, 300), (3, 400)]
[(0, 100), (1, 200), (2, 300), (3, 400), (4, None), (5, None), (6, None), (7, None), (8, None), (9, None)]
1
2
3
1
On
Off
On
Off
2
2
2
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
[0, 1, 4]
Combinations:
('a', 'b')
...
Permutations:
('a', 'b')
...
Product:
(0, 0, 0, 0)
...
combinations_with_replacement:
(0, 0, 0, 0)
...
a
b
c
d
0
1
2
3
Corey
Nicole
5
7
9
Date: 2018-11-08
Author: Corey
Description: This is a sample log file
a
b
d
0
1
2
3
0
1
3
6
0
0
0
0
NY <itertools._grouper object at 0x...>
{'name': 'John Doe', 'city': 'Gotham', 'state': 'NY'}
{'name': 'Jane Doe', 'city': 'Kings Landing', 'state': 'NY'}

CO <itertools._grouper object at 0x...>
...
[0, 1, 4, 9, 16]
[0, 1, 4, 9, 16]
"""
