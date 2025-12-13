import random
# Library Management System

# A list of book titles.
books = []

# Each book should be stored as a tuple (title, author, year).
book1 = ("Python 101", "John Smith", 2020)

# Store a set of unique genres of the library.
genres = {"Programming", "AI", "Math"}

# Store books in a dictionary where the key is the book ID and the value is the book tuple.
library = {}

def add_book(library, id, book): # → Add a new book
    library[id] = book
    print(f"Book added: {library[id]}")

    books.append(book[0]) # Add a new title to the books titles list

def search_book(library, title): # → Search for a book by title
    for book in library:
        if library[book][0] == title:
            return library[book]

def list_books(library): #→ Print all books
    print("List of all books:")
    for book in library:
        print(library[book])

def return_random_book(books): # Return a random book from the list of titles
    random_book_id = random.choice(list(library.keys()))
    print(f"Random book to read: {library[random_book_id]}")
