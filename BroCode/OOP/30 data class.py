# ============================================
# 📘 DATA CLASSES IN PYTHON
# ============================================

# Data Class = A special type of class mainly
# used for storing data.
#
# It reduces boilerplate code compared to a
# normal class.
#
# @dataclass automatically provides:
#
# __init__() → Creates the object
# __repr__() → Provides a readable object output
# __eq__()   → Compares objects based on their data
#
# Available from Python 3.7+.


# ============================================
# 1️⃣ IMPORT DATACLASS
# ============================================

from dataclasses import dataclass, field


# ============================================
# 2️⃣ CREATE DATA CLASS
# ============================================

@dataclass
class Person:

    name: str
    age: int
    password: str = field(repr=False)
    is_alive: bool = True


# Type hints:
#
# name: str
# → name should contain a string.
#
# age: int
# → age should contain an integer.
#
# password: str
# → password should contain a string.
#
# is_alive: bool = True
# → Default value is True.


# ============================================
# 3️⃣ field(repr=False)
# ============================================

# `repr=False` prevents the password from
# appearing when the object is printed.
#
# Example:
#
# print(person1)
#
# Password will NOT be displayed.


# ============================================
# 4️⃣ __post_init__()
# ============================================

@dataclass
class Person:

    name: str
    age: int
    password: str = field(repr=False)
    is_alive: bool = True

    def __post_init__(self):

        if self.age < 0:
            raise ValueError("Age cannot be negative")


# __post_init__()
# → Automatically runs after the generated
#   __init__() method.
#
# It is useful for validation or additional
# initialization.


# ============================================
# 5️⃣ CREATE OBJECTS
# ============================================

person1 = Person("Spongebob", 30, "pineapple1")
person2 = Person("Patrick", 35, "password")


# ============================================
# 6️⃣ PRINT OBJECTS
# ============================================

print(person1)
print(person2)

# Output:
#
# Person(name='Spongebob', age=30, is_alive=True)
# Person(name='Patrick', age=35, is_alive=True)
#
# Password is hidden because:
#
# field(repr=False)


# ============================================
# 7️⃣ COMPARE OBJECTS
# ============================================

print(person1 == person2)

# Output:
# False
#
# @dataclass automatically provides __eq__()
# which compares the values of the fields.


# ============================================
# 📌 IMPORTANT
# ============================================

# @dataclass
# → Automatically generates common methods.
#
# __init__()
# → Initializes object attributes.
#
# __repr__()
# → Gives a readable representation.
#
# __eq__()
# → Compares two objects.
#
# field(repr=False)
# → Hides a field from printed representation.
#
# __post_init__()
# → Runs automatically after __init__().
#
#
# Remember:
#
# Data Class → Mainly for storing data
# @dataclass → Less boilerplate code
# __post_init__ → Extra validation/setup
# ============================================