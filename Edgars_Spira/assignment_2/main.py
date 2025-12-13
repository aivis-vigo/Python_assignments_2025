import library_utils as lib

book1 = ("Python 101", "John Smith", 2021)
book2 = ("Math 101", "John Doe", 2022)
book3 = ("CS 101", "Joanna Smith", 2023)

# Test functions:

# Add a book
print("TEST ADD_BOOK FUNCTION")
lib.add_book(lib.library, 1, book1)
lib.add_book(lib.library, 2, book2)
lib.add_book(lib.library, 3, book3)

# Search:
print("TEST SEARCH_BOOK FUNCTION")
print(lib.search_book(lib.library, "Python 101"))
print(lib.search_book(lib.library, "Math 101"))

# List all books:
print("TEST LIST_BOOKS FUNCTION")
lib.list_books(lib.library)

lib.return_random_book(lib.books)