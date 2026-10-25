"""
Generators - How to Use Them and the Benefits
=============================================
Corey Schafer - Python Tutorial

A generator produces values ONE AT A TIME, on demand, instead of building the
entire result in memory up front.

    * Any function containing `yield` is a generator function. Calling it
      returns a generator object; the body does not run until you iterate.
    * Each `yield` hands one value back and PAUSES the function. The next
      request resumes right where it left off.
    * When the function finishes, the generator raises StopIteration and
      for-loops stop automatically.

Covers:
    * Converting a list-building function into a generator
    * Pulling values manually with next()
    * Generator expressions: (x for x in ...) vs [x for x in ...]
    * Why generators matter for memory

Run:
    python 15_generators.py
"""


# ---------------------------------------------------------------------------
# List-building version (for comparison)
# ---------------------------------------------------------------------------
# def square_numbers(nums):
#     result = []
#     for i in nums:
#         result.append(i * i)
#     return result


# ---------------------------------------------------------------------------
# Generator version
# ---------------------------------------------------------------------------
def square_numbers(nums):
    for i in nums:
        yield i * i  # hand back one value, then pause here


my_nums = square_numbers([1, 2, 3, 4, 5])

# Nothing has been computed yet - we just have a generator object.
print(my_nums)  # <generator object square_numbers at 0x...>

# You can pull values manually with next(). A sixth call would raise
# StopIteration because the input only has five items.
# print(next(my_nums))   # 1
# print(next(my_nums))   # 4
# print(next(my_nums))   # 9
# print(next(my_nums))   # 16
# print(next(my_nums))   # 25
# print(next(my_nums))   # StopIteration

# A for-loop calls next() for you and stops cleanly at StopIteration.
for num in my_nums:
    print(num)

# ---------------------------------------------------------------------------
# List comprehension: all values computed and stored immediately
# ---------------------------------------------------------------------------
my_nums = [x * x for x in [1, 2, 3, 4, 5]]

for num in my_nums:
    print(num)

# ---------------------------------------------------------------------------
# Generator expression: same syntax with ( ) instead of [ ]
# ---------------------------------------------------------------------------
my_nums = (x * x for x in [1, 2, 3, 4, 5])
print(my_nums)  # <generator object <genexpr> at 0x...>

# Wrapping it in list() consumes the generator and materialises every value.
print(list(my_nums))

# ---------------------------------------------------------------------------
# Why bother?
# ---------------------------------------------------------------------------
# With millions of items a list holds EVERY value in memory at once. A
# generator holds only the current one, so memory use stays flat no matter
# how large the input is - and you can start processing the first result
# before the last one has been computed.
#
# The moment you call list() on a generator you give that advantage up,
# because all the values are pulled into memory.


"""
Expected output
---------------
<generator object square_numbers at 0x...>
1
4
9
16
25
1
4
9
16
25
<generator object <genexpr> at 0x...>
[1, 4, 9, 16, 25]
"""
