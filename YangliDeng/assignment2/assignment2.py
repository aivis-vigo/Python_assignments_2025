import random
from library_utils import add_book, search_book, list_books

# List of book titles
books = ["Python 101", "Data Science", "Machine Learning"]

# Tuples (title, author, year)
book1 = ("Python 101", "John Smith", 2020)
book2 = ("Data Science", "Alice Brown", 2021)
book3 = ("Machine Learning", "David Lee", 2022)

# Set of genres
genres = {"Programming", "AI", "Math"}

# Dictionary (book_id : book_tuple)
library = {
    1: book1,
    2: book2
}

# Add a new book
add_book(library, 3, book3)

# List all books
print("All books in library:")
list_books(library)

# Search for a book
print("\nSearch result:")
result = search_book(library, "Python 101")
print(result)

# Suggest a random book
print("\nRandom book suggestion:")
random_book = random.choice(list(library.values()))
print(random_book)
