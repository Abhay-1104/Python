# ============================================
# 📘 DECORATORS IN PYTHON
# ============================================

# Decorator = A function that extends the behavior
# of another function WITHOUT modifying the
# original function.
#
# A decorator takes a function as an argument
# and returns a new function with extra behavior.
#
# Syntax:
#
# @decorator
# def function():
#     ...


# ============================================
# 1️⃣ SPRINKLES DECORATOR
# ============================================

def add_sprinkles(func):

    def wrapper(*args, **kwargs):
        print("*You add sprinkles 🎊*")
        func(*args, **kwargs)

    return wrapper


# ============================================
# 2️⃣ FUDGE DECORATOR
# ============================================

def add_fudge(func):

    def wrapper(*args, **kwargs):
        print("*You add fudge 🍫*")
        func(*args, **kwargs)

    return wrapper


# ============================================
# 3️⃣ APPLYING DECORATORS
# ============================================

@add_sprinkles
@add_fudge
def get_ice_cream(flavor):
    print(f"Here is your {flavor} ice cream 🍨")


# Multiple decorators are applied from
# BOTTOM → TOP.
#
# First:
# @add_fudge
#
# Then:
# @add_sprinkles


# ============================================
# 4️⃣ CALLING FUNCTION
# ============================================

get_ice_cream("vanilla")


# Output:
#
# *You add sprinkles 🎊*
# *You add fudge 🍫*
# Here is your vanilla ice cream 🍨


# ============================================
# 📌 IMPORTANT
# ============================================

# `@add_sprinkles`
# → Adds sprinkles behavior.
#
# `@add_fudge`
# → Adds fudge behavior.
#
# `wrapper(*args, **kwargs)`
# → Allows the decorator to work with functions
#   having different arguments.
#
# `func(*args, **kwargs)`
# → Calls the original function.
#
#
# Without @ syntax:
#
# get_ice_cream = add_sprinkles(
#     add_fudge(get_ice_cream)
# )
#
#
# Remember:
# Decorator → Adds extra behavior to a function
#             without changing its original code.
# ============================================