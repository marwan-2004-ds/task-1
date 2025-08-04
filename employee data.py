employees = {}

while True:
    emp_no = input("Enter employee number (or 'done' to finish): ")
    if emp_no.lower() == 'done':
        break

    name = input("Enter employee name: ")
    age = input("Enter employee age: ")
    department = input("Enter employee department: ")

    employees[emp_no] = {
        'name': name,
        'age': age,
        'department': department
    }

print("\nEmployee Data:")
for emp_no, info in employees.items():
    print(f"Employee No: {emp_no} | Name: {info['name']} | Age: {info['age']} | Department: {info['department']}")
