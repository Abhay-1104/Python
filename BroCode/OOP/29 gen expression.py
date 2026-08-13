# ============================================
# 📘 GENERATOR EXPRESSIONS IN PYTHON
# ============================================

# Generator Expression = A compact way to create
# a generator without defining a function or
# using `yield`.
#
# Similar to list comprehension, but uses ()
# instead of [].
#
# Syntax:
#
# (expression for value in iterable if condition)
#
# List comprehension:
# [expression for value in iterable]
#
# Generator expression:
# (expression for value in iterable)
#
# Generator expressions produce values ONE AT
# A TIME, so they are memory efficient.


# ============================================
# 1️⃣ BASIC GENERATOR EXPRESSION
# ============================================

number = int(input("Enter a number to count up to: "))

counter = (count for count in range(1, number + 1))


for n in counter:
    print(n)


# Example:
#
# Input: 5
#
# Output:
# 1
# 2
# 3
# 4
# 5
#
#
# `counter` is a generator object.
# Values are generated only when needed.


# ============================================
# 2️⃣ READING FILE WITH GENERATOR EXPRESSION
# ============================================

file_path = "C:\\Users\\HP\\Desktop\\test.txt"

with open(file_path) as file:

    lines = (line.strip() for line in file)

    for line in lines:
        print(line)


# `line.strip()`
# → Removes extra whitespace and newline
#   characters.
#
# The file is processed one line at a time,
# making it memory efficient for large files.


# ============================================
# 3️⃣ GENERATOR EXPRESSION WITH CONDITION
# ============================================

number = int(input("Enter a number to square up to: "))

even_squares = (
    x**2
    for x in range(1, number + 1)
    if x % 2 == 0
)


for square in even_squares:
    print(square)


# Example:
#
# Input: 10
#
# Even numbers:
# 2, 4, 6, 8, 10
#
# Squares:
# 4, 16, 36, 64, 100
#
# Output:
# 4
# 16
# 36
# 64
# 100


# ============================================
# 📌 LIST COMPREHENSION vs GENERATOR EXPRESSION
# ============================================

# List comprehension:
#
# squares = [x**2 for x in range(1, 100)]
#
# → Creates and stores the entire list
#   in memory.


# Generator expression:
#
# squares = (x**2 for x in range(1, 100))
#
# → Produces values one at a time.
#
# → Uses less memory.


# ============================================
# 📌 IMPORTANT
# ============================================

# Generator expression:
#
# (expression for value in iterable
#              if condition)
#
#
# Uses:
# () → Generator expression
# [] → List comprehension
#
#
# Generator expressions:
# - Are concise.
# - Are memory efficient.
# - Produce values one at a time.
# - Do not require a separate function.
# - Do not require `yield`.
#
#
# Generator function:
#
# def numbers():
#     yield 1
#     yield 2
#
#
# Generator expression:
#
# numbers = (x for x in range(1, 3))
#
#
# Remember:
#
# List comprehension → [ ]
# Generator expression → ( )
#
# Generator expression = Simple + memory efficient
# ============================================