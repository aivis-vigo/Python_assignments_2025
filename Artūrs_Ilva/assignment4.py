import string
import secrets

first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
phone = input("Enter your phone number: ")

first_name = first_name.replace(" ", "").replace("-", "")
last_name = last_name.replace(" ", "").replace("-", "")
phone_digits = "".join(ch for ch in phone if ch.isdigit())

if len(first_name) < 2 or len(last_name) < 2 or len(phone_digits) < 4:
    print("Error: need at least 2 letters in each name and 4 digits in phone.")
else:
    part1 = first_name[:2].upper()

    part2 = last_name[-2:].lower()

    last4_reversed = phone_digits[-4:][::-1]

    rand_digit = secrets.choice(string.digits)
    rand_symbol = secrets.choice(string.punctuation)

    password = part1 + part2 + last4_reversed + rand_digit + rand_symbol

    print("Generated password:", password)
