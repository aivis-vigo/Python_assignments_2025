"""
This is a homework with brain exercises.
"""
import string
import secrets

def generate_password_from_info():
    first = input("Enter first name: ").strip()
    last = input("Enter last name: ").strip()
    phone = input("Enter phone number: ").strip()

    # Clean input
    phone = phone.replace(" ", "").replace("-", "")

    num_digits = int(input("How many random digits to add? "))
    num_symbols = int(input("How many random symbols to add? "))

    part1 = first[:2].upper()           # first 2 letters uppercase
    part2 = last[-2:].lower()           # last 2 letters lowercase
    part3 = phone[-4:][::-1]            # last 4 digits reversed

    # Generate random digits and symbols
    random_digits = ''.join(secrets.choice(string.digits) for _ in range(num_digits))
    random_symbols = ''.join(secrets.choice(string.punctuation) for _ in range(num_symbols))

    password = part1 + part2 + part3 + random_digits + random_symbols

    # Ensure password is at least 8 characters long
    while len(password) < 8:
        password += secrets.choice(string.ascii_letters + string.digits)

    # Save
    with open("passwords.txt", "a") as f:
        f.write(password + "\n")

    return password

print("Generated password:", generate_password_from_info())
