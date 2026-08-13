# ============================================
# 📘 ABSTRACT CLASSES IN PYTHON
# ============================================

# Abstract class = A class that cannot be instantiated
# directly and is meant to be inherited by other classes.
#
# Abstract methods = Methods declared in the parent class
# but implemented by the child classes.
#
# Uses:
# - Prevents creating objects of the abstract class.
# - Forces child classes to implement required methods.


# ============================================
# 1️⃣ ABSTRACT CLASS
# ============================================

from abc import ABC, abstractmethod


class Vehicle(ABC):

    @abstractmethod
    def go(self):
        pass

    @abstractmethod
    def stop(self):
        pass


# Vehicle is an abstract class.
#
# go() and stop() are abstract methods.
# They have no implementation in Vehicle.


# ============================================
# 2️⃣ CHILD CLASSES
# ============================================

class Car(Vehicle):

    def go(self):
        print("You drive the car")

    def stop(self):
        print("You stop the car")


class Motorcycle(Vehicle):

    def go(self):
        print("You ride the motorcycle")

    def stop(self):
        print("You stop the motorcycle")


class Boat(Vehicle):

    def go(self):
        print("You sail the boat")

    def stop(self):
        print("You anchor the boat")


# Each child class MUST implement:
# - go()
# - stop()
#
# Otherwise, the child class also remains abstract.


# ============================================
# 3️⃣ CREATING OBJECTS
# ============================================

car = Car()
motorcycle = Motorcycle()
boat = Boat()


car.go()
car.stop()

motorcycle.go()
motorcycle.stop()

boat.go()
boat.stop()


# ============================================
# 📌 IMPORTANT
# ============================================

# ABC
# → Base class used to create abstract classes.
#
# @abstractmethod
# → Makes a method abstract.
#
# pass
# → Used when no implementation is provided.
#
# Vehicle() ❌
# → Cannot create an object of an abstract class.
#
# Car() ✅
# → Can create an object because it implements
#   all abstract methods.


# Remember:
#
# Abstract Class
#      ↓
# Abstract Methods
#      ↓
# Child Classes MUST implement them
# ============================================