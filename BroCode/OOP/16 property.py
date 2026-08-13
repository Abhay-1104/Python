# ============================================
# 📘 @property IN PYTHON
# ============================================

# @property allows a method to be accessed like
# an attribute.
#
# It is useful when we want to add logic when:
# - Reading a value   → Getter
# - Changing a value  → Setter
# - Deleting a value  → Deleter


# ============================================
# 1️⃣ RECTANGLE CLASS
# ============================================

class Rectangle:

    def __init__(self, width, height):
        self._width = width
        self._height = height


    # ========================================
    # GETTER
    # ========================================

    @property
    def width(self):
        return f"{self._width:.1f}cm"


    @property
    def height(self):
        return f"{self._height:.1f}cm"


    # ========================================
    # SETTER
    # ========================================

    @width.setter
    def width(self, new_width):
        if new_width > 0:
            self._width = new_width
        else:
            print("Width must be greater than zero")


    @height.setter
    def height(self, new_height):
        if new_height > 0:
            self._height = new_height
        else:
            print("Height must be greater than zero")


    # ========================================
    # DELETER
    # ========================================

    @width.deleter
    def width(self):
        del self._width
        print("Width has been deleted")


    @height.deleter
    def height(self):
        del self._height
        print("Height has been deleted")


# ============================================
# 2️⃣ CREATING OBJECT
# ============================================

rectangle = Rectangle(3, 4)


# ============================================
# 3️⃣ GETTER
# ============================================

print(rectangle.width)
print(rectangle.height)

# Output:
# 3.0cm
# 4.0cm
#
# We access width like an attribute:
#
# rectangle.width
#
# Even though width() is actually a method,
# @property allows us to use it without ().


# ============================================
# 4️⃣ SETTER
# ============================================

rectangle.width = 5
rectangle.height = 6

print(rectangle.width)
print(rectangle.height)

# Output:
# 5.0cm
# 6.0cm


# Invalid values:

rectangle.width = -2
rectangle.height = 0

# Output:
# Width must be greater than zero
# Height must be greater than zero


# ============================================
# 5️⃣ DELETER
# ============================================

del rectangle.width
del rectangle.height

# Output:
# Width has been deleted
# Height has been deleted


# ============================================
# 📌 IMPORTANT
# ============================================

# @property
# → Getter
# → Read the value like an attribute.
#
# @width.setter
# → Setter
# → Controls how width is changed.
#
# @width.deleter
# → Deleter
# → Controls how width is deleted.
#
#
# Example:
#
# rectangle.width
# → Getter
#
# rectangle.width = 5
# → Setter
#
# del rectangle.width
# → Deleter
#
#
# `_width` and `_height`
# → Conventionally treated as internal attributes.
#
# Remember:
# @property → Getter
# @name.setter → Setter
# @name.deleter → Deleter
# ============================================