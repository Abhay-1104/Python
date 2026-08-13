# ============================================
# 📘 MEMBERSHIP OPERATORS IN PYTHON
# ============================================

# Membership operators are used to check whether
# a value exists in a sequence/collection.
#
# Operators:
# 1. in      → True if value is found
# 2. not in  → True if value is NOT found
#
# Can be used with:
# - String
# - List
# - Tuple
# - Set
# - Dictionary


# ============================================
# 1️⃣ MEMBERSHIP IN A STRING
# ============================================

word = "APPLE"

letter = input("Guess a letter in the secret word: ")

if letter in word:
    print(f"There is a {letter}")
else:
    print(f"{letter} was not found")


# Example:
# word = "APPLE"
# letter = "P"
#
# "P" in "APPLE" → True


# ============================================
# 2️⃣ MEMBERSHIP IN A SET
# ============================================

students = {"Spongebob", "Patrick", "Sandy"}

student = input("Enter the name of a student: ")

if student in students:
    print(f"{student} is in this class")
else:
    print(f"{student} is NOT in this class")


# `in` checks whether the student exists in the set.


# ============================================
# 3️⃣ MEMBERSHIP IN A DICTIONARY
# ============================================

grades = {
    "Sandy": "A",
    "Squidward": "B",
    "Spongebob": "C",
    "Patrick": "D"
}

student = input("Enter the name of a student: ")

if student in grades:
    print(f"{student}'s grade is {grades[student]}.")
else:
    print(f"{student} is not in the dictionary")


# ⚠️ Important:
# `in` checks KEYS in a dictionary by default.
#
# "Sandy" in grades → True
#
# To check values:
#
# "A" in grades.values() → True


# ============================================
# 4️⃣ USING `in` WITH AND
# ============================================

email = "BroCode@gmail.com"

if "@" in email and "." in email:
    print("Valid email")
else:
    print("Invalid email")


# Both conditions must be True:
#
# "@" in email → True
# "." in email → True
#
# Therefore:
# Valid email


# ============================================
# 📌 IMPORTANT
# ============================================

# `in`
# → Checks if a value EXISTS.
#
# `not in`
# → Checks if a value DOES NOT EXIST.
#
# Examples:
#
# "A" in "APPLE"       → True
# "X" in "APPLE"       → False
# "X" not in "APPLE"   → True
#
# For dictionaries:
#
# key in dictionary
# key in dictionary.keys()
# value in dictionary.values()
#
# Membership operators return:
# True or False
# ============================================