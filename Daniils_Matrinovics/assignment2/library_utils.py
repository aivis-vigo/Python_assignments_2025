#List: Create a list of book titles.

books = ["Python 101", "Data Science", "Machine Learning"]

#Tuple: Each book should be stored as a tuple (title, author, year).

book1 = ("Python 101", "John Smith", 2020)
book2 = ("Data Science", "Jane Doe", 2022)
book3 = ("Machine Learning", "Donald Trump", 2025)

#Set: Store a set of unique genres of the library.

genres = {"Programming", "AI", "Math"}

#Dictionary: Store books in a dictionary where the key is the book ID and the value is the book tuple.

library = {
    1: book1,
    2: book2,
    3: book3
}

#Functions:
# Add a new book
def add_book(library, id, book):
    if book not in books:
        books.append(book[0])
        library[id] = book
    else:
        print("The book already exists!")

# Search for a book by title
def search_book(library, title):
    result = [b for b in library.values() if b[0]==title]
    return result[0] if result else "Book not found!" 

# Print all books
def list_books(library):
    print(library)