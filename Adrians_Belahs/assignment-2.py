import library_utils

#Initial books
books = ["Python 101", "Data Science", "Machine Learning"]
book1 = [books[0],"John Smith",2020]
book2 = [books[1],"Alice Brown", 2021]
book3 = [books[2],"Oliver Theobald",2017]

#Store a set of unique genres of the library.
genres = {"Programming", "AI", "Math"}

library = {
    1:book1,
    2:book2,
    3:book3
}

#Preapre all parameters for function
book = ["Arch of Triumph","Erich Maria Remarque",1945]
last_key = next(reversed(library))  # get last id of dictionary
id = last_key + 1

print("Select action:\n[1:Print library]\n[2:Add book]\n[3:Search for book by title]"
      "\n[4:Suggest random book]\n[5:Exit]\n")
action = int(input("Action: ") or 5)
while(action!=0):
    if(action==1):
        library_utils.print_library(library)
    elif(action==2):
        title = str(input("Enter title: ") or "undefined")
        author = str(input("Enter author: ") or "undefined")
        year = int(input("Enter year: ") or 0)
        book = [title,author,year]
        dublicate = 0
        for id_, element in library.items():
            if element[0].lower() == title.lower():
                print("This book already exists in library!")
                dublicate = 1
        if dublicate == 0:
            library_utils.add_book(library, id, book)
            print("Book has been added to library!")
    elif(action==3):
        title = str(input("Enter title of book: "))
        library_utils.search_book(library, title)
    elif(action==4):
        library_utils.random_book(library)
    elif(action==5):
        print("Program terminated")
        break
    action = int(input("\nAction: "))