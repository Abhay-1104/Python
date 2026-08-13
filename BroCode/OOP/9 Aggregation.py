# ============================================
# 📘 AGGREGATION IN PYTHON
# ============================================

# Aggregation = A relationship where one object
# (the whole) contains references to one or more
# INDEPENDENT objects (the parts).
#
# The parts can exist independently of the whole.
#
# Example:
# Library → Whole
# Books   → Parts
#
# A Book can exist without a Library.


# ============================================
# 1️⃣ LIBRARY CLASS
# ============================================

class Library:

    def __init__(self, name):
        self.name = name
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def list_books(self):
        return [
            f"{book.title} by {book.author}"
            for book in self.books
        ]


# Library contains a list of Book objects.
#
# add_book()
# → Adds a Book object to the library.
#
# list_books()
# → Returns book titles and authors.


# ============================================
# 2️⃣ BOOK CLASS
# ============================================

class Book:

    def __init__(self, title, author):
        self.title = title
        self.author = author


# Book is an independent class.
# A Book does not need a Library to exist.


# ============================================
# 3️⃣ CREATING OBJECTS
# ============================================

library = Library("New York Public Library")

book1 = Book("Harry Potter...", "J.K. Rowling")
book2 = Book("The Hobbit", "J. R. R. Tolkein")
book3 = Book("The Colour of Magic", "Terry Pratchett")


# ============================================
# 4️⃣ ADDING BOOKS TO LIBRARY
# ============================================

library.add_book(book1)
library.add_book(book2)
library.add_book(book3)


# ============================================
# 5️⃣ DISPLAYING BOOKS
# ============================================

print(library.name)

for book in library.list_books():
    print(book)


# Output:
#
# New York Public Library
# Harry Potter... by J.K. Rowling
# The Hobbit by J. R. R. Tolkein
# The Colour of Magic by Terry Pratchett


# ============================================
# 📌 IMPORTANT
# ============================================

# Aggregation represents a "HAS-A" relationship.
#
# Library HAS-A Book.
#
# Library → Whole
# Book    → Part
#
# The Book objects are created separately:
#
# book1 = Book(...)
#
# Then they are added to the Library:
#
# library.add_book(book1)
#
# Therefore, books can exist independently
# of the library.
#
# Remember:
# Aggregation → HAS-A + independent objects
# ============================================