# ============================================
# 📘 EXCEPTIONS IN PYTHON
# ============================================

# Exception = An event that interrupts the normal
# flow of a program.
#
# Common exceptions:
# - ZeroDivisionError → Dividing by zero
# - ValueError        → Invalid value
# - TypeError         → Invalid operation between types
#
# Exception handling uses:
# 1. try
# 2. except
# 3. finally


# ============================================
# 1️⃣ TRY
# ============================================

try:
    number = int(input("Enter a number: "))
    print(1 / number)


# ============================================
# 2️⃣ EXCEPT
# ============================================

except ZeroDivisionError:
    print("You can't divide by zero!")


except ValueError:
    print("Enter only numbers please!")


except Exception:
    print("Something went wrong!")


# ============================================
# 3️⃣ FINALLY
# ============================================

finally:
    print("Do some cleanup here")


# ============================================
# 📌 HOW IT WORKS
# ============================================

# try:
# → Code that might cause an exception.
#
# except:
# → Handles the exception if it occurs.
#
# finally:
# → Always executes, whether an exception
#   occurs or not.
#
#
# Example 1:
#
# Input: 10
# 1 / 10 → 0.1
#
#
# Example 2:
#
# Input: 0
# → ZeroDivisionError
# → "You can't divide by zero!"
#
#
# Example 3:
#
# Input: abc
# → ValueError
# → "Enter only numbers please!"


# ============================================
# 📌 IMPORTANT
# ============================================

# Multiple except blocks can be used to handle
# different types of exceptions.
#
# `except Exception` is a general fallback for
# unexpected exceptions.
#
# `finally` is commonly used for cleanup tasks,
# such as closing files or releasing resources.
#
#
# Remember:
#
# try     → Try risky code
# except  → Handle errors
# finally → Always execute
# ============================================