# ============================================
# 📘 DEFAULT & KEYWORD ARGUMENTS
# ============================================

# ============================================
# 1️⃣ DEFAULT ARGUMENTS
# ============================================

# A default argument has a predefined value.
# If no value is passed, the default value is used.

def net_price(list_price, discount=0, tax=0.05):
    return list_price * (1 - discount) * (1 - tax)


print(net_price(500))          # discount=0, tax=0.05
print(net_price(500, 0.1))     # discount=0.1, tax=0.05
print(net_price(500, 0.1, 0))  # discount=0.1, tax=0


# Default parameters must come after
# parameters without default values.
#
# ✅ def func(a, b=10)
# ❌ def func(a=10, b)


# ============================================
# 2️⃣ KEYWORD ARGUMENTS
# ============================================

# Keyword arguments are passed using parameter names.
# Order does not matter and improves readability.

def hello(greeting, title, first, last):
    print(f"{greeting} {title}{first} {last}")


hello("Hello", title="Mr.", last="John", first="James")


# Positional argument:
# hello("Hello", ...)
#
# Keyword arguments:
# title="Mr."
# last="John"
# first="James"


# ============================================
# 3️⃣ POSitional + KEYWORD ARGUMENTS
# ============================================

def student(name, age, branch):
    print(name, age, branch)


student("Abhay", age=19, branch="IoT")


# ✅ Positional arguments must come BEFORE
#    keyword arguments.
#
# ❌ student(name="Abhay", 19, branch="IoT")


# ============================================
# 4️⃣ `sep` AND `end`
# ============================================

# `end` → controls what print() ends with
for number in range(1, 6):
    print(number, end=" ")

print()


# Output:
# 1 2 3 4 5


# `sep` → controls what comes between values
print("1", "2", "3", sep="-")

# Output:
# 1-2-3


# ============================================
# 5️⃣ EXAMPLE
# ============================================

def get_phone(country, area, first, last):
    return f"{country}-{area}-{first}-{last}"


phone_num = get_phone(
    country=1,
    area=123,
    first=456,
    last=7890
)

print(phone_num)

# Output:
# 1-123-456-7890


# ============================================
# 📌 IMPORTANT
# ============================================

# Default Argument:
# → Value is defined in the function definition.
#
# def count(end, start=0):
#                       ↑
#                  default value
#
#
# Keyword Argument:
# → Parameter name is used while calling the function.
#
# count(end=10, start=5)
#
#
# Remember:
# DEFAULT  → value given while DEFINING
# KEYWORD  → name given while CALLING
# ============================================