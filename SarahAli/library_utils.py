# library_utils.py
import random  # standard library

# Function to add a new book
def add_book(library, book_id, book):
    if book_id in library:
        print(f"Book ID {book_id} already exists!")
    else:
        library[book_id] = book
        print(f"Book '{book[0]}' added successfully!")

# Function to search a book by title
def search_book(library, title):
    found = False
    for book_id, book in library.items():
        if book[0].lower() == title.lower():
            print(f"Found: ID={book_id}, Title={book[0]}, Author={book[1]}, Year={book[2]}")
            found = True
    if not found:
        print(f"No book found with title '{title}'")

# Function to list all books
def list_books(library):
    if not library:
        print("Library is empty.")
    else:
        print("Library Books:")
        for book_id, book in library.items():
            print(f"ID={book_id}, Title={book[0]}, Author={book[1]}, Year={book[2]}")

# Function to suggest a random book
def suggest_random_book(library):
    if not library:
        print("Library is empty.")
    else:
        book = random.choice(list(library.values()))
        print(f"Suggested Book: {book[0]} by {book[1]} ({book[2]})")
