# ============================================
# 📘 PYTHON VARIABLE SCOPE (LEGB RULE)
# ============================================

# Scope = The region where a variable can be accessed.
#
# Python follows the LEGB rule:
#
# L → Local
# E → Enclosed
# G → Global
# B → Built-in
#
# Python searches for a variable in this order:
# Local → Enclosed → Global → Built-in


# ============================================
# 1️⃣ LOCAL SCOPE
# ============================================

def func1():
    x = 1
    print(x)


def func2():
    x = 2
    print(x)


func1()
func2()

# Output:
# 1
# 2
#
# `x` inside each function is LOCAL to that function.
# They are separate variables.


# ============================================
# 2️⃣ ENCLOSED SCOPE
# ============================================

def func1():
    x = 1

    def func2():
        print(x)

    func2()


func1()

# Output:
# 1
#
# `x` belongs to the outer function (func1)
# and is accessible inside the inner function (func2).
#
# This is called ENCLOSED scope.


# ============================================
# 3️⃣ GLOBAL SCOPE
# ============================================

def func1():
    print(x)


def func2():
    print(x)


x = 3

func1()
func2()

# Output:
# 3
# 3
#
# `x` is defined outside all functions,
# so it has GLOBAL scope.
#
# Functions can read a global variable.


# ============================================
# 4️⃣ BUILT-IN SCOPE
# ============================================

from math import e


def func1():
    print(e)


func1()

# Output:
# 2.718281828459045
#
# `e` is available from the imported math module.
# Python can access names provided by built-in/imported
# environments when they aren't found in local,
# enclosed, or global scope.


# ============================================
# 📌 LEGB RULE
# ============================================

# L → Local
#     Variable inside the current function.
#
# E → Enclosed
#     Variable in an outer function.
#
# G → Global
#     Variable defined outside functions.
#
# B → Built-in
#     Python's built-in names/functions.
#
#
# Example:
#
# x = 10          # Global
#
# def outer():
#     x = 20      # Enclosed
#
#     def inner():
#         x = 30  # Local
#         print(x)
#
#     inner()
#
# inner() finds x in Local first.
#
# ============================================