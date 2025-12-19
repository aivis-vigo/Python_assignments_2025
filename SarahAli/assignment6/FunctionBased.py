# Function to generate full name
def get_full_name(first, last):
    return first + " " + last

# Function to compute average
def compute_average(grades):
    total = 0
    for g in grades:
        total += g
    return total / len(grades)

# Main program
first_name = input("Enter first name: ")
last_name = input("Enter last name: ")
print("Full name:", get_full_name(first_name, last_name))

grades = []
n = int(input("How many grades? "))
for i in range(n):
    grades.append(float(input("Enter grade: ")))

print("Average grade:", compute_average(grades))
