class Student:
    def __init__(self, name, surname):
        self.name = name 
        self.surname = surname
        self.grades = []

    def fullname(self):
        return self.name + " " + self.surname

    def add_grade(self, grade):
        self.grades.append(grade)

    def avg_grade(self):
        if len(self.grades) == 0: return 0
        return sum(self.grades)/len(self.grades)
    
student = Student("John","Doe")
student.add_grade(7)
student.add_grade(8)
student.add_grade(9)
student.add_grade(6)

print("OOP ---")
print("Full name: ",student.fullname(),"\nStored grades: ",student.grades,"\nAverage: ",student.avg_grade())