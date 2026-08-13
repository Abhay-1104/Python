# ============================================
# 📘 *ARGS AND **KWARGS
# ============================================

# *args → allows a function to accept multiple
#          positional arguments.
#
# **kwargs → allows a function to accept multiple
#            keyword arguments.
#
# `args` and `kwargs` are just common names.
# The important part is * and **.


# ============================================
# 1️⃣ *ARGS
# ============================================

def add(*nums):
    total = 0

    for num in nums:
        total += num

    return total


print(add(1, 2, 3, 4))

# Output:
# 10


# *args stores all positional arguments in a tuple.
#
# add(1, 2, 3, 4)
# → nums = (1, 2, 3, 4)


# ============================================
# 2️⃣ *ARGS Example
# ============================================

def display_name(*args):
    print("Hello", end=" ")

    for arg in args:
        print(arg, end=" ")


display_name("Dr.", "Spongebob", "Harold", "Squarepants", "III")

# Output:
# Hello Dr. Spongebob Harold Squarepants III


# ============================================
# 3️⃣ **KWARGS
# ============================================

# **kwargs stores multiple keyword arguments
# in a dictionary.

def print_address(**kwargs):
    for value in kwargs.values():
        print(value, end=" ")


print_address(
    street="123 Fake St.",
    pobox="P.O Box 777",
    city="Detroit",
    state="MI",
    zip="54321"
)

# Output:
# 123 Fake St. P.O Box 777 Detroit MI 54321


# kwargs:
#
# {
#     "street": "123 Fake St.",
#     "pobox": "P.O Box 777",
#     "city": "Detroit",
#     "state": "MI",
#     "zip": "54321"
# }


# ============================================
# 4️⃣ *ARGS + **KWARGS
# ============================================

def shipping_label(*args, **kwargs):

    # Positional arguments
    for arg in args:
        print(arg, end=" ")

    print()

    # Check if "apt" exists
    if "apt" in kwargs:
        print(f"{kwargs.get('street')} {kwargs.get('apt')}")

    # Check if "pobox" exists
    elif "pobox" in kwargs:
        print(f"{kwargs.get('street')}")
        print(f"{kwargs.get('pobox')}")

    else:
        print(f"{kwargs.get('street')}")

    print(f"{kwargs.get('city')}, "
          f"{kwargs.get('state')} {kwargs.get('zip')}")


shipping_label(
    "Dr.", "Spongebob", "Squarepants",
    street="123 Fake St.",
    pobox="PO box #1001",
    city="Detroit",
    state="MI",
    zip="54321"
)


# Output:
# Dr. Spongebob Squarepants
# 123 Fake St.
# PO box #1001
# Detroit, MI 54321


# ============================================
# 📌 IMPORTANT
# ============================================

# *args
# → Multiple POSITIONAL arguments
# → Stored as a TUPLE
#
# def func(*args):
#     ...


# **kwargs
# → Multiple KEYWORD arguments
# → Stored as a DICTIONARY
#
# def func(**kwargs):
#     ...


# Example:
#
# func(1, 2, 3)
# → args = (1, 2, 3)
#
# func(name="Abhay", age=19)
# → kwargs = {"name": "Abhay", "age": 19}


# Remember:
# *args   → tuple  → positional arguments
# **kwargs → dict   → keyword arguments
# ============================================