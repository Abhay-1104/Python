# ============================================
# 📘 ITERATORS IN PYTHON
# ============================================

# Iterator = An object that returns elements
# one at a time and remembers its position.
#
# An iterator must have:
#
# __iter__()
# → Returns the iterator object itself.
#
# __next__()
# → Returns the next item.
# → Raises StopIteration when no items remain.
#
# Iterators are commonly used with `for` loops.


# ============================================
# 1️⃣ IMPORT RANDOM
# ============================================

import random


# ============================================
# 2️⃣ CREATE ITERATOR CLASS
# ============================================

class Dice:

    def __init__(self, rolls):
        self.rolls = rolls
        self.count = 0


    # ----------------------------------------
    # __iter__()
    # ----------------------------------------

    def __iter__(self):
        return self


    # ----------------------------------------
    # __next__()
    # ----------------------------------------

    def __next__(self):

        if self.count < self.rolls:

            self.count += 1

            return random.randint(1, 6)

        else:
            raise StopIteration


# ============================================
# 3️⃣ CREATE OBJECT
# ============================================

dice = Dice(3)


# ============================================
# 4️⃣ ITERATE THROUGH OBJECT
# ============================================

for die in dice:
    print(die)


# Possible output:
#
# 4
# 2
# 6
#
# Each value is randomly generated between
# 1 and 6.


# ============================================
# 📌 HOW IT WORKS
# ============================================

# dice = Dice(3)
#
# count = 0
#
# for loop calls:
# __iter__()
#     ↓
# __next__()
#     ↓
# random number
#
# count = 1
#     ↓
# __next__()
#     ↓
# random number
#
# count = 2
#     ↓
# __next__()
#     ↓
# random number
#
# count = 3
#     ↓
# __next__()
#     ↓
# StopIteration
#     ↓
# Loop stops


# ============================================
# 📌 IMPORTANT
# ============================================

# __iter__()
# → Makes the object iterable.
#
# __next__()
# → Controls what value is returned next.
#
# StopIteration
# → Tells Python that iteration is finished.
#
# `for` loop automatically handles
# StopIteration.
#
#
# Remember:
#
# __iter__() → Get iterator
# __next__() → Get next value
# StopIteration → No more values
# ============================================