# Function definitions
def create_student(name, surname):
    return {
        "name":name,
        "surname":surname,
        "grades":[]
    }

def fullname(student):
    return student["name"] + " " + student["surname"]

def add_grade(student, grade):
    student["grades"].append(grade)

def avg_grade(student):
    grade_sum = 0
    for grade in student["grades"]:
        grade_sum += grade
    return grade_sum/len(student["grades"])

# Usage
john = create_student("John", "Doe")
add_grade(john, 7)
add_grade(john, 8)
add_grade(john, 9)
add_grade(john, 6)

print("Function based ---")
print("Full name: ",fullname(john),"\nStored grades: ",john["grades"],"\nAverage: ",avg_grade(john))