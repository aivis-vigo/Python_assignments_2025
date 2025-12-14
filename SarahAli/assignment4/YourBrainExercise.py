import string
import secrets

def generate_password_from_info():
    # 1. Ask user for input
    first_name = input("First name: ").strip()
    last_name = input("Last name: ").strip()
    phone = input("Phone number: ").replace(" ", "").replace("-", "")

    # 2. Ask how many random digits and symbols to add
    try:
        num_digits = int(input("How many random digits to add? "))
    except ValueError:
        num_digits = 1  # default if user types wrong

    try:
        num_symbols = int(input("How many random symbols to add? "))
    except ValueError:
        num_symbols = 1  # default if user types wrong

    # 3. Build password parts
    part1 = first_name[:2].upper()
    part2 = last_name[-2:].lower()
    part3 = phone[-4:][::-1]

    # 4. Generate random digits and symbols
    digits = "".join(secrets.choice(string.digits) for _ in range(num_digits))
    symbols = "".join(secrets.choice(string.punctuation) for _ in range(num_symbols))

    # 5. Combine all parts
    password = part1 + part2 + part3 + digits + symbols

    # 6. Ensure at least 8 characters
    while len(password) < 8:
        password += secrets.choice(string.digits)

    # 7. Show steps
    print("\nSteps:")
    print(f"- First 2 letters (uppercase): {part1}")
    print(f"- Last 2 letters (lowercase): {part2}")
    print(f"- Last 4 digits reversed: {part3}")
    print(f"- Random digits: {digits}")
    print(f"- Random symbols: {symbols}")

    # 8. Print final password
    print("\nGenerated password:", password)

    # 9. Save password to file safely
    try:
        with open("passwords.txt", "a") as file:
            file.write(password + "\n")
        print("Password successfully saved in 'passwords.txt'.")
    except Exception as e:
        print("Error saving password:", e)

# Run the function
generate_password_from_info()
