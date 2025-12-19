# ## Input
# 0. Ask the user for their first name and last name.
print("Enter your first and last names:")
full_name = input().split(' ')

first_name = full_name[0]
last_name = full_name[1]

print(f"Your full name is:  {first_name} {last_name}")


# **String Analysis**
# 1. Print the length of the first name and last name.
print(f"Length of first name: {len(first_name)}" )
print(f"Length of last name: {len(last_name)}")


# 2. Count vowels (a, e, i, o, u, y) in the first name.
# 3. Count consonants in the first name.
all_vowels = ['a', 'e', 'i', 'o', 'u', 'y']
all_upper_vowels = [x.upper() for x in all_vowels]
vowels = 0
consonants = 0

for char in first_name:
    if char in all_vowels or char in all_upper_vowels:
        vowels += 1
    else:
        consonants += 1

print(f"Count of vowels in the first name is {vowels} and consonants is {consonants}")

# 4. Print the first name in uppercase and lowercase.
print(f"First name in uppercase: {first_name.upper()}")
print(f"First name in lowercase: {first_name.lower()}")

# 5. Print the last name reversed.
print(f"Reversed last name: {last_name[::-1]}")



# **Loop Practice**
# 1. Use a for loop to print each character of the first name.
print("For loop practice:")
for char in first_name:
    print(char)

# 2. Use a while loop to print and remove characters from the first name until it is empty.
first_name_copy = first_name
print("While loop with removal:")
while len(first_name_copy) > 0:
    print(first_name_copy[0])
    first_name_copy = first_name_copy[1:]


# **Conditional Statements**
# 1. Compare the lengths of the first and last name.
# 2. Print a message:
# If first name > last name → "First name is longer than last name."
# If first name < last name → "Last name is longer than first name."
# If equal → "First name and last name are equal in length."

print("Length of first / last names comparison:")
if len(first_name) > len(last_name): print("First name is longer than last name.")
elif len(first_name) < len(last_name): print("Last name is longer than first name.")
elif len(first_name) == len(last_name): print("First name and last name are equal in length.")


# **Personal Password Generator**
# 1. Create personal password by Combining:
# First letter of first name
# Last letter of last name
# Total number of letters (first + last name)
password = first_name[0] + last_name[0] + str((len(first_name) + len(last_name)))
print(f"Generated password: {password}")

# **List Methods Practice**
# 1. Create a list of characters from your last name.
last_name_list = [x for x in last_name]

# 2. Use .append() to add "*" at the end.
last_name_list.append("*")

# 3. Use .insert() to add "@" at the beginning.
last_name_list.insert(0, "@")

# 4. Use .remove() (or .pop()) to remove a character.
last_name_list.pop(2)

# 5. Use .reverse() to reverse the list.
last_name_list.reverse()

# 6. Print the final list.
print(last_name_list)