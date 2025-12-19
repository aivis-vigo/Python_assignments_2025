import random

with open("name_list_generator/names.txt", encoding="utf8") as f:
    data = f.read().splitlines()
    first_names = data[::2]
    last_names = data[1::2]  # Pretend those are surnames


def generate_name() -> str:
    res = ""
    res += random.choice(first_names)
    res += " "
    res += random.choice(last_names)
    return res


def average_grade(grades) -> float:
    total = 0.0
    for val in grades.values():
        total += val
    return total / len(grades)


# example usage

print(generate_name())
grades = {
    generate_name(): 1,
    generate_name(): 2,
    generate_name(): 3,
    generate_name(): 4,
    generate_name(): 5,
    generate_name(): 6,
    generate_name(): 7,
    generate_name(): 8,
    generate_name(): 9,
    generate_name(): 10,
}
print(grades)
print(average_grade(grades))
