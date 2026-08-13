# ============================================
# 📘 FILE DETECTION IN PYTHON
# ============================================

# Python's `os` module provides functions to
# check whether a file or directory exists.
#
# Common functions:
# os.path.exists() → Checks if path exists
# os.path.isfile() → Checks if path is a file
# os.path.isdir()  → Checks if path is a directory


# ============================================
# 1️⃣ IMPORT OS
# ============================================

import os


# ============================================
# 2️⃣ FILE PATH
# ============================================

file_path = "test.txt"


# ============================================
# 3️⃣ CHECK IF PATH EXISTS
# ============================================

if os.path.exists(file_path):

    print(f"The location '{file_path}' exists")


    # Check if it is a file
    if os.path.isfile(file_path):
        print("That is a file")


    # Check if it is a directory
    elif os.path.isdir(file_path):
        print("That is a directory")


# If path does not exist
else:
    print("That location doesn't exist")


# ============================================
# 📌 IMPORTANT
# ============================================

# os.path.exists(path)
# → True if the file/directory exists.
#
# os.path.isfile(path)
# → True if the path is a file.
#
# os.path.isdir(path)
# → True if the path is a directory.
#
#
# Example:
#
# file_path = "test.txt"
#
# If test.txt exists:
#
# The location 'test.txt' exists
# That is a file
#
#
# If test.txt does not exist:
#
# That location doesn't exist
#
#
# Remember:
#
# exists() → Does it exist?
# isfile() → Is it a file?
# isdir()  → Is it a directory?
# ============================================