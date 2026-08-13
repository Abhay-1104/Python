# ============================================
# 📘 WRITING FILES IN PYTHON
# ============================================

# Python can write data to different file formats:
#
# 1. .txt  → Plain text
# 2. .json → Structured data
# 3. .csv  → Tabular data
#
# `with open()` is used to open a file safely.
#
# Common modes:
#
# "w" → Write mode
#       Creates a new file or OVERWRITES an existing file.
#
# "a" → Append mode
#       Adds data to the end of a file.
#
# "r" → Read mode
#       Reads data from a file.


# ============================================
# 1️⃣ WRITING .TXT FILE
# ============================================

txt_data = "I like pizza!"

file_path = "output.txt"

try:
    with open(file_path, "w") as file:
        file.write(txt_data)

    print(f".txt file '{file_path}' has been created successfully")

except FileExistsError:
    print("That file already exists")


# file.write()
# → Writes text into the file.
#
# `with open()` automatically closes the file
# after the block is finished.


# ============================================
# 2️⃣ WRITING .JSON FILE
# ============================================

import json

employee = {
    "name": "Spongebob",
    "age": 30,
    "job": "Cook"
}

file_path = "output.json"

try:
    with open(file_path, "w") as file:
        json.dump(employee, file, indent=4)

    print(f"JSON file '{file_path}' has been created successfully")

except FileExistsError:
    print("That file already exists!")


# json.dump()
# → Writes a Python object into a JSON file.
#
# indent=4
# → Makes the JSON file easier to read
#   by adding indentation.


# ============================================
# 3️⃣ WRITING .CSV FILE
# ============================================

import csv

employees = [
    ["Name", "Age", "Job"],
    ["Spongebob", 30, "Cook"],
    ["Patrick", 37, "Unemployed"],
    ["Sandy", 27, "Scientist"]
]

file_path = "output.csv"

try:
    with open(file_path, "w", newline="") as file:

        writer = csv.writer(file)

        for row in employees:
            writer.writerow(row)

    print(f"CSV file '{file_path}' was created")

except FileExistsError:
    print("That file already exists!")


# csv.writer()
# → Creates a CSV writer object.
#
# writer.writerow(row)
# → Writes one row into the CSV file.
#
# newline=""
# → Helps prevent unwanted blank lines,
#   especially on Windows.


# ============================================
# 📌 IMPORTANT
# ============================================

# TXT:
# file.write(data)
#
# JSON:
# json.dump(data, file, indent=4)
#
# CSV:
# writer = csv.writer(file)
# writer.writerow(row)
#
#
# `with open()`:
# → Opens the file.
# → Performs the required operation.
# → Automatically closes the file.
#
#
# Remember:
#
# .txt  → Simple text
# .json → Structured data
# .csv  → Rows and columns
#
# "w" → Write / overwrite
# "a" → Append
# "r" → Read
# ============================================