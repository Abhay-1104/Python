# ============================================
# 📘 LAMBDA FUNCTIONS IN PYTHON
# ============================================

# Lambda function = A small anonymous function.
#
# It is usually used for a short, one-time operation.
#
# Syntax:
#
# lambda parameters: expression
#
# A lambda can take multiple arguments but has
# only ONE expression.


# ============================================
# 1️⃣ BASIC LAMBDA
# ============================================

double = lambda x: x * 2

print(double(2))

# Output:
# 4


# ============================================
# 2️⃣ MULTIPLE PARAMETERS
# ============================================

add = lambda x, y: x + y

print(add(3, 4))

# Output:
# 7


# ============================================
# 3️⃣ FIND MAXIMUM
# ============================================

max_value = lambda x, y: x if x > y else y

print(max_value(6, 7))

# Output:
# 7


# ============================================
# 4️⃣ FIND MINIMUM
# ============================================

min_value = lambda x, y: x if x < y else y

print(min_value(9, 8))

# Output:
# 8


# ============================================
# 5️⃣ FULL NAME
# ============================================

full_name = lambda first, last: first + " " + last

print(full_name("Spongebob", "Squarepants"))

# Output:
# Spongebob Squarepants


# ============================================
# 6️⃣ CHECK EVEN NUMBER
# ============================================

is_even = lambda x: x % 2 == 0

print(is_even(5))

# Output:
# False


# ============================================
# 7️⃣ CHECK AGE
# ============================================

age_check = lambda age: True if age >= 18 else False

print(age_check(21))

# Output:
# True


# ============================================
# 📌 IMPORTANT
# ============================================

# Normal function:
#
# def double(x):
#     return x * 2
#
#
# Lambda:
#
# double = lambda x: x * 2
#
#
# Lambda is useful when:
# - Function is very small.
# - Function is needed temporarily.
# - Used with higher-order functions.
#
# Common functions used with lambda:
#
# sort()
# map()
# filter()
# reduce()
#
#
# Remember:
#
# lambda parameters: expression
#
# Lambda → anonymous + short + one expression
# ============================================