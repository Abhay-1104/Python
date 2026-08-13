# ============================================
# 📘 MATCH-CASE STATEMENT IN PYTHON
# ============================================

# match-case is similar to a switch statement in
# other programming languages.
#
# It is useful when we need to compare one value
# with multiple possible cases.
#
# Syntax:
#
# match value:
#     case value1:
#         # code
#     case value2:
#         # code
#     case _:
#         # default case


# ============================================
# 1️⃣ BASIC EXAMPLE
# ============================================

def is_weekend(day):

    match day:
        case "Saturday" | "Sunday":
            return True

        case "Monday" | "Tuesday" | "Wednesday" | "Thursday" | "Friday":
            return False

        case _:
            return False


print(is_weekend("Monday"))

# Output:
# False


# ============================================
# 🔹 `case _`
# ============================================

# `_` is the default case.
# It runs when none of the previous cases match.
#
# Example:
#
# is_weekend("Holiday")
# → No case matches
# → case _ runs
# → False


# ============================================
# 🔹 `|` OR OPERATOR IN MATCH-CASE
# ============================================

# `|` allows multiple values in the same case.
#
# case "Saturday" | "Sunday":
#
# Means:
# Saturday OR Sunday
#
# So:
#
# is_weekend("Saturday") → True
# is_weekend("Sunday")   → True
# is_weekend("Monday")   → False


# ============================================
# 📌 IMPORTANT
# ============================================

# match → value we want to compare
# case  → possible matching value
# _     → default case
# |     → match multiple values (OR)
#
# match-case can make code cleaner and easier
# to read than using many `if-elif` statements.
#
# ⚠️ `match-case` was introduced in Python 3.10.
# ============================================