"""
Slicing Lists and Strings
=========================
Corey Schafer - Python Tutorial

The full slice syntax is  sequence[start:stop:step]

    start  -> index to begin at (INCLUSIVE). Defaults to the beginning.
    stop   -> index to stop at  (EXCLUSIVE). Defaults to the end.
    step   -> how far to jump each time. Defaults to 1. Negative = go backwards.

Negative indexes count from the END:  -1 is the last item, -2 the second last.

Positive index:   0   1   2   3   4   5   6   7   8   9
Value:            0   1   2   3   4   5   6   7   8   9
Negative index: -10  -9  -8  -7  -6  -5  -4  -3  -2  -1

Run:
    python 11_slicing_lists_strings.py
"""

my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

print(my_list)

# ---------------------------------------------------------------------------
# Single indexes
# ---------------------------------------------------------------------------
print(my_list[0])  # 0  first item
print(my_list[-1])  # 9  last item
print(my_list[-10])  # 0  first item, counting from the end

# ---------------------------------------------------------------------------
# [start:stop]
# ---------------------------------------------------------------------------
print(my_list[3:8])  # [3, 4, 5, 6, 7]       - stop index 8 is NOT included
print(my_list[-7:-2])  # [3, 4, 5, 6, 7]       - same slice using negative indexes
print(my_list[1:-2])  # [1, 2, 3, 4, 5, 6, 7] - mixing positive and negative is fine

# Leaving out start / stop
print(my_list[1:])  # [1, ..., 9]  from index 1 to the end
print(my_list[:-1])  # [0, ..., 8]  from the beginning up to (not incl.) the last
print(my_list[:])  # the whole list - a common way to make a shallow COPY

# ---------------------------------------------------------------------------
# [start:stop:step]
# ---------------------------------------------------------------------------
print(my_list[2:-1])  # [2, 3, 4, 5, 6, 7, 8]
print(my_list[2:-1:2])  # [2, 4, 6, 8]           every 2nd item
print(my_list[2:-1:1])  # [2, 3, 4, 5, 6, 7, 8]  step of 1 is the default

# A NEGATIVE step walks backwards, so start must be to the RIGHT of stop.
print(my_list[-1:2:-1])  # [9, 8, 7, 6, 5, 4, 3]
print(my_list[::-1])  # [9, 8, ..., 0]  the idiom for reversing a sequence

# ---------------------------------------------------------------------------
# Strings slice exactly the same way
# ---------------------------------------------------------------------------
sample_url = "http://coreyms.com"
print(sample_url)

print(sample_url[::-1])  # moc.smyeroc//:ptth  - reversed
print(sample_url[-4:])  # .com                - the top-level domain
print(sample_url[7:])  # coreyms.com         - drop 'http://'
print(sample_url[7:-4])  # coreyms             - drop 'http://' AND '.com'


"""
Expected output
---------------
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
0
9
0
[3, 4, 5, 6, 7]
[3, 4, 5, 6, 7]
[1, 2, 3, 4, 5, 6, 7]
[1, 2, 3, 4, 5, 6, 7, 8, 9]
[0, 1, 2, 3, 4, 5, 6, 7, 8]
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
[2, 3, 4, 5, 6, 7, 8]
[2, 4, 6, 8]
[2, 3, 4, 5, 6, 7, 8]
[9, 8, 7, 6, 5, 4, 3]
[9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
http://coreyms.com
moc.smyeroc//:ptth
.com
coreyms.com
coreyms
"""
