# ============================================
# 📘 INHERITANCE IN PYTHON
# ============================================

# Inheritance allows a child class to inherit
# attributes and methods from a parent class.
#
# Syntax:
# class Child(Parent):
#
# Benefits:
# - Code reusability
# - Less duplicate code
# - Easy to extend classes


# ============================================
# 1️⃣ PARENT CLASS
# ============================================

class Animal:

    def __init__(self, name):
        self.name = name
        self.alive = True

    def eat(self):
        print(f"{self.name} is eating")

    def sleep(self):
        print(f"{self.name} is asleep")


# Animal is the PARENT class.
#
# It provides:
# - name
# - alive
# - eat()
# - sleep()


# ============================================
# 2️⃣ CHILD CLASSES
# ============================================

class Dog(Animal):

    def speak(self):
        print("WOOF!")


class Cat(Animal):

    def speak(self):
        print("MEOW!")


class Mouse(Animal):

    def speak(self):
        print("SQUEEK!")


# Dog, Cat, and Mouse inherit from Animal.
#
# They automatically get:
# - name
# - alive
# - eat()
# - sleep()
#
# They also have their own speak() method.


# ============================================
# 3️⃣ CREATING OBJECTS
# ============================================

dog = Dog("Scooby")
cat = Cat("Garfield")
mouse = Mouse("Mickey")


# ============================================
# 4️⃣ USING INHERITED METHODS
# ============================================

dog.eat()
cat.sleep()
mouse.eat()

# Output:
# Scooby is eating
# Garfield is asleep
# Mickey is eating


# ============================================
# 5️⃣ USING CHILD METHODS
# ============================================

dog.speak()
cat.speak()
mouse.speak()

# Output:
# WOOF!
# MEOW!
# SQUEEK!


# ============================================
# 📌 IMPORTANT
# ============================================

# Parent class → Animal
#
# Child classes → Dog, Cat, Mouse
#
# Dog("Scooby")
# → Dog inherits Animal's __init__()
#
# dog.eat()
# → inherited from Animal
#
# dog.speak()
# → defined inside Dog
#
# Remember:
# class Child(Parent):
#     ...
#
# Child can use the attributes and methods
# inherited from Parent.
# ============================================