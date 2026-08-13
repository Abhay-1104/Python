# ============================================
# 📘 CLASS VARIABLES IN PYTHON
# ============================================

# Class variables are shared by ALL objects
# (instances) of a class.
#
# They are defined inside the class but OUTSIDE
# the __init__() constructor.
#
# Instance variable → belongs to one object
# Class variable    → shared by all objects


# ============================================
# 1️⃣ CREATING CLASS VARIABLES
# ============================================

class Student:

    # Class variables
    class_year = 2025
    num_students = 0

    def __init__(self, name, age):

        # Instance variables
        self.name = name
        self.age = age

        # Update shared class variable
        Student.num_students += 1


# ============================================
# 2️⃣ CREATING OBJECTS
# ============================================

student1 = Student("Spongebob", 30)
student2 = Student("Patrick", 35)
student3 = Student("Squidward", 55)
student4 = Student("Sandy", 27)


# Every time a Student object is created:
#
# Student.num_students += 1
#
# Therefore:
# student1 → 1
# student2 → 2
# student3 → 3
# student4 → 4


# ============================================
# 3️⃣ ACCESSING CLASS VARIABLES
# ============================================

print(
    f"My graduating class of {Student.class_year} "
    f"has {Student.num_students} students"
)

# Output:
# My graduating class of 2025 has 4 students


# Class variables can be accessed using:
#
# ClassName.variable
#
# Example:
# Student.class_year
# Student.num_students


# ============================================
# 4️⃣ INSTANCE VARIABLES
# ============================================

print(student1.name)
print(student2.name)
print(student3.name)
print(student4.name)

# Output:
# Spongebob
# Patrick
# Squidward
# Sandy


# ============================================
# 📌 CLASS vs INSTANCE VARIABLES
# ============================================

# Class Variable:
# → Shared by all objects.
# → Defined inside class, outside __init__().
#
# Example:
# class_year = 2025
#
#
# Instance Variable:
# → Unique to each object.
# → Defined using self inside __init__().
#
# Example:
# self.name = name
# self.age = age
#
#
# Remember:
#
# Student.class_year
# → Shared by all students
#
# student1.name
# → Belongs only to student1
# ============================================