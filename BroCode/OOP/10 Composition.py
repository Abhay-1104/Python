# ============================================
# 📘 AGGREGATION vs COMPOSITION
# ============================================

# Aggregation:
# → One object contains references to other
#   INDEPENDENT objects.
# → "HAS-A" relationship.
#
# Composition:
# → One object directly OWNS its components.
# → Components depend on the main object.
# → "OWNS-A" relationship.


# ============================================
# 1️⃣ ENGINE CLASS
# ============================================

class Engine:

    def __init__(self, hp):
        self.hp = hp


# ============================================
# 2️⃣ WHEEL CLASS
# ============================================

class Wheel:

    def __init__(self, size):
        self.size = size


# ============================================
# 3️⃣ CAR CLASS
# ============================================

class Car:

    def __init__(self, make, model, hp, ws):
        self.make = make
        self.model = model

        # Composition:
        # Car creates its own Engine object.
        self.engine = Engine(hp)

        # Composition:
        # Car creates its own Wheel objects.
        self.wheels = [Wheel(ws) for _ in range(4)]

    def display_car(self):
        return (
            f"{self.make} {self.model} "
            f"{self.engine.hp}(hp) "
            f"{self.wheels[0].size}in"
        )


# ============================================
# 4️⃣ CREATING CAR OBJECTS
# ============================================

car1 = Car("Ford", "Mustang", 500, 18)
car2 = Car("Chevrolet", "Corvette", 670, 19)


# ============================================
# 5️⃣ DISPLAYING INFORMATION
# ============================================

print(car1.display_car())
print(car2.display_car())

# Output:
#
# Ford Mustang 500(hp) 18in
# Chevrolet Corvette 670(hp) 19in


# ============================================
# 📌 COMPOSITION IN THIS EXAMPLE
# ============================================

# Car creates Engine:
#
# self.engine = Engine(hp)
#
# Car creates 4 Wheels:
#
# self.wheels = [Wheel(ws) for _ in range(4)]
#
# Engine and Wheel objects are created INSIDE
# the Car object.
#
# Therefore:
#
# Car → OWNS → Engine
# Car → OWNS → Wheels
#
# This is COMPOSITION.


# ============================================
# 📌 AGGREGATION vs COMPOSITION
# ============================================

# AGGREGATION:
# → HAS-A
# → Objects can exist independently.
#
# Example:
# Library HAS-A Book
#
# book = Book(...)
# library.add_book(book)


# COMPOSITION:
# → OWNS-A
# → Components are created/owned by the
#   main object.
#
# Example:
# Car OWNS-A Engine
# Car OWNS-A Wheels
#
#
# Easy way to remember:
#
# Aggregation  → HAS-A
# Composition  → OWNS-A
# ============================================