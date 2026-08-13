# ============================================
# 📘 Dictionaries in Python
# ============================================
# A dictionary is a collection of key-value pairs.
# - Syntax: { key: value, key: value }
# - Keys must be unique & immutable
# - Values can be any data type
# - Ordered & changeable

# ============================================
# 1️⃣ Creating a Dictionary
# ============================================

student = {
    "name": "Abhay",
    "age": 19,
    "branch": "IoT",
    "skills": ["Python", "C", "Web Dev"]
}

print(" Full dictionary:", student)       # prints entire dictionary
print(" Access by key:", student["name"]) # access value using key
print(" Safe access using get():", student.get("age")) # safe access (no error if key missing)

# ============================================
# 2️⃣ Another Dictionary Example
# ============================================

capitals = {
    "USA": "Washington D.C",
    "India": "New Delhi",
    "Russia": "Moscow",
    "China": "Beijing"
}

print(capitals)                # print dictionary
print(capitals.get("India"))   # get value of India → New Delhi
print(capitals.get("Japan"))   # returns None if key not present

# check if key exists
if capitals.get("Japan"):
    print("that capital is in dictionary")
else:
    print("that capital not in dictionary")

# ============================================
# 3️⃣ Update, Add, Remove
# ============================================

capitals.update({"Germany": "Berlin"})   # add new key-value pair
capitals.update({"USA": "Detroit"})      # update value of existing key
print(capitals)

capitals.pop("China")   # remove specific key
print(capitals)

capitals.popitem()      # remove last inserted key-value pair
capitals.clear()        # remove everything (dictionary becomes empty)

# ============================================
# 4️⃣ Dictionary Views
# ============================================

keys = capitals.keys()     # returns all keys
print(keys)

for i in capitals.keys():  # loop through keys
    print(i)

values = capitals.values() # returns all values
print(values)

for i in capitals.values(): # loop through values
    print(i)

items = capitals.items()   # returns (key, value) pairs
print(items)

for k, v in capitals.items():   # loop through key-value pairs
    print(f"{k}:{v}")
