# ============================================
# 📘 ITERABLES IN PYTHON
# ============================================

# Iterable = An object/collection that can return
# its elements one at a time, allowing it to be
# used in a loop.
#
# Common iterables:
# - List
# - Tuple
# - Set
# - String
# - Dictionary


# ============================================
# 1️⃣ EXAMPLES OF ITERABLES
# ============================================

my_list = [1, 2, 3, 4, 5]
my_tuple = (1, 2, 3, 4, 5)
my_set = {"apple", "orange", "banana", "coconut"}
my_name = "Bro Code"
my_dictionary = {"A": 1, "B": 2, "C": 3}


# ============================================
# 2️⃣ ITERATING OVER A LIST
# ============================================

for item in my_list:
    print(item)

# Output:
# 1
# 2
# 3
# 4
# 5


# ============================================
# 3️⃣ ITERATING OVER A DICTIONARY
# ============================================

# By default, looping through a dictionary
# gives its KEYS.

for key in my_dictionary:
    print(key)

# Output:
# A
# B
# C


# Get only VALUES using .values()

for value in my_dictionary.values():
    print(value)

# Output:
# 1
# 2
# 3


# Get both KEYS and VALUES using .items()

for key, value in my_dictionary.items():
    print(f"{key} = {value}")

# Output:
# A = 1
# B = 2
# C = 3


# ============================================
# 📌 IMPORTANT
# ============================================

# List   → [1, 2, 3]
# Tuple  → (1, 2, 3)
# Set    → {1, 2, 3}
# String → "Hello"
# Dict   → {"A": 1, "B": 2}
#
# All of these are iterable.
#
# Dictionary:
#
# for key in dictionary:
#     → keys
#
# dictionary.values()
#     → values
#
# dictionary.items()
#     → key-value pairs
#
# Remember:
# Iterable → Can be used with a `for` loop.
# ============================================