# Define a Student class
class Student:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.grades = []

    def full_name(self):
        return self.first_name + " " + self.last_name

    def add_grade(self, grade):
        self.grades.append(grade)

    def average_grade(self):
        total = 0
        for g in self.grades:
            total += g
        if len(self.grades) > 0:
            return total / len(self.grades)
        else:
            return 0

# Main program
first = input("Enter first name: ")
last = input("Enter last name: ")

student = Student(first, last)
print("Full name:", student.full_name())

n = int(input("How many grades? "))
for i in range(n):
    student.add_grade(float(input("Enter grade: ")))

print("Average grade:", student.average_grade())
