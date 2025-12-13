
FirstName = str(input("Please enter your first name: "))
LastName = str(input("Please enter your last name: "))

Fname = len(FirstName.replace(" ", ""))
Lname = len(LastName.replace(" ", ""))

print("Your first name has", Fname, 
      "characters and your last name has", 
      Lname, "characters.")

def Vowels (FirstName):
    vowels = "aeiou"
    count = 0
    for char in FirstName.lower():
        if char in vowels:
            count += 1
    return count

print("Your first name has", Vowels(FirstName), "vowels.")