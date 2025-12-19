from functools import reduce

john = {
    "name":"John",
    "surname":"Doe",
    "grades":[]
}
fullname = john["name"] + " " + john["surname"]
student = john | {"grades": [7,8,9,6]}
avg_grade = reduce(lambda a, b: a + b, student["grades"])/len(student["grades"])

print("Functional ---")
print("Full name: ",fullname,"\nStored grades: ",student["grades"],"\nAverage: ",avg_grade)
print("The original john is not mutaded: ", john)