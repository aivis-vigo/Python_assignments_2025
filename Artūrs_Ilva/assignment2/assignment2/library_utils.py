import random  # standard library

# List – book titles
books = ["Python 101", "Data Science", "Machine Learning"]

# Set – unique genres
genres = {"Programming", "AI", "Math"}

# Dictionary – key = book ID, value = (title, author, year, genre)
library = {
    1: ("Python 101", "John Smith", 2020, "Programming"),
    2: ("Data Science", "Alice Brown", 2021, "AI"),
    3: ("Machine Learning", "Bob Green", 2019, "AI"),
}


def add_book(book_id: int, title: str, author: str, year: int, genre: str) -> None:
    book = (title, author, year, genre)
    library[book_id] = book
    books.append(title)
    genres.add(genre)


def search_book(title: str):
    title_lower = title.lower()
    for book_id, book in library.items():
        if book[0].lower() == title_lower:
            return book_id, book
    return None


def list_books():
    return list(library.items())


def suggest_random_book():
    if not library:
        return None
    book_id = random.choice(list(library.keys()))
    return book_id, library[book_id]