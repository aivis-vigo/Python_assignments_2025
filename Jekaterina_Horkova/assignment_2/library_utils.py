def add_book(library, book_id, book):
    if book_id in library:
        return False  
    library[book_id] = book
    return True


def search_book(library, title):
    for book_id, book in library.items():
        if book[0].lower() == title.lower():
            return book_id, book
    return None


def list_books(library):
    print("\n--- Library Books ---")
    for book_id, (title, author, year) in library.items():
        print(f"ID: {book_id} | Title: {title} | Author: {author} | Year: {year}")
    print("----------------------\n")
