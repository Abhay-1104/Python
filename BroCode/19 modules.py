# ============================================
# 📘 MODULES IN PYTHON
# ============================================

# A module is a Python file (.py) containing
# variables, functions, or classes that can be
# reused in another Python file.
#
# `import` is used to use a module.

# ============================================
# 📄 main.py
# ============================================

import example

# Access variables/functions using:
# module_name.variable
# module_name.function()


result = example.pi

result = example.square(3)
result = example.cube(3)
result = example.circumference(3)
result = example.area(3)

print(result)


# Output:
# 28.27431


# ============================================
# 📌 IMPORTANT
# ============================================

# `import example`
# → Imports example.py as a module.
#
# `example.pi`
# → Accesses the variable `pi`.
#
# `example.square(3)`
# → Calls the square() function from example.py.
#
# A module helps us:
# - Reuse code
# - Organize large programs
# - Keep related functions together
#
# Remember:
# module = Python file (.py)
# import  = bring module into another file
# ============================================