'''
This code was changed based on "Challenge" task, I was not sure does that task is a part of our homework or not.
'''
import requests
from helpers import math_tools, file_tools

radius = 5

area = math_tools.circle_area(radius)
circum = math_tools.circle_circumference(radius)

response = requests.get("https://timeapi.io/api/Time/current/zone?timeZone=UTC")
data = response.json()

current_time = f"{data['year']}-{data['month']:02d}-{data['day']:02d} {data['hour']:02d}:{data['minute']:02d}:{data['seconds']:02d}"

text = (
    f"[{current_time}] "
    f"Radius={radius}, Area={area:.2f}, Circumference={circum:.2f}"
)

file_tools.save_to_file("data/results.txt", text)

print("File contents:")
print(file_tools.read_file("data/results.txt"))
