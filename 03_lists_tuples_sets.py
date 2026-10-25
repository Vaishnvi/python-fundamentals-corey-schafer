"""
Lists, Tuples and Sets
======================
Corey Schafer - Python Tutorial for Beginners #4

Lists and tuples hold SEQUENTIAL data (order matters, duplicates allowed).
    * list  -> mutable   (can be changed after creation)
    * tuple -> immutable (cannot be changed after creation)
Sets are UNORDERED collections with NO duplicates. They are great for
membership tests and for comparing groups of values.

Covers:
    * Indexing and slicing lists
    * Adding items: append, insert, extend
    * Removing items: remove, pop
    * Ordering: reverse, sort (in place) vs sorted() (returns a new list)
    * min / max / sum, index(), the `in` operator
    * enumerate(), ', '.join(), str.split()
    * Why aliasing a list is dangerous, and why tuples are safe
    * Set operations: intersection, difference, union
    * Creating empty containers

Run:
    python 03_lists_tuples_sets.py
"""

# ---------------------------------------------------------------------------
# Lists
# ---------------------------------------------------------------------------
courses = ["History", "Math", "Physics", "Compsci"]

print(courses)
print(len(courses))  # 4 items

# Indexing: 0 is the first item, -1 is the last item.
print(courses[0])  # History
print(courses[3])  # Compsci
print(courses[-1])  # Compsci

# Slicing: [start (inclusive) : stop (exclusive)]
print(courses[0:2])  # ['History', 'Math']
print(courses[:2])  # same thing - start defaults to 0
print(courses[2:])  # ['Physics', 'Compsci'] - stop defaults to the end

# --- Adding items ---------------------------------------------------------
courses.append("Art")  # add ONE item to the end
print(courses)

courses.insert(0, "Geography")  # add ONE item at a specific index
print(courses)

courses2 = ["Chemistry", "Education"]

# CAUTION: insert()/append() with a list adds the whole list as a single
# nested item, e.g. ['Chemistry', 'Education'] becomes ONE element.
# courses.insert(0, courses2)

# extend() unpacks the iterable and adds each item individually.
courses.extend(courses2)
print(courses)

# --- Removing items -------------------------------------------------------
courses.remove("Math")  # remove by VALUE (first occurrence)
print(courses)

popped = courses.pop()  # remove and RETURN the last item
print(popped)  # Education
print(courses)

# --- Reordering -----------------------------------------------------------
courses.reverse()  # in place
print(courses)

courses.sort()  # in place, alphabetical for strings
print(courses)

nums = [1, 5, 2, 4, 3]
nums.sort()  # ascending for numbers
print(nums)

courses.sort(reverse=True)  # descending
print(courses)

# sorted() returns a NEW sorted list and does NOT alter the original.
courses_sort = sorted(courses)
print(courses_sort)

# --- Handy built-ins ------------------------------------------------------
print(min(nums))  # 1
print(max(nums))  # 5
print(sum(nums))  # 15

print(courses.index("Compsci"))  # position of a value (ValueError if missing)
print("Lin Algebra" in courses)  # membership test -> False

# --- Looping with an index ------------------------------------------------
for index, course in enumerate(courses):
    print(index, course)

# enumerate() can start counting from any number.
for index, course in enumerate(courses, start=1):
    print(index, course)

# --- Lists <-> strings ----------------------------------------------------
course_str = ", ".join(courses)  # list -> single string
print(course_str)

new_list = course_str.split(", ")  # string -> list
print(new_list)

# ---------------------------------------------------------------------------
# Mutability: lists vs tuples
# ---------------------------------------------------------------------------
# Assigning a list to a second name does NOT copy it. Both names point to the
# SAME object, so a change through one name is visible through the other.
list_1 = ["History", "Math", "Physics", "Compsci"]
list_2 = list_1

list_1[0] = "Art"
print(list_1)  # ['Art', 'Math', 'Physics', 'Compsci']
print(list_2)  # ['Art', 'Math', 'Physics', 'Compsci']  <- changed too!

# Tuples are immutable, so this kind of accidental change cannot happen.
tuple_1 = ("History", "Math", "Physics", "Compsci")
tuple_2 = tuple_1

# tuple_1[0] = "Art"   # TypeError: 'tuple' object does not support item assignment

print(tuple_1)
print(tuple_2)

# ---------------------------------------------------------------------------
# Sets
# ---------------------------------------------------------------------------
# Unordered, no duplicates. Notice 'Math' appears twice below but is stored once.
# The print order is NOT guaranteed and may differ between runs.
cs_courses = {"History", "Math", "Physics", "Compsci", "Math"}
print(cs_courses)

# Membership tests on a set are very fast (O(1) on average vs O(n) for a list).
print("Math" in cs_courses)  # True

art_courses = {"History", "Math", "Art", "Design"}

print(cs_courses.intersection(art_courses))  # in BOTH sets
print(cs_courses.difference(art_courses))  # in cs_courses but NOT in art_courses
print(cs_courses.union(art_courses))  # everything from both sets, de-duplicated

# ---------------------------------------------------------------------------
# Creating empty containers
# ---------------------------------------------------------------------------
empty_list = []
empty_list = list()

empty_tuple = ()
empty_tuple = tuple()

# GOTCHA: {} creates an empty DICT, not an empty set. Use set() instead.
empty_set = set()


"""
Expected output (set ordering may vary)
---------------------------------------
['History', 'Math', 'Physics', 'Compsci']
4
History
Compsci
Compsci
['History', 'Math']
['History', 'Math']
['Physics', 'Compsci']
['History', 'Math', 'Physics', 'Compsci', 'Art']
['Geography', 'History', 'Math', 'Physics', 'Compsci', 'Art']
['Geography', 'History', 'Math', 'Physics', 'Compsci', 'Art', 'Chemistry', 'Education']
['Geography', 'History', 'Physics', 'Compsci', 'Art', 'Chemistry', 'Education']
Education
['Geography', 'History', 'Physics', 'Compsci', 'Art', 'Chemistry']
['Chemistry', 'Art', 'Compsci', 'Physics', 'History', 'Geography']
['Art', 'Chemistry', 'Compsci', 'Geography', 'History', 'Physics']
[1, 2, 3, 4, 5]
['Physics', 'History', 'Geography', 'Compsci', 'Chemistry', 'Art']
['Art', 'Chemistry', 'Compsci', 'Geography', 'History', 'Physics']
1
5
15
3
False
0 Physics
1 History
2 Geography
3 Compsci
4 Chemistry
5 Art
1 Physics
2 History
3 Geography
4 Compsci
5 Chemistry
6 Art
Physics, History, Geography, Compsci, Chemistry, Art
['Physics', 'History', 'Geography', 'Compsci', 'Chemistry', 'Art']
['Art', 'Math', 'Physics', 'Compsci']
['Art', 'Math', 'Physics', 'Compsci']
('History', 'Math', 'Physics', 'Compsci')
('History', 'Math', 'Physics', 'Compsci')
{'Physics', 'Compsci', 'Math', 'History'}
True
{'Math', 'History'}
{'Physics', 'Compsci'}
{'Compsci', 'Physics', 'Design', 'Math', 'Art', 'History'}
"""
