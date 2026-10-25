"""
my_module - a tiny module used to demonstrate imports
=====================================================
Imported by 07_modules_std_lib.py.

When Python imports a module it RUNS the module's top-level code once, which is
why the print() below shows up when another script imports this file.
"""

print("Imported my_module")

test = "Test string"


def find_index(to_search, target):
    """Return the index of `target` in the sequence `to_search`, or -1 if absent."""
    for i, value in enumerate(to_search):
        if value == target:
            return i

    return -1
