import pandas as pd

data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
    'Age': [20, 22, 19, 21, 20],
    'Grade': ['A', 'B', 'A', 'C', 'B'],
    'Marks': [85, 78, 92, 65, 74] }

students_data = pd.DataFrame(data)

print(students_data)

print(" =============================== ")

value = students_data.head(3)

print(value)

print(" =============================== ")

grade = students_data[(students_data == "A")]

print (grade)

print(" =============================== ")

