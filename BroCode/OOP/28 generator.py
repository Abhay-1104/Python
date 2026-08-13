# ============================================
# 📘 GENERATORS IN PYTHON
# ============================================

# Generator = A function that behaves like an
# iterator and produces values one at a time.
#
# A generator uses `yield` instead of `return`.
#
# yield:
# → Pauses the function.
# → Returns the current value.
# → Resumes from where it stopped when the
#   next value is requested.
#
# Generators are memory efficient because they
# don't store all values at once.
#
# return → Gives a value and ends the function.
# yield  → Gives a value and pauses the function.
#
# Useful for:
# - Large amounts of data
# - Large files
# - Data streams
# - Memory-efficient loops


# ============================================
# 1️⃣ COUNTING GENERATOR
# ============================================

def count_to(n):

    count = 1

    while count <= n:

        yield count       # Pause and return value

        count += 1        # Resume from here


number = int(input("Enter a number to count up to: "))


for n in count_to(number):
    print(n)


# Example:
#
# Input: 5
#
# Output:
# 1
# 2
# 3
# 4
# 5
#
#
# How it works:
#
# count_to(5)
#     ↓
# yield 1 → pause
#     ↓
# yield 2 → pause
#     ↓
# yield 3 → pause
#     ↓
# yield 4 → pause
#     ↓
# yield 5 → pause
#     ↓
# generator finishes


# ============================================
# 2️⃣ READING A FILE USING GENERATOR
# ============================================

def read_file(file_path):

    with open(file_path) as file:

        for line in file:
            yield line.strip()


file_path = "C:\\Users\\HP\\Desktop\\test.txt"


for line in read_file(file_path):
    print(line)


# ============================================
# 📌 WHY USE A GENERATOR FOR FILES?
# ============================================

# A normal approach might load the entire file
# into memory.
#
# A generator reads and provides ONE LINE AT A
# TIME.
#
# This is useful for very large files.
#
#
# File:
#
# line 1
# line 2
# line 3
# ...
# line 1000000
#
# Generator:
#
# line 1 → process
# line 2 → process
# line 3 → process
# ...
#
# It doesn't need to store all lines in memory.


# ============================================
# 📌 YIELD vs RETURN
# ============================================

# return:
#
# def test():
#     return 1
#
# → Returns a value and ends the function.
#
#
# yield:
#
# def test():
#     yield 1
#     yield 2
#
# → Produces values one at a time and pauses
#   between them.


# ============================================
# 📌 IMPORTANT
# ============================================

# Generator function
# → Function containing `yield`.
#
# yield
# → Produces a value and pauses execution.
#
# Generator
# → Remembers its state and continues from
#   where it stopped.
#
# Memory efficient
# → Values are generated only when needed.
#
#
# Remember:
#
# Generator → Uses yield
# yield     → Pause + return value
# return    → Return + stop function
#
# Generator = "Drip faucet 🚰"
# One value at a time.
# ============================================