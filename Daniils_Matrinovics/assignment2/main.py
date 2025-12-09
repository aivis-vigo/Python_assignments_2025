import library_utils as lu
import random

print("Original library:")
lu.list_books(lu.library)

lu.add_book(lu.library, 4, ("Dinosaur book","Dinosaur Michael",1000))

print("Modified library:")
lu.list_books(lu.library)

suggestion = lu.search_book(lu.library, random.choice(lu.books))

print("Random book suggestion:")
print(suggestion)
