'''
I did not understand should there be a user input or not, so decided to make a code with user input 
because it will be more logically correct.
List of books will be shown above the menu.
'''

from library_utils import add_book, search_book, list_books
import random

library = {
    1: ("Python 101", "John Smith", 2020),
    2: ("Data Science", "Alice Brown", 2021),
    3: ("Machine Learning", "David Clark", 2022)
}

result_message = ""   


def suggest_random_book(library):
    book_id = random.choice(list(library.keys()))
    title, author, year = library[book_id]
    return f"Suggested: {title} by {author} ({year})"


while True:
    print("====== Library Menu ======")
    print("1. List all books")
    print("2. Add book")
    print("3. Search for a book")
    print("4. Suggest random book")
    print("5. Exit")
    print("==========================")

    if result_message:
        print("\n--- RESULT ---")
        print(result_message)
        print("--------------\n")

    choice = input("Choose an option (1–5): ")

    if choice == "1":
        list_books(library)
        result_message = "Displayed book list. Output is the menu."

    elif choice == "2":
        book_id = int(input("Enter new book ID: "))
        title = input("Enter title: ")
        author = input("Enter author: ")
        year = int(input("Enter year: "))

        new_book = (title, author, year)
        success = add_book(library, book_id, new_book)

        if success:
            result_message = "Book added!"
        else:
            result_message = "Book ID already exists!"

    elif choice == "3":
        title = input("Enter title to search: ")
        result = search_book(library, title)

        if result:
            book_id, book = result
            result_message = f"Found → ID {book_id}: {book}"
        else:
            result_message = "Book not found."

    elif choice == "4":
        result_message = suggest_random_book(library)

    elif choice == "5":
        print("Goodbye!")
        break

    else:
        result_message = "Invalid choice!"
