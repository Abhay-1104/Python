# ============================================
# 📘 if __name__ == "__main__"
# ============================================

# This file can be run directly or imported.
#
# The main block runs only when this file
# is executed directly.


# ============================================
# 1️⃣ FUNCTION
# ============================================

def favorite_food(food):
    print(f"Your favorite food is {food}")


def main():
    print("This is 21_1")
    favorite_food("pizza")
    print("Goodbye!")


# ============================================
# 2️⃣ MAIN BLOCK
# ============================================

if __name__ == "__main__":
    main()


# If 21_1.py is run directly:
# → main() executes.
#
# If 21_1.py is imported:
# → main() does not execute.
#
# But favorite_food() can still be used
# by another file.