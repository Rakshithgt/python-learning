student = {
    "name": "Rakshith",
    "age": 28,
    "course": "Python",
    "marks": 85,
    "passed": True,
    "email": "rakshithgt222@gmail.com"
}

print(student)
print(type(student))
student["marks"] = 92
print(student)
print(student.get("email"))

student = {
    "name": "Rakshith",
    "age": 28,
    "course": "Python",
    "marks": 92,
    "passed": True
}

for key, value in student.items():
    print(f"{key}: {value}")
    
    
employees = [
    {"name": "Rakshith", "salary": 60000},
    {"name": "Arun", "salary": 45000},
    {"name": "Priya", "salary": 75000},
    {"name": "John", "salary": 40000}
]

for employee in employees:
    if employee["salary"] >= 60000:
        print(employee)