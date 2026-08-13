# ============================================
# 📘 FUNCTIONS IN PYTHON
# ============================================
#
# A function is a reusable block of code that performs
# a specific task.
#
# Instead of writing the same code multiple times,
# we can define a function once and call it whenever
# we need it.
#
# Syntax:
#
# def function_name(parameters):
#     # code to execute
#     return value
#
# Important Points:
# - `def` is used to define a function.
# - Parameters are variables given to a function.
# - Arguments are the actual values passed to the function.
# - `return` sends a value back from the function.
# - A function is executed only when it is called.
#
# ============================================
# 1️⃣ EXAMPLE 1 — Function with Parameters
# ============================================

def display_invoice(username, amount, due_date):
    print(f"Hello {username}")
    print(f"Your bill of ${amount:.2f} is due: {due_date}")


# Calling the function
display_invoice("BroCode", 42.50, "01/01")
display_invoice("JoeSchmo", 100.01, "01/02")


# Output:
#
# Hello BroCode
# Your bill of $42.50 is due: 01/01
#
# Hello JoeSchmo
# Your bill of $100.01 is due: 01/02


# --------------------------------------------
# 🔹 Explanation
# --------------------------------------------
#
# def display_invoice(username, amount, due_date):
#
# `def`:
#     Keyword used to define a function.
#
# `display_invoice`:
#     Name of the function.
#
# `username`, `amount`, `due_date`:
#     These are PARAMETERS of the function.
#
# When we call:
#
# display_invoice("BroCode", 42.50, "01/01")
#
# The values are passed to the parameters:
#
# username  → "BroCode"
# amount    → 42.50
# due_date  → "01/01"
#
# Therefore, the function executes:
#
# print(f"Hello {username}")
# → Hello BroCode
#
# print(f"Your bill of ${amount:.2f} is due: {due_date}")
# → Your bill of $42.50 is due: 01/01
#
#
# ============================================
# 🔹 Parameters vs Arguments
# ============================================
#
# Parameters:
#     Variables written inside the function definition.
#
# Example:
#
# def display_invoice(username, amount, due_date):
#                      ↑         ↑       ↑
#                  parameters
#
#
# Arguments:
#     Actual values passed when calling the function.
#
# Example:
#
# display_invoice("BroCode", 42.50, "01/01")
#                   ↑        ↑      ↑
#                arguments
#
#
# ============================================
# 🔹 Formatting Numbers with :.2f
# ============================================
#
# In:
#
# f"${amount:.2f}"
#
# `.2f` means:
#     Display the number as a floating-point number
#     with exactly 2 digits after the decimal point.
#
# Example:
#
# amount = 42.5
# print(f"${amount:.2f}")
#
# Output:
# $42.50
#
# Another example:
#
# amount = 100.01
# print(f"${amount:.2f}")
#
# Output:
# $100.01
#
#
# ============================================
# 2️⃣ EXAMPLE 2 — Function with Return Value
# ============================================
#
# A function can return a value using the `return`
# statement.
#
# Example:

def create_name(first, last):
    first = first.capitalize()
    last = last.capitalize()

    return first + " " + last


full_name = create_name("spongebob", "squarepants")

print(full_name)


# Output:
#
# Spongebob Squarepants


# --------------------------------------------
# 🔹 Explanation
# --------------------------------------------
#
# def create_name(first, last):
#
# The function accepts two parameters:
#
# first → first name
# last  → last name
#
#
# first = first.capitalize()
#
# `.capitalize()` converts the first character
# to uppercase and the remaining characters
# to lowercase.
#
# Example:
#
# "spongebob".capitalize()
# → "Spongebob"
#
#
# last = last.capitalize()
#
# "squarepants".capitalize()
# → "Squarepants"
#
#
# return first + " " + last
#
# `return` sends the result back to the place
# where the function was called.
#
# The result becomes:
#
# "Spongebob" + " " + "Squarepants"
# → "Spongebob Squarepants"
#
#
# ============================================
# 🔹 Storing the Returned Value
# ============================================
#
# We can store the returned value in a variable:
#
# full_name = create_name("spongebob", "squarepants")
#
# The function returns:
#
# "Spongebob Squarepants"
#
# So:
#
# full_name = "Spongebob Squarepants"
#
# Then:
#
# print(full_name)
#
# Output:
#
# Spongebob Squarepants
#
#
# ============================================
# 3️⃣ FUNCTION WITHOUT RETURN
# ============================================
#
# A function doesn't always need to return a value.
#
# Example:

def greet(name):
    print(f"Hello {name}")


greet("Abhay")


# Output:
# Hello Abhay
#
# This function performs an action (printing),
# but it does not return a value.
#
#
# ============================================
# 4️⃣ FUNCTION WITH RETURN
# ============================================
#
# A function can calculate something and return
# the result.

def add(a, b):
    return a + b


result = add(10, 20)

print(result)


# Output:
# 30
#
# Here:
#
# a = 10
# b = 20
#
# return a + b
# → return 30
#
# Therefore:
#
# result = 30
#
#
# ============================================
# 5️⃣ IMPORTANT DIFFERENCE: print vs return
# ============================================
#
# `print()`:
#     Displays something on the screen.
#
# `return`:
#     Sends a value back from the function.
#
# Example:

def using_print(a, b):
    print(a + b)


def using_return(a, b):
    return a + b


using_print(10, 20)
# Output:
# 30


result = using_return(10, 20)

print(result)
# Output:
# 30
#
# The returned value can be stored and used later.
#
#
# ============================================
# 6️⃣ FUNCTION CALL
# ============================================
#
# Defining a function does NOT execute it.
#
# Example:

def say_hello():
    print("Hello!")


# Nothing is printed yet.
#
# The function runs only when we call it:

say_hello()

# Output:
# Hello!
#
#
# ============================================
# 📌 IMPORTANT POINTS TO REMEMBER
# ============================================
#
# 1. Use `def` to create a function.
#
# 2. A function contains reusable code.
#
# 3. Parameters are variables in the function definition.
#
# 4. Arguments are actual values passed to the function.
#
# 5. Use `return` to send a value back from a function.
#
# 6. `print()` displays a value but does not return it.
#
# 7. A function must be called to execute its code.
#
# 8. A function can have zero, one, or multiple parameters.
#
# 9. A function can return any type of value:
#    - int
#    - float
#    - string
#    - list
#    - tuple
#    - dictionary
#    - etc.
#
# 10. Functions help make programs:
#     - Reusable
#     - Organized
#     - Easier to understand
#     - Easier to maintain
#
# ============================================
# END OF FUNCTIONS NOTES
# ============================================