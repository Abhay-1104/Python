# ============================================
# 📘 SORTING IN PYTHON
# ============================================

# Python provides two main ways to sort:
#
# .sort()
# → Sorts the original list.
# → Changes the list itself.
# → Works with LISTS only.
#
# sorted()
# → Returns a new sorted object/list.
# → Does NOT change the original data.
# → Can be used with lists, tuples, dictionaries, etc.
#
# reverse=True
# → Sorts in descending order.
#
# key=
# → Tells Python what value to use for sorting.


# ============================================
# 1️⃣ LISTS
# ============================================

fruits = ["banana", "orange", "apple", "coconut"]

# fruits.sort()
# → Ascending order

# fruits.sort(reverse=True)
# → Descending order

print(fruits)


# Example:
#
# fruits.sort()
# print(fruits)
#
# ['apple', 'banana', 'coconut', 'orange']
#
#
# fruits.sort(reverse=True)
#
# ['orange', 'coconut', 'banana', 'apple']


# ============================================
# 2️⃣ TUPLES
# ============================================

fruits = ("banana", "orange", "apple", "coconut")

# Tuple does NOT have .sort()
# because tuples are immutable.
#
# Use sorted() instead.

# fruits = tuple(sorted(fruits))
# → Ascending order
#
# fruits = tuple(sorted(fruits, reverse=True))
# → Descending order

print(fruits)


# sorted(fruits)
# → Returns a list.
#
# tuple(sorted(fruits))
# → Converts the sorted list back to a tuple.


# ============================================
# 3️⃣ DICTIONARIES
# ============================================

fruits = {
    "banana": 105,
    "apple": 72,
    "orange": 73,
    "coconut": 354
}


# --------------------------------------------
# Sort by KEY (ascending)
# --------------------------------------------

# fruits = dict(sorted(fruits.items()))


# --------------------------------------------
# Sort by KEY (descending)
# --------------------------------------------

# fruits = dict(
#     sorted(
#         fruits.items(),
#         key=lambda item: item[0],
#         reverse=True
#     )
# )


# --------------------------------------------
# Sort by VALUE (ascending)
# --------------------------------------------

# fruits = dict(
#     sorted(
#         fruits.items(),
#         key=lambda item: item[1]
#     )
# )


# --------------------------------------------
# Sort by VALUE (descending)
# --------------------------------------------

# fruits = dict(
#     sorted(
#         fruits.items(),
#         key=lambda item: item[1],
#         reverse=True
#     )
# )


print(fruits)


# ============================================
# 📌 DICTIONARY `items()`
# ============================================

# fruits.items() gives key-value pairs:
#
# ("banana", 105)
# ("apple", 72)
# ("orange", 73)
# ("coconut", 354)
#
#
# item[0] → KEY
# item[1] → VALUE
#
# Therefore:
#
# key=lambda item: item[0]
# → Sort by key
#
# key=lambda item: item[1]
# → Sort by value


# ============================================
# 📌 IMPORTANT
# ============================================

# .sort()
# → Changes original list
# → List only
#
# sorted()
# → Returns a new sorted result
# → Works with many iterables
#
# reverse=True
# → Descending order
#
# key=
# → Decides what to sort by
#
#
# Example:
#
# sorted(fruits.items(), key=lambda x: x[1])
#
# x[0] → key
# x[1] → value
#
# ============================================