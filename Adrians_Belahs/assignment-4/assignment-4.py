import string
import secrets

#Function to clean input
def clean(s: str) -> str:
    return s.replace(" ","").replace("-","")

#Function to get first 2 letters uppercase
def first_two_letters_upp(name: str) -> str:
    return name[:2].upper()

#Function to get last 2 letters lowercase
def last_two_letters_low(name: str) -> str:
    return name[-2:].lower()

#Function to get last 4 digits of phone number reversed
def reverse_last_four(phone: str) -> str:
    # Remove everything except digits
    digits = "".join(ch for ch in phone if ch.isdigit())
    last_four = digits[-4:][::-1]
    return last_four

#Function to get 1 random digit and 1 random symbol
def random_digit_symbol(dig_num: int, sym_num: int) -> str:
    digits,symbols,i,j = "","",0,0
    all_symbols = "!@#$%^&*()-_=+[]{};:,.<>/?"
    while i<dig_num:
        digits += secrets.choice(string.digits)
        i+=1
    while j<sym_num:
        symbols += secrets.choice(all_symbols)
        j+=1
    return digits + symbols

#Combine all elements into a password
def generate_password(a: str, b: str, c: str, d: str) -> str:
    password = a + b + c + d
    return password

#Check if password length is at least 8
def is_legit(password: str) -> bool:
    if len(password)>=8:
        return True
    else: return False

#Save password to a file
def save_to_file(filename, username, password):
    with open(filename, "a") as f:
        f.write(username + " : " + password + "\n")


#Get user input
first_name = str(input("First name: "))         or  "Ad-r ian"
last_name = str(input("Last name: "))           or  "Be   la--h"
phone_number = str(input("Phone number: "))     or  "267-680-51"

#User's choice for password settings
choice_dig = int(input("How many digits to add?: "))
choice_symb = int(input("How many symbols to add?: "))

#Clean all 3 variables for further work
clean_first_name = clean(first_name)
clean_last_name = clean(last_name)
clean_phone_number = clean(phone_number)

#Get 3 elements for password
f_name_first_two_upper = first_two_letters_upp(clean_first_name)
l_name_last_two_low = last_two_letters_low(clean_last_name)
phone_number_rev_last_four = reverse_last_four(clean_phone_number)


#Test
generated_password = generate_password(f_name_first_two_upper, l_name_last_two_low, phone_number_rev_last_four, random_digit_symbol(choice_dig, choice_symb))
print(generated_password)
if is_legit(generated_password):
    print("Password is strong :)")
    save_to_file("user_passwords.txt", clean_first_name, generated_password)
else:
    print("Password is weak :(")