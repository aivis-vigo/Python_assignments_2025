# library_utils.py

def add_book(library, book_id, book):
    library[book_id] = book


def search_book(library, title):
    for book_id in library:
        book = library[book_id]
        if book[0] == title:
            return book
    return None


def list_books(library):
    for book_id in library:
        book = library[book_id]
        print(book_id, ":", book)
