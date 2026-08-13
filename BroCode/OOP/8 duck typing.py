# ============================================
# 📘 DUCK TYPING IN PYTHON
# ============================================

# Duck Typing = A way to achieve polymorphism
# without requiring inheritance.
#
# Python focuses on what an object CAN DO,
# rather than what class it belongs to.
#
# "If it looks like a duck and quacks like a duck,
# it must be a duck."


# ============================================
# 1️⃣ PARENT CLASS
# ============================================

class Animal:
    alive = True


# ============================================
# 2️⃣ CHILD CLASSES
# ============================================

class Dog(Animal):

    def speak(self):
        print("WOOF!")


class Cat(Animal):

    def speak(self):
        print("MEOW!")


# ============================================
# 3️⃣ UNRELATED CLASS
# ============================================

class Car:

    alive = True

    def speak(self):
        print("HONK!")


# Car does NOT inherit from Animal.
#
# But Car has the required:
# - speak()
# - alive


# ============================================
# 4️⃣ DUCK TYPING IN ACTION
# ============================================

animals = [Dog(), Cat(), Car()]

for animal in animals:
    animal.speak()
    print(animal.alive)


# Output:
#
# WOOF!
# True
# MEOW!
# True
# HONK!
# True


# ============================================
# 📌 IMPORTANT
# ============================================

# Dog → has speak() and alive
# Cat → has speak() and alive
# Car → has speak() and alive
#
# Even though Car is NOT an Animal,
# the loop can still use it because it has
# the required attributes and methods.
#
# This is Duck Typing.
#
# In simple words:
# "Don't care what the object IS,
#  care about what the object CAN DO."
#
# Remember:
# Duck Typing → Focuses on behavior,
# not the object's class/type.
# ============================================