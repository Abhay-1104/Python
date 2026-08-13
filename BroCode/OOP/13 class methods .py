# ============================================
# 📘 CLASS METHODS IN PYTHON
# ============================================

# Class method = A method that works with the
# class itself rather than a specific object.
#
# It takes `cls` as the first parameter.
#
# `cls` → refers to the class itself.
#
# Types of methods:
#
# Instance method → works with object data
# Static method   → utility function
# Class method    → works with class-level data


# ============================================
# 1️⃣ STUDENT CLASS
# ============================================

class Student:

    # Class variables
    count = 0
    total_gpa = 0

    def __init__(self, name, gpa):
        self.name = name
        self.gpa = gpa

        Student.count += 1
        Student.total_gpa += gpa


    # INSTANCE METHOD
    def get_info(self):
        return f"{self.name} {self.gpa}"


    # CLASS METHOD
    @classmethod
    def get_count(cls):
        return f"Total # of students: {cls.count}"


    # CLASS METHOD
    @classmethod
    def get_average_gpa(cls):

        if cls.count == 0:
            return 0

        return f"Average GPA: {cls.total_gpa / cls.count:.2f}"


# ============================================
# 2️⃣ CREATING OBJECTS
# ============================================

student1 = Student("Spongebob", 3.2)
student2 = Student("Patrick", 2.0)
student3 = Student("Sandy", 4.0)


# count = 3
# total_gpa = 3.2 + 2.0 + 4.0 = 9.2


# ============================================
# 3️⃣ CALLING CLASS METHODS
# ============================================

print(Student.get_count())
print(Student.get_average_gpa())


# Output:
#
# Total # of students: 3
# Average GPA: 3.07


# ============================================
# 📌 IMPORTANT
# ============================================

# @classmethod
# → Creates a class method.
#
# cls
# → Refers to the class itself.
#
# Class methods can access class variables:
#
# cls.count
# cls.total_gpa
#
# They can be called using:
#
# Student.get_count()
#
#
# ============================================
# 🔹 TYPES OF METHODS
# ============================================

# Instance Method:
# → Uses `self`
# → Works with object/instance data
#
# def get_info(self):
#     ...
#
#
# Static Method:
# → Uses `@staticmethod`
# → Does not need self or cls
# → Used for utility functions
#
#
# Class Method:
# → Uses `@classmethod`
# → Uses `cls`
# → Works with class-level data
#
#
# Remember:
#
# self → object
# cls  → class
# ============================================