def main():
    number_of_students = int(input("How many students you wanna grade? "))
    
    with open('grades.txt', 'w') as f:
        for _ in range(number_of_students):
            name = input("Name is: ")
            grades = list(map(int, input("Grades are: ").split()))
            average_grade = sum(grades) / len(grades)
            
            f.write(f"{name}: {grades} average grade is: {average_grade}\n")
            print(f"Average grade is: {average_grade}")

main()
