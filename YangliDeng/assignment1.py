
FirstName = str(input("Enter your first name: "))
LastName = str(input("Enter your last name: "))

Fname = len(FirstName.replace(" ", ""))
Lname = len(LastName.replace(" ", ""))

print("Your first name has", Fname, 
      "characters and your last name has", 
      Lname, "characters.")

def Vowels (FirstName):
    vowels = "aeiou"
    count = 0
    for name in FirstName.lower():
        if name in vowels:
            count += 1
    return count

print("Vowels in first name:", Vowels(FirstName))