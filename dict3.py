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

total_salary = 0

for emp_id, employee in employees.items():
    total_salary += employee['salary']
    average_salary = total_salary / len(employees)
print(total_salary)
print(average_salary)