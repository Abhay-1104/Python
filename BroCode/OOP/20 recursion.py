# ============================================
# 📘 RECURSION IN PYTHON
# ============================================

# Recursion = A function that calls itself
# from within its own function.
#
# It helps break a complex problem into
# smaller and simpler problems.
#
# Two ways to solve problems:
#
# Iterative → Uses loops, usually faster
# Recursive → Function calls itself, often simpler
#
# Recursive functions MUST have a BASE CASE
# to stop the recursion.


# ============================================
# 1️⃣ WALKING STEPS
# ============================================

# ---------- ITERATIVE ----------

def walk(steps):
    for step in range(1, steps + 1):
        print(f"You take step #{step}")


# ---------- RECURSIVE ----------

def walk(steps):

    # Base case
    if steps == 0:
        return

    # Recursive call
    walk(steps - 1)

    print(f"You take step #{steps}")


walk(5)


# Output:
#
# You take step #1
# You take step #2
# You take step #3
# You take step #4
# You take step #5


# ============================================
# 📌 HOW RECURSION WORKS
# ============================================

# walk(3)
#     ↓
# walk(2)
#     ↓
# walk(1)
#     ↓
# walk(0) → STOP
#
# Then the functions return:
#
# print step #1
# print step #2
# print step #3


# ============================================
# 2️⃣ FACTORIAL
# ============================================

# Factorial:
#
# 5! = 5 × 4 × 3 × 2 × 1
#    = 120


# ---------- ITERATIVE ----------

def factorial(x):

    result = 1

    if x > 0:
        for i in range(1, x + 1):
            result *= i

    return result


print(factorial(5))


# ---------- RECURSIVE ----------

def factorial(x):

    # Base case
    if x == 1:
        return 1

    # Recursive case
    return x * factorial(x - 1)


print(factorial(5))


# Output:
# 120


# ============================================
# 📌 HOW FACTORIAL RECURSION WORKS
# ============================================

# factorial(5)
# → 5 * factorial(4)
#
# factorial(4)
# → 4 * factorial(3)
#
# factorial(3)
# → 3 * factorial(2)
#
# factorial(2)
# → 2 * factorial(1)
#
# factorial(1)
# → 1  ← BASE CASE
#
# Then:
#
# 2 × 1 = 2
# 3 × 2 = 6
# 4 × 6 = 24
# 5 × 24 = 120


# ============================================
# 📌 IMPORTANT
# ============================================

# Every recursive function needs:
#
# 1. Base Case
#    → Condition that stops recursion.
#
# 2. Recursive Case
#    → Function calls itself with a
#      smaller/simpler problem.
#
#
# Example:
#
# if x == 1:       ← Base case
#     return 1
#
# return x * factorial(x - 1)  ← Recursive case
#
#
# Remember:
# Recursion → Function calls itself.
# Base case → Stops recursion.
# Recursive case → Calls itself again.
# ============================================