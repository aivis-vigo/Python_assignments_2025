"""
This homework is created by:
Jekaterina Horkova
Student ID: jh23009
"""
#Ask for input
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")


#Print the length of the first name and last name.
print("Length of first name:", len(first_name))
print("Length of last name:", len(last_name))


#Count vowels (a, e, i, o, u) in the first name.
vowels = "AEIOUaeiou"

vowel_count = 0
for ch in first_name:
    if ch in vowels:
        vowel_count += 1
        
print("Number of vowels in first name:", vowel_count)


#Count consonants in the first name.
consonant_count = 0
for ch in first_name:
    if ch.isalpha and ch not in vowels:
        consonant_count += 1
        
print("Number of consonants in first name:", consonant_count)


#Print the first name in uppercase and lowercase.
uppercase = first_name.upper()
lowercase = first_name.lower()

print("First name (upper):", uppercase)
print("First name (lower):", lowercase)

#Print the last name reversed
reverse = last_name[::-1]
print("Last name (reversed): "+ reverse)


#Use a for loop to print each character of the first name.
print("Characters in first name (for loop):")
for ch in first_name:
    print(ch)


#Use a while loop to repeatedly print and remove characters from the first name until nothing is left.
print("Characters in first name (while loop):")
name = first_name   

while name:   
    print(name[0])  
    name = name[1:]


"""
Conditions (if/elif/else):
Compare the lengths of the first and last name.
Print a different message depending on whether the first name is longer, shorter, or equal.
"""
if len(first_name) == len(last_name):
    print("Comparison result: Length of first name and last name are equal")
elif len(first_name) > len(last_name):
    print("Comparison result: First name is longer than last name")
else:
    print("Comparison result: Last name is longer than first name")


"""
Generate a personal password:
Combine:
The first letter of the first name
The last letter of the last name
The total number of characters (first name + last name)
"""
first_letter = first_name[0]
last_letter = last_name[-1]
total_length = len(first_name) + len(last_name)

password = first_letter + last_letter + str(total_length)

print("Generated password:", password)


"""
List methods practice
Create a list that contains each character of your last name.
Use .append() to add a "*" character to the end of the list.
Use .insert() to add "@" at the beginning.
Use .remove() (or .pop()) to delete one character.
Use .reverse() to reverse the list.
"""
my_list = list(last_name)
my_list.append("*")
my_list.insert(0,"@")
my_list.pop(2)
my_list.reverse()
print(my_list)






































