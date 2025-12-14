# main.py
from library_utils import add_book, search_book, list_books, suggest_random_book

# List of book titles
books = ["Python 101", "Data Science", "Machine Learning"]

# Tuples for each book
book1 = ("Python 101", "John Smith", 2020)
book2 = ("Data Science", "Alice Brown", 2021)
book3 = ("Machine Learning", "Bob Johnson", 2022)

# Set of unique genres
genres = {"Programming", "AI", "Math"}

# Dictionary of books with ID as key
library = {
    1: book1,
    2: book2,
    3: book3
}

# Demonstrate functions
print("--- List all books ---")
list_books(library)

print("\n--- Search for a book ---")
search_book(library, "Data Science")

print("\n--- Add a new book ---")
new_book = ("Deep Learning", "Carol White", 2023)
add_book(library, 4, new_book)

print("\n--- List books after adding new book ---")
list_books(library)

print("\n--- Suggest a random book ---")
suggest_random_book(library)
