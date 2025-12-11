
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

consonant_count = Fname - Vowels(FirstName)
print("Consonants in first name:", consonant_count)

print("Furst name (upper): ", FirstName.upper())
print("First name (lower): ", FirstName.lower())
print("Last name (reversed): ", LastName[::-1])

print("Characters in first name (for loop):")
for F in FirstName:
    print(F)
print("Characters in first name (while loop):")
i = 0
while i < Fname:
    print(FirstName[i])
    i += 1

if Fname > Lname:
    print("First name is longer than last name.")
elif Fname < Lname:
    print("Last name is longer than first name.")
else:
    print("First name and last name are of equal length.")

total_length = Fname + Lname


print("Generated password: ",FirstName[0],LastName[-1],total_length)