# ============================================
# 📘 CLASSES & OBJECTS IN PYTHON
# ============================================

# A class is a blueprint for creating objects.
#
# Object = An instance of a class.
#
# Example:
# Car → class
# car1, car2, car3 → objects


# ============================================
# 1️⃣ CREATING A CLASS
# ============================================

class Car:

    # Constructor
    def __init__(self, model, year, color, for_sale):
        self.model = model
        self.year = year
        self.color = color
        self.for_sale = for_sale

    # Method
    def drive(self):
        print(f"You drive the {self.color} {self.model}")

    def stop(self):
        print(f"You stop the {self.color} {self.model}")

    def describe(self):
        print(f"{self.year} {self.color} {self.model}")


# ============================================
# 📌 IMPORTANT
# ============================================

# __init__() → Constructor
# Runs automatically when an object is created.
#
# self → Refers to the current object.
#
# self.model, self.year, etc. → Attributes
# belonging to the object.
#
# drive(), stop(), describe() → Methods
# (functions inside a class).