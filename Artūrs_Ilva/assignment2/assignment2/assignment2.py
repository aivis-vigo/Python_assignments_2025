from library_utils import (
    add_book,
    search_book,
    list_books,
    suggest_random_book,
    books,
    genres,
    library,
)


def print_book(book_id, book):
    title, author, year, genre = book
    print(f"[{book_id}] {title} - {author} ({year}), genre: {genre}")


def main():
    while True:
        print("Library Management System")
        print("1. List all books")
        print("2. Add a new book")
        print("3. Search for a book by title")
        print("4. Suggest a random book")
        print("5. Show all titles (list)")
        print("6. Show all genres (set)")
        print("0. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            print("\nAll books in the library:")
            for book_id, book in list_books():
                print_book(book_id, book)

        elif choice == "2":
            try:
                book_id = int(input("Enter new book ID (number): "))
            except ValueError:
                print("ID must be a number.")
                continue

            if book_id in library:
                print("This ID already exists.")
                continue

            title = input("Title: ")
            author = input("Author: ")
            try:
                year = int(input("Year: "))
            except ValueError:
                print("Year must be a number.")
                continue
            genre = input("Genre: ")

            add_book(book_id, title, author, year, genre)
            print("Book added successfully.")

        elif choice == "3":
            title = input("Enter title to search: ")
            result = search_book(title)
            if result is None:
                print("Book not found.")
            else:
                book_id, book = result
                print("Book found:")
                print_book(book_id, book)

        elif choice == "4":
            suggestion = suggest_random_book()
            if suggestion is None:
                print("Library is empty.")
            else:
                book_id, book = suggestion
                print("You should read:")
                print_book(book_id, book)

        elif choice == "5":
            print("\nAll titles (list):")
            for title in books:
                print("-", title)

        elif choice == "6":
            print("\nAll genres (set):")
            for g in genres:
                print("-", g)

        elif choice == "0":
            print("Goodbye.")
            break

        else:
            print("Invalid option. Try again.")


if __name__ == "__main__":
    main()