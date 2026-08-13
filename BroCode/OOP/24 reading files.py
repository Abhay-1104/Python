# ============================================
# 📘 READING FILES IN PYTHON
# ============================================

# Python can read different types of files:
#
# 1. .txt  → Plain text
# 2. .json → Structured data
# 3. .csv  → Tabular data
#
# Common file mode:
#
# "r" → Read mode
#
# `with open()` automatically closes the file
# after reading.


# ============================================
# 1️⃣ READING .TXT FILE
# ============================================

file_path = "C:/Users/HP/Desktop/input.txt"

try:
    with open(file_path, "r") as file:
        content = file.read()
        print(content)

except FileNotFoundError:
    print("That file was not found")

except PermissionError:
    print("You do not have permission to read that file")


# file.read()
# → Reads the entire contents of the file.


# ============================================
# 2️⃣ READING .JSON FILE
# ============================================

import json

file_path = "C:/Users/HP/Desktop/input.json"

try:
    with open(file_path, "r") as file:
        content = json.load(file)
        print(content)

except FileNotFoundError:
    print("That file was not found")

except PermissionError:
    print("You do not have permission to read that file")


# json.load()
# → Reads JSON data from a file.
#
# The JSON data is converted into a Python
# object such as:
# - Dictionary
# - List
# - String
# - Number


# ============================================
# 3️⃣ READING .CSV FILE
# ============================================

import csv

file_path = "C:/Users/HP/Desktop/input.csv"

try:
    with open(file_path, "r") as file:

        content = csv.reader(file)

        for line in content:
            print(line)

except FileNotFoundError:
    print("That file was not found")

except PermissionError:
    print("You do not have permission to read that file")


# csv.reader()
# → Reads rows from a CSV file.
#
# Each row is returned as a list.
#
# Example CSV:
#
# Name,Age,Job
# Spongebob,30,Cook
#
# Output:
#
# ['Name', 'Age', 'Job']
# ['Spongebob', '30', 'Cook']


# ============================================
# 📌 IMPORTANT
# ============================================

# TXT:
# file.read()
#
# JSON:
# json.load(file)
#
# CSV:
# csv.reader(file)
#
#
# Common exceptions:
#
# FileNotFoundError
# → File/path does not exist.
#
# PermissionError
# → Program does not have permission
#   to access the file.
#
#
# Remember:
#
# "r" → Read
# "w" → Write
# "a" → Append
#
# with open() → Automatically closes the file.
# ============================================