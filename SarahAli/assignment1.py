# Ask for first and last name
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")

# String Analysis
print("Length of first name:", len(first_name))
print("Length of last name:", len(last_name))

# Count vowels and consonants in first name
vowels = "aeiouAEIOU"
vowel_count = 0
consonant_count = 0
for c in first_name:
    if c in vowels:
        vowel_count += 1
    else:
        consonant_count += 1
print("Vowels in first name:", vowel_count)
print("Consonants in first name:", consonant_count)

# Uppercase and lowercase
print("First name (upper):", first_name.upper())
print("First name (lower):", first_name.lower())

# Reverse last name
print("Last name (reversed):", last_name[::-1])

# For loop to print each character
print("\nCharacters in first name (for loop):")
for c in first_name:
    print(c)

# While loop to print characters
print("\nCharacters in first name (while loop):")
i = 0
while i < len(first_name):
    print(first_name[i])
    i += 1

# Compare lengths
if len(first_name) > len(last_name):
    print("\nComparison result: First name is longer than last name.")
elif len(first_name) < len(last_name):
    print("\nComparison result: Last name is longer than first name.")
else:
    print("\nComparison result: First name and last name are equal in length.")

# Simple password
password = first_name[0] + last_name[-1] + str(len(first_name) + len(last_name))
print("Generated password:", password)

# List methods practice
last_list = []
for c in last_name:
    last_list.append(c)
last_list.append("*")
last_list.insert(0, "@")
if len(last_list) > 1:
    last_list.pop(1)
last_list.reverse()
print("List methods example on last name:")
print(last_list)
