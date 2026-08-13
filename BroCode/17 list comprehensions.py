# ============================================
# 📘 LIST COMPREHENSION IN PYTHON
# ============================================

# List comprehension = A concise way to create lists.
#
# Syntax:
# [expression for value in iterable if condition]
#
# It is shorter and cleaner than using a traditional
# for loop.


# ============================================
# 1️⃣ BASIC EXAMPLE
# ============================================

doubles = [x * 2 for x in range(1, 11)]
triples = [y * 3 for y in range(1, 11)]
squares = [z * z for z in range(1, 11)]

print(doubles)
print(triples)
print(squares)


# Example:
# [x * 2 for x in range(1, 6)]
#
# x = 1 → 2
# x = 2 → 4
# x = 3 → 6
# ...
#
# Result:
# [2, 4, 6, 8, 10]


# ============================================
# 2️⃣ LIST COMPREHENSION WITH STRINGS
# ============================================

fruits = ["apple", "orange", "banana", "coconut"]

uppercase_words = [fruit.upper() for fruit in fruits]
fruit_chars = [fruit[0] for fruit in fruits]

print(uppercase_words)
# ['APPLE', 'ORANGE', 'BANANA', 'COCONUT']

print(fruit_chars)
# ['a', 'o', 'b', 'c']


# ============================================
# 3️⃣ LIST COMPREHENSION WITH CONDITION
# ============================================

numbers = [1, -2, 3, -4, 5, -6, 8, -7]

positive_numbers = [x for x in numbers if x >= 0]
negative_numbers = [x for x in numbers if x < 0]

even_numbers = [x for x in numbers if x % 2 == 0]
odd_numbers = [x for x in numbers if x % 2 == 1]


# positive_numbers:
# [1, 3, 5, 8]
#
# negative_numbers:
# [-2, -4, -6, -7]
#
# even_numbers:
# [-2, -4, -6, 8]
#
# odd_numbers:
# [1, 3, 5, -7]


# ============================================
# 4️⃣ FILTERING GRADES
# ============================================

grades = [85, 42, 79, 90, 56, 61, 30]

passing_grades = [grade for grade in grades if grade >= 60]

print(passing_grades)

# Output:
# [85, 79, 90, 61]


# ============================================
# 📌 IMPORTANT
# ============================================

# Without list comprehension:
#
# squares = []
#
# for x in range(1, 6):
#     squares.append(x * x)
#
#
# With list comprehension:
#
# squares = [x * x for x in range(1, 6)]
#
#
# Structure:
#
# [expression  for  value  in  iterable  if condition]
#     ↑           ↑          ↑              ↑
#   result     variable    source         filter
#
#
# Examples:
#
# [x * 2 for x in range(5)]
# → Transform each value
#
# [x for x in numbers if x > 0]
# → Filter values
#
# ============================================