from expense_utils import add_expense, read_expenses, FILE

# Optional: show where the expenses file is
print("Expenses file:", FILE)

# Add some example expenses
add_expense("Coffee", 3.5)
add_expense("Book", 12.0)
add_expense("Lunch", 8.25)

# Print all expenses
print("\nExpense Log:")
for expense in read_expenses():
    print(expense.strip())
