"""
Dictionaries - Working with Key-Value Pairs
===========================================
Corey Schafer - Python Tutorial for Beginners #5

A dict maps KEYS to VALUES. Keys must be hashable (strings, numbers, tuples);
values can be anything, including lists and other dicts.

Covers:
    * Creating a dict and reading values with [] vs .get()
    * Adding and updating entries, including bulk updates with .update()
    * Removing entries with del and .pop()
    * len(), .keys(), .values(), .items()
    * Looping over key/value pairs

Run:
    python 04_dictionaries.py
"""

student = {"name": "John", "age": 25, "courses": ["Math", "Compsci"]}
print(student)

# ---------------------------------------------------------------------------
# Reading values
# ---------------------------------------------------------------------------
# Square brackets raise a KeyError if the key does not exist.
print(student["name"])  # John
print(student["courses"])  # ['Math', 'Compsci']

# .get() returns None (or a default you supply) instead of raising.
print(student.get("name"))  # John
print(student.get("id"))  # None  - key does not exist, no error
print(student.get("phone", "Not Found"))  # Not Found - custom default

# ---------------------------------------------------------------------------
# Adding and updating entries
# ---------------------------------------------------------------------------
# Assigning to a key that does not exist ADDS it.
student["phone"] = "555-5555"
print(student.get("phone", "Not Found"))  # 555-5555

# Assigning to an existing key OVERWRITES its value.
student["name"] = "Jane"
print(student)

# .update() changes several keys at once; new keys are added, existing ones
# are overwritten.
student.update({"name": "VK", "id": "731", "age": 30})
print(student)

# ---------------------------------------------------------------------------
# Removing entries
# ---------------------------------------------------------------------------
del student["age"]  # remove a key (KeyError if missing)
print(student)

popped = student.pop("id")  # remove a key AND return its value
print(popped, student)

# ---------------------------------------------------------------------------
# Inspecting the dict
# ---------------------------------------------------------------------------
print(len(student))  # number of key/value pairs
print(student.keys())  # dict_keys([...])
print(student.values())  # dict_values([...])
print(student.items())  # dict_items([(key, value), ...])

# Looping directly over a dict gives you only the keys. Use .items() to get
# both the key and the value in one go.
for key, value in student.items():
    print(key, value)


"""
Expected output
---------------
{'name': 'John', 'age': 25, 'courses': ['Math', 'Compsci']}
John
['Math', 'Compsci']
John
None
Not Found
555-5555
{'name': 'Jane', 'age': 25, 'courses': ['Math', 'Compsci'], 'phone': '555-5555'}
{'name': 'VK', 'age': 30, 'courses': ['Math', 'Compsci'], 'phone': '555-5555', 'id': '731'}
{'name': 'VK', 'courses': ['Math', 'Compsci'], 'phone': '555-5555', 'id': '731'}
731 {'name': 'VK', 'courses': ['Math', 'Compsci'], 'phone': '555-5555'}
3
dict_keys(['name', 'courses', 'phone'])
dict_values(['VK', ['Math', 'Compsci'], '555-5555'])
dict_items([('name', 'VK'), ('courses', ['Math', 'Compsci']), ('phone', '555-5555')])
name VK
courses ['Math', 'Compsci']
phone 555-5555
"""
