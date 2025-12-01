#FUNCTION-BASED APPROACH
def fb_full_name(first_name, last_name):
    return first_name + " " + last_name

def fb_average_grade(grades):
    if not grades:
        return 0
    total = 0
    for g in grades:
        total += g
    return total / len(grades)

def demo_function_based():
    first = "Anna"
    last = "Petrova"
    grades = [8, 9, 10, 7]

    print("Function-based approach")
    print("Full name:", fb_full_name(first, last))
    print("Grades:", grades)
    print("Average grade:", fb_average_grade(grades))
    print()


#FUNCTIONAL PROGRAMMING
def fp_full_name(first_name, last_name):
    return " ".join([first_name, last_name])

def fp_average_grade(grades):
    if not grades:
        return 0
    def add_all(nums):
        if not nums:
            return 0
        return nums[0] + add_all(nums[1:])
    total = add_all(grades)
    return total / len(grades)

def demo_functional():
    first = "Marks"
    last = "Ozols"
    grades = [6, 7, 8, 9]

    print("Functional programming approach")
    print("Full name:", fp_full_name(first, last))
    print("Grades:", grades)
    print("Average grade:", fp_average_grade(grades))
    print()


#OOP APPROACH
class Person:

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def full_name(self):
        return self.first_name + " " + self.last_name

class Student(Person):

    def __init__(self, first_name, last_name, grades=None):
        super().__init__(first_name, last_name)
        self.grades = list(grades) if grades is not None else []

    def add_grade(self, grade):
        self.grades.append(grade)

    def average_grade(self):
        if not self.grades:
            return 0
        return sum(self.grades) / len(self.grades)

def demo_oop():
    student = Student("Elina", "Kalnina", [9, 10, 8])
    student.add_grade(7)

    print("OOP approach")
    print("Full name:", student.full_name())
    print("Grades:", student.grades)
    print("Average grade:", student.average_grade())
    print()


def main():
    demo_function_based()
    demo_functional()
    demo_oop()


if __name__ == "__main__":
    main()