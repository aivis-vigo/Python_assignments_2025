#   1. FUNCTIONAL APPROACH

# Full name using lambda (functional)
full_name_functional = (lambda first, last: f"{first} {last}")("Jana", "Doe")

# Average grade 
grades_functional = [37, 90, 75, 45]
average_functional = (lambda nums: sum(nums) / len(nums))(grades_functional)

print("=== Functional Approach ===")
print("Full name:", full_name_functional)
print("Grades:", " ".join(map(str, grades_functional)))
print("Average grade:", average_functional)
print()

#   2. FUNCTION-BASED APPROACH

def get_full_name(first, last):
    return f"{first} {last}"

def average_grade(grades):
    return sum(grades) / len(grades)

grades_list = [37, 90, 55, 44]

print("=== Function-Based Approach ===")
print("Full name:", get_full_name("Justin", "Black"))
print("Grades:", " ".join(map(str, grades_list)))
print("Average grade:", average_grade(grades_list))
print()

#   3. OOP APPROACH

class Person:
    def __init__(self, first, last):
        self.first = first
        self.last = last

    def full_name(self):
        return f"{self.first} {self.last}"

class Student:
    def __init__(self, grades):
        self.grades = grades

    def average(self):
        return sum(self.grades) / len(self.grades)

person = Person("Mila", "Kerpe")
student = Student([37, 33, 75, 44])  

print("=== OOP Approach ===")
print("Full name:", person.full_name())
print("Grades:", " ".join(map(str, student.grades)))
print("Average grade:", student.average())
print()
