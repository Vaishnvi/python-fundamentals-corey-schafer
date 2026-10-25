"""
Strings - Working with Textual Data
===================================
Corey Schafer - Python Tutorial for Beginners #2

Covers:
    * Indexing single characters of a string
    * Slicing with [start:stop] (start is inclusive, stop is exclusive)
    * Common string methods: lower, upper, count, find, replace
    * Three ways to build strings: concatenation, str.format(), f-strings
    * Discovering what an object can do with dir() and help()

Run:
    python 01_strings_text_data.py
"""

message = "Hello World"

# ---------------------------------------------------------------------------
# Indexing
# ---------------------------------------------------------------------------
# A string is a sequence of characters. Each character has a position (index)
# starting at 0, so index 10 is the 11th character.
print(message[10])  # d

# ---------------------------------------------------------------------------
# Slicing: message[start:stop]
# ---------------------------------------------------------------------------
# `start` is inclusive, `stop` is exclusive.
print(message[0:5])  # Hello  -> characters at index 0, 1, 2, 3, 4

# Leaving `start` off means "from the beginning".
print(message[:5])  # Hello

# Leaving `stop` off means "all the way to the end".
print(message[6:])  # World

# ---------------------------------------------------------------------------
# String methods
# ---------------------------------------------------------------------------
# NOTE: strings are immutable. Every method below returns a NEW string and
# leaves `message` exactly as it was.

print(message.lower())  # hello world
print(message.upper())  # HELLO WORLD

# count() -> how many times a substring appears
print(message.count("Hello"))  # 1
print(message.count("l"))  # 3

# find() -> index where the substring starts, or -1 if it is not present
print(message.find("World"))  # 6
print(message.find("Universe"))  # -1

# replace() -> returns a new string with the replacement applied
new_message = message.replace("World", "Universe")
print(new_message)  # Hello Universe

# ---------------------------------------------------------------------------
# Building strings from pieces
# ---------------------------------------------------------------------------
greeting = "Hello"
name = "Michael"

# 1. Concatenation with `+`. Gets messy fast and only works with strings.
message = greeting + ", " + name + ". Welcome!"

# 2. str.format(). The {} placeholders are filled in order.
message = "{}, {}. Welcome!".format(greeting, name)

# 3. f-strings (Python 3.6+). Preferred: any expression can go inside {}.
message = f"{greeting}, {name.upper()}. Welcome!"

print(message)  # Hello, MICHAEL. Welcome!

# ---------------------------------------------------------------------------
# Introspection: what can a string do?
# ---------------------------------------------------------------------------
# dir() lists every attribute and method available on an object.
print(dir(name))

# help() prints the documentation for an object or method.
# help(str) would print docs for the whole class (very long), so we only ask
# about a single method here.
help(str.lower)


"""
Expected output
---------------
d
Hello
Hello
World
hello world
HELLO WORLD
1
3
6
-1
Hello Universe
Hello, MICHAEL. Welcome!
['__add__', '__class__', '__contains__', ..., 'upper', 'zfill']
Help on method_descriptor:

lower(self, /) unbound builtins.str method
    Return a copy of the string converted to lowercase.
"""
