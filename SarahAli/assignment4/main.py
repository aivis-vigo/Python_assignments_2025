import string
import secrets

def generate_password_from_info():
    # 1. Ask user for input
    first_name = input("First name: ").strip()
    last_name = input("Last name: ").strip()
    phone = input("Phone number: ").replace(" ", "").replace("-", "")

    # 2. Build password parts
    # First 2 letters of first name (uppercase)
    part1 = first_name[:2].upper()
    # Last 2 letters of last name (lowercase)
    part2 = last_name[-2:].lower()
    # Last 4 digits of phone reversed
    part3 = phone[-4:][::-1]
    # Random digit
    random_digit = secrets.choice(string.digits)
    # Random symbol
    random_symbol = secrets.choice(string.punctuation)

    # 3. Combine all parts
    password = part1 + part2 + part3 + random_digit + random_symbol

    # 4. Show steps
    print("\nSteps:")
    print(f"- First 2 letters (uppercase): {part1}")
    print(f"- Last 2 letters (lowercase): {part2}")
    print(f"- Last 4 digits reversed: {part3}")
    print(f"- Random digit: {random_digit}")
    print(f"- Random symbol: {random_symbol}")

    # 5. Print final password
    print("\nGenerated password:", password)

    # 6. Save password to file
    with open("passwords.txt", "a") as file:
        file.write(password + "\n")

# Run the function
generate_password_from_info()
