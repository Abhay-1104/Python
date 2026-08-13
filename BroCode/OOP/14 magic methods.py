# ============================================
# 📘 MAGIC METHODS / DUNDER METHODS
# ============================================

# Magic methods are also called DUNDER methods.
# Dunder = Double UNDERscore
#
# They start and end with double underscores:
# __init__
# __str__
# __eq__
#
# Python automatically calls these methods when
# certain built-in operations are used.
#
# They allow us to customize how objects behave.


# ============================================
# 1️⃣ BOOK CLASS
# ============================================

class Book:

    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages


    # Called when print(object) is used
    def __str__(self):
        return f"'{self.title}' by {self.author}"


    # Called when == is used
    def __eq__(self, other):
        return (
            self.title == other.title
            and self.author == other.author
        )


    # Called when < is used
    def __lt__(self, other):
        return self.pages < other.pages


    # Called when > is used
    def __gt__(self, other):
        return self.pages > other.pages


    # Called when + is used
    def __add__(self, other):
        return f"{self.pages + other.pages} pages"


    # Called when `in` is used
    def __contains__(self, keyword):
        return (
            keyword in self.title
            or keyword in self.author
        )


    # Called when object[key] is used
    def __getitem__(self, key):

        if key == "title":
            return self.title

        elif key == "author":
            return self.author

        elif key == "pages":
            return self.pages

        else:
            return f"Key '{key}' was not found"


# ============================================
# 2️⃣ CREATING OBJECTS
# ============================================

book1 = Book("The Hobbit", "J.R.R. Tolkien", 310)

book2 = Book(
    "Harry Potter and The Philosopher's Stone",
    "J.K. Rowling",
    223
)

book3 = Book(
    "The Lion, the Witch and the Wardrobe",
    "C.S. Lewis",
    172
)


# ============================================
# 3️⃣ USING MAGIC METHODS
# ============================================

print(book1)
# Calls __str__()


print(book1 == book3)
# Calls __eq__()


print(book1 < book2)
# Calls __lt__()


print(book2 > book3)
# Calls __gt__()


print(book1 + book2)
# Calls __add__()


print("Lion" in book3)
# Calls __contains__()


print(book3["title"])
# Calls __getitem__()


# ============================================
# 📌 IMPORTANT
# ============================================

# Operation          Magic Method
# --------------------------------
# print(obj)          __str__()
# obj1 == obj2        __eq__()
# obj1 < obj2         __lt__()
# obj1 > obj2         __gt__()
# obj1 + obj2         __add__()
# x in obj            __contains__()
# obj[key]            __getitem__()
#
#
# `__init__`
# → Automatically called when an object
#   is created.
#
# Magic methods allow us to define how our
# custom objects behave with Python operators
# and built-in functions.
#
# Remember:
# Magic methods = Dunder methods = __method__
# ============================================