
name = input("Enter your name: ")
surname = input("Enter your surname: ")

print("length of the first name - ",len(name))
print("length of the last name - ",len(surname))
vowel_count = name.count('a') + name.count('e') + name.count('i') + name.count('o') + name.count('u')
print("vowels in first name - ",vowel_count)
print("consonants in first name - ",len(name) - vowel_count)
print("first name in uppercase - ",name.upper())
print("first name in lowercase - ",name.lower())
print("last name reversed - ",name[::-1])

print("characters in first name (for loop):")
for n in name:
    print(n)
print("characters in first name (while loop):")
temp_name = name
while len(temp_name) > 0:
    print(temp_name[0])
    temp_name = temp_name[1:]

comp_result = ""
if(len(name) > len(surname)):
    comp_result = "First name is longer than last name."
elif(len(name) < len(surname)):
    comp_result = "Last name is longer than first name."
else:
    comp_result = "First name and last name are equal in length."
print("comparison result - ",comp_result)

print("generated password: ",name[0] + surname[-1] + str(len(name) + len(surname)))

surname_list = list(surname)
surname_list.pop()
surname_list.append('*')
surname_list.insert(0,'@')
surname_list.reverse()
print("List methods example on last name - ", surname_list)