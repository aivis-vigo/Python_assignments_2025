from datetime import datetime
import os

# Ensure expenses.txt is always in the same folder as this module
FILE = os.path.join(os.path.dirname(__file__), "expenses.txt")

def add_expense(item, amount):
    """Add a new expense with a timestamp to the file."""
    with open(FILE, "a") as f:
        time = datetime.now().strftime("%Y-%m-%d %H:%M")
        f.write(f"{time} - {item}: ${amount}\n")

def read_expenses():
    """Read all expenses from the file."""
    try:
        with open(FILE, "r") as f:
            return f.readlines()
    except FileNotFoundError:
        return []
