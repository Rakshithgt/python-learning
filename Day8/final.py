employees = {
    "EMP001": {
        "name": "Rakshith",
        "salary": 60000,
        "skills": ["Python", "SQL", "GenAI"]
    },
    "EMP002": {
        "name": "Arun",
        "salary": 70000,
        "skills": ["Java", "AWS", "Docker"]
    },
    "EMP003": {
        "name": "Priya",
        "salary": 75000,
        "skills": ["Python", "GenAI", "FastAPI"]
    },
    "EMP004": {
        "name": "John",
        "salary": 45000,
        "skills": ["Python", "Git"]
    }
}

def calculate_total_salary(employees):
    total = 0

    for employee in employees.values():
        total += employee["salary"]

    return total

print(calculate_total_salary(employees))

def find_highest_paid(employees):
    highest_salary = 0
    highest_paid_employee = ""
    
    for employee in employees.values():
        if employee["salary"] > highest_salary:
            highest_salary = employee["salary"]
            highest_paid_employee = employee["name"]
    return highest_salary,  highest_paid_employee
salary, name = find_highest_paid(employees)

print(name)
print(salary)

def find_by_skills(employees, skill):
    matched_employees = []
    
    for employee in employees.values():
        if skill in employee["skills"]:
            matched_employees.append(employee["name"])
    return matched_employees
print(find_by_skills(employees, "Python"))


def employee_summary(employees):
    count = len(employees)
    total = calculate_total_salary(employees)
    average = total / count
    
    return count, total, average
    
count, total, average = employee_summary(employees)

print(count)
print(total)
print(average)
    
                          

