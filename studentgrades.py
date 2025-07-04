students = [
    {"name": "hesham", "grades": [80, 85, 90]},
    {"name": "Youssef", "grades": [75, 70, 80]},
    {"name": "noor", "grades": [90, 95, 100]}
]

for student in students:
    grades = student["grades"]
    total = sum(grades)
    average = total / len(grades)
    print(student["name"], "Average:", average)
