# ============================================
# 📘 STATIC METHODS IN PYTHON
# ============================================

# Static method = A method that belongs to the
# class rather than a specific object.
#
# Usually used for general utility functions.
#
# Instance Method:
# → Works with object/instance data.
#
# Static Method:
# → Does not need object or class data.


# ============================================
# 1️⃣ EMPLOYEE CLASS
# ============================================

class Employee:

    def __init__(self, name, position):
        self.name = name
        self.position = position


    # INSTANCE METHOD
    def get_info(self):
        return f"{self.name} = {self.position}"


    # STATIC METHOD
    @staticmethod
    def is_valid_position(position):

        valid_positions = [
            "Manager",
            "Cashier",
            "Cook",
            "Janitor"
        ]

        return position in valid_positions


# ============================================
# 2️⃣ USING STATIC METHOD
# ============================================

print(Employee.is_valid_position("Rocket Scientist"))

# Output:
# False


print(Employee.is_valid_position("Manager"))

# Output:
# True


# ============================================
# 📌 IMPORTANT
# ============================================

# @staticmethod
# → Used to create a static method.
#
# Static method does NOT need:
# - self
# - object data
# - class data
#
# It can be called directly using:
#
# Employee.is_valid_position("Manager")
#
#
# Instance method:
#
# employee = Employee("Abhay", "Cook")
# employee.get_info()
#
# It uses `self` to access:
# self.name
# self.position
#
#
# Remember:
#
# Instance method → works with object data
#
# Static method → utility function, no object data
# ============================================