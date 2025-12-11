
FirstName = str(input("Enter your first name: "))
LastName = str(input("Enter your last name: "))
# Calculate lengths excluding spaces
Fname = len(FirstName.replace(" ", ""))
Lname = len(LastName.replace(" ", ""))

print("Your first name has", Fname, 
      "characters and your last name has", 
      Lname, "characters.")
# Function to count vowels in the first name
def Vowels (FirstName):
    vowels = "aeiou"
    count = 0
    for name in FirstName.lower():
        if name in vowels:
            count += 1
    return count

print("Vowels in first name:", Vowels(FirstName))
# Calculate consonants in the first name, Just subtracting vowels from total length
consonant_count = Fname - Vowels(FirstName)
print("Consonants in first name:", consonant_count)
# String manipulations
print("Furst name (upper): ", FirstName.upper())
print("First name (lower): ", FirstName.lower())
print("Last name (reversed): ", LastName[::-1])
# For loop and while loop to print each character in the first name
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
# Password generation
total_length = Fname + Lname

password = FirstName[0] + LastName[-1] + str(total_length)
password = password.replace(" ", "")

print("Generated password: ", password)
# List methods example, just use different methods on last name
LastName_List = list(LastName)
LastName_List.append("*")
LastName_List.insert(0,"@")
LastName_List.remove(LastName_List[1])
LastName_List.reverse()
print("List methods example on last name:")
print(LastName_List)