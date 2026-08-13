# ============================================
# 📘 MULTIPLE & MULTILEVEL INHERITANCE
# ============================================

# Multiple Inheritance:
# A class inherits from MORE THAN ONE parent class.
#
# Syntax:
# class C(A, B):
#
#
# Multilevel Inheritance:
# A class inherits from a class which itself
# inherits from another class.
#
# Example:
# C(B) ← B(A) ← A


# ============================================
# 1️⃣ PARENT CLASS
# ============================================

class Animal:

    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f"{self.name} is eating")

    def sleep(self):
        print(f"{self.name} is sleeping")


# ============================================
# 2️⃣ CHILD CLASSES
# ============================================

class Prey(Animal):

    def flee(self):
        print(f"{self.name} is fleeing")


class Predator(Animal):

    def hunt(self):
        print(f"{self.name} is hunting")


# ============================================
# 3️⃣ MULTILEVEL INHERITANCE
# ============================================

class Rabbit(Prey):
    pass


class Hawk(Predator):
    pass


# Rabbit → Prey → Animal
# Hawk   → Predator → Animal
#
# Rabbit gets:
# - name
# - eat()
# - sleep()
# - flee()
#
# Hawk gets:
# - name
# - eat()
# - sleep()
# - hunt()


# ============================================
# 4️⃣ MULTIPLE INHERITANCE
# ============================================

class Fish(Prey, Predator):
    pass


# Fish inherits from BOTH:
# Prey and Predator
#
# Therefore Fish gets:
# - eat()
# - sleep()
# - flee()
# - hunt()


# ============================================
# 5️⃣ CREATING OBJECTS
# ============================================

rabbit = Rabbit("Bugs")
hawk = Hawk("Tony")
fish = Fish("Nemo")


# ============================================
# 6️⃣ USING INHERITED METHODS
# ============================================

rabbit.eat()
rabbit.flee()

hawk.sleep()
hawk.hunt()

fish.eat()
fish.flee()
fish.hunt()


# ============================================
# 📌 IMPORTANT
# ============================================

# MULTILEVEL:
#
# Animal
#   ↓
# Prey
#   ↓
# Rabbit
#
# Rabbit inherits from Prey,
# and Prey inherits from Animal.


# MULTIPLE:
#
#        Prey    Predator
#          ↘      ↙
#            Fish
#
# Fish inherits from both Prey and Predator.
#
#
# Remember:
#
# Multiple:
# class C(A, B):
#
# Multilevel:
# class C(B):
#     B inherits from A
# ============================================