# ============================================
# 📘 super() IN PYTHON
# ============================================

# super() is used in a child class to call
# methods or the constructor of the parent class.
#
# It helps reuse parent class code instead of
# writing the same code again.


# ============================================
# 1️⃣ PARENT CLASS
# ============================================

class Shape:

    def __init__(self, color, is_filled):
        self.color = color
        self.is_filled = is_filled

    def describe(self):
        print(
            f"It is {self.color} and "
            f"{'filled' if self.is_filled else 'not filled'}"
        )


# ============================================
# 2️⃣ USING super() IN CHILD CLASS
# ============================================

# Actually inherit from Shape:
class Circle(Shape):

    def __init__(self, color, is_filled, radius):
        super().__init__(color, is_filled)
        self.radius = radius

    def describe(self):
        print(
            f"It is a circle with an area of "
            f"{3.14 * self.radius * self.radius}cm^2"
        )
        super().describe()


# `super().__init__(color, is_filled)`
# → Calls Shape's __init__().
#
# `super().describe()`
# → Calls Shape's describe() method.


# ============================================
# 3️⃣ SQUARE
# ============================================

class Square(Shape):

    def __init__(self, color, is_filled, width):
        super().__init__(color, is_filled)
        self.width = width

    def describe(self):
        print(
            f"It is a square with an area of "
            f"{self.width * self.width}cm^2"
        )
        super().describe()


# ============================================
# 4️⃣ TRIANGLE
# ============================================

class Triangle(Shape):

    def __init__(self, color, is_filled, width, height):
        super().__init__(color, is_filled)
        self.width = width
        self.height = height

    def describe(self):
        print(
            f"It is a triangle with an area of "
            f"{self.width * self.height / 2}cm^2"
        )
        super().describe()


# ============================================
# 5️⃣ CREATING OBJECTS
# ============================================

circle = Circle("red", True, 5)
square = Square("blue", False, 6)
triangle = Triangle("yellow", True, 7, 8)


# ============================================
# 6️⃣ CALLING METHODS
# ============================================

circle.describe()
square.describe()
triangle.describe()


# Example output:
#
# It is a circle with an area of 78.5cm^2
# It is red and filled
#
# It is a square with an area of 36cm^2
# It is blue and not filled
#
# It is a triangle with an area of 28.0cm^2
# It is yellow and filled


# ============================================
# 📌 IMPORTANT
# ============================================

# super().__init__()
# → Calls the parent constructor.
#
# super().method()
# → Calls a parent method.
#
# In this example:
#
# Circle → Shape
# Square → Shape
# Triangle → Shape
#
# The child classes add their own properties and
# behavior while reusing Shape's code with super().
#
# Remember:
# super() → access parent class functionality
# ============================================