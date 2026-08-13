# ============================================
# 📘 USING THE CAR CLASS
# ============================================

# Import Car class from car.py

from car import Car


# ============================================
# 1️⃣ CREATING OBJECTS
# ============================================

car1 = Car("Mustang", 2024, "red", False)
car2 = Car("Corvette", 2025, "blue", True)
car3 = Car("Charger", 2026, "yellow", True)


# Each object has its own attributes.


# ============================================
# 2️⃣ ACCESSING ATTRIBUTES
# ============================================

print(car1.model)
print(car1.year)
print(car1.color)
print(car1.for_sale)

# Output:
# Mustang
# 2024
# red
# False


# ============================================
# 3️⃣ CALLING METHODS
# ============================================

car1.drive()

# Output:
# You drive the red Mustang


car1.stop()

# Output:
# You stop the red Mustang


car3.describe()

# Output:
# 2026 yellow Charger


# ============================================
# 📌 IMPORTANT
# ============================================

# Class:
# → Blueprint for objects.
#
# Object:
# → Instance of a class.
#
# Attribute:
# → Data stored inside an object.
#
# Method:
# → Function defined inside a class.
#
# Example:
#
# Car              → Class
# car1             → Object
# car1.model       → Attribute
# car1.drive()     → Method
#
# `self` refers to the current object.
# ============================================