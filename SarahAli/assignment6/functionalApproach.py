# Step 1: Full name
first_name = input("Enter first name: ")
last_name = input("Enter last name: ")
full_name = first_name + " " + last_name
print("Full name:", full_name)

# Step 2: Store grades and compute average
grades = []
n = int(input("How many grades? "))
for i in range(n):
    grade = float(input("Enter grade: "))
    grades.append(grade)

total = 0
for g in grades:
    total += g

average = total / len(grades)
print("Average grade:", average)
