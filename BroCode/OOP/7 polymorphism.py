# ============================================
# 📘 POLYMORPHISM IN PYTHON
# ============================================

# Polymorphism = "Many forms"
#
# Poly  → Many
# Morphe → Form
#
# Polymorphism allows different objects to use
# the same method name but behave differently.
#
# Two common ways:
# 1. Inheritance
# 2. Duck Typing


# ============================================
# 1️⃣ ABSTRACT PARENT CLASS
# ============================================

from abc import ABC, abstractmethod


class Shape(ABC):

    @abstractmethod
    def area(self):
        pass


# Every child class must have an area() method.


# ============================================
# 2️⃣ DIFFERENT SHAPES
# ============================================

class Circle(Shape):

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2


class Square(Shape):

    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2


class Triangle(Shape):

    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return self.base * self.height * 0.5


# ============================================
# 3️⃣ INHERITANCE + POLYMORPHISM
# ============================================

class Pizza(Circle):

    def __init__(self, topping, radius):
        super().__init__(radius)
        self.topping = topping


# Pizza inherits area() from Circle.


# ============================================
# 4️⃣ POLYMORPHISM IN ACTION
# ============================================

shapes = [
    Circle(4),
    Square(5),
    Triangle(6, 7),
    Pizza("pepperoni", 15)
]


for shape in shapes:
    print(f"{shape.area()}cm²")


# Each object uses the same method:
#
# shape.area()
#
# But the behavior depends on the object:
#
# Circle   → Circle's area()
# Square   → Square's area()
# Triangle → Triangle's area()
# Pizza    → inherited Circle's area()
#
# This is POLYMORPHISM:
# Same method → different behavior.


# ============================================
# 📌 IMPORTANT
# ============================================

# Polymorphism = One interface, many forms.
#
# Inheritance:
# → Child classes share a common parent.
#
# Duck Typing:
# → If an object has the required method,
#   Python can use it regardless of its class.
#
# Example:
#
# for shape in shapes:
#     shape.area()
#
# Python doesn't need to know exactly which
# shape it is. It only needs an `area()` method.
#
# Remember:
# Same method → Different implementations
# ============================================