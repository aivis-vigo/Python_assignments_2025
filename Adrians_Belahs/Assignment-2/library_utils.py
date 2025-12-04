import random

#Print all library
def print_library(library):
    print("Library:")
    for id_, element in library.items():
        print(id_, element)
    return

#Function that adds book
def add_book(library, id, book):
    library[id] = book
    return

#Function that searches for book by title
def search_book(library,title):
    for id_, element in library.items():
        if element[0].lower() == title.lower():
            print("Book",element,"found with ID:", id_)
            return
    print("Book not found")

#Suggest random book
def random_book(library):
    last_key = next(reversed(library)) #Get last key of library
    ans = random.randint(1,last_key)
    print("Random book for reading: ",library[ans])
    return
