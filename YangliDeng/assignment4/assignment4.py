import string        # Used for digits and symbols
import secrets       # Used for secure random choices
import os            # Used to save file in the same folder as this script

def generate_password_from_info():
    # Ask user for input
    first_name = input("First name: ").replace(" ", "")
    last_name = input("Last name: ").replace(" ", "")
    phone = input("Phone number: ").replace(" ", "").replace("-", "")

    # Ask how many random digits and symbols to add
    num_digits = int(input("How many random digits? "))
    num_symbols = int(input("How many random symbols? "))

    # Take first 2 letters of first name (uppercase)
    part1 = first_name[:2].upper()

    # Take last 2 letters of last name (lowercase)
    part2 = last_name[-2:].lower()

    # Take last 4 digits of phone number and reverse them
    part3 = phone[-4:][::-1]

    # Generate random digits
    digits = ""
    for i in range(num_digits):
        digits += secrets.choice(string.digits)

    # Generate random symbols
    symbols = ""
    for i in range(num_symbols):
        symbols += secrets.choice(string.punctuation)

    # Combine all parts to form the password
    password = part1 + part2 + part3 + digits + symbols

    # Ensure password is at least 8 characters long
    while len(password) < 8:
        password += secrets.choice(string.digits)

    # Create file path in the same folder as this script
    file_path = os.path.join(os.path.dirname(__file__), "passwords.txt")

    # Save the password to the file
    with open(file_path, "a") as file:
        file.write(password + "\n")

    # Print the generated password
    print("Generated password:", password)


# Call the function
generate_password_from_info()
