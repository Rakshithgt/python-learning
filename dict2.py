employees = {
    "EMP001": {
        "name": "Rakshith",
        "age": 28,
        "salary": 60000,
        "skills": ["Python", "SQL", "GenAI"]
    },
    "EMP002": {
        "name": "Arun",
        "age": 30,
        "salary": 70000,
        "skills": ["Java", "AWS", "Docker"]
    }
}

print(employees["EMP001"]["name"])
print(employees["EMP001"]["salary"])
print(employees["EMP001"]["skills"][0])

print(employees["EMP002"]["name"])
print(employees["EMP002"]["salary"])
print(employees["EMP002"]["skills"][0])


for emp_id, employee in employees.items():
    print(emp_id)
    print(f"Name: {employee['name']}")
    print(f"Salary: {employee['salary']}")
    print()
    
for emp_id, employee in employees.items():
    if "Python" in employee["skills"]:
         print(f"Name: {employee['name']}")