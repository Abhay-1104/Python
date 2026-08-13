# ============================================
# 📘 zip() IN PYTHON
# ============================================

# zip() = Combines multiple iterables into a
# single iterator of tuples.
#
# It is useful when we want to work with
# corresponding elements from multiple lists.
#
# Syntax:
#
# zip(iterable1, iterable2, iterable3, ...)


# ============================================
# 1️⃣ EXAMPLE
# ============================================

names = ["Spongebob", "Patrick", "Squidward"]
ages = [30, 35, 50]
jobs = ["Cook", "Unemployed", "Cashier"]


# Combine the lists
data = zip(names, ages, jobs)


# ============================================
# 2️⃣ LOOP THROUGH ZIP
# ============================================

for name, age, job in data:
    print(f"{name} is a {age} year old {job}")


# Output:
#
# Spongebob is a 30 year old Cook
# Patrick is a 35 year old Unemployed
# Squidward is a 50 year old Cashier


# ============================================
# 📌 HOW zip() WORKS
# ============================================

# names:
# Spongebob    Patrick    Squidward
#
# ages:
# 30           35         50
#
# jobs:
# Cook         Unemployed Cashier
#
# zip() combines them:
#
# ("Spongebob", 30, "Cook")
# ("Patrick", 35, "Unemployed")
# ("Squidward", 50, "Cashier")


# ============================================
# 📌 IMPORTANT
# ============================================

# zip() returns an iterator of tuples.
#
# It combines elements based on their position.
#
# If iterables have different lengths,
# zip() stops when the SHORTEST iterable ends.
#
# Example:
#
# a = [1, 2, 3]
# b = ["a", "b"]
#
# list(zip(a, b))
#
# [(1, "a"), (2, "b")]
#
#
# Remember:
# zip() → Combine corresponding elements
#         from multiple iterables.
# ============================================