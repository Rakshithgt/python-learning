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
    },
    "EMP003": {
        "name": "Priya",
        "age": 26,
        "salary": 75000,
        "skills": ["Python", "GenAI", "FastAPI"]
    },
    "EMP004": {
        "name": "John",
        "age": 32,
        "salary": 45000,
        "skills": ["Python", "Git"]
    }
}

print(len(employees))

for emp_id, employee in employees.items():
    print(emp_id)
    print(f"Name:{employee['name']}")
    print(f"Salary:{employee['salary']}")
    
for emp_id, employee in employees.items():
    if "Python" in employee["skills"]:
        print(f"Name: {employee['name']}")
        
for emp_id, employee in employees.items():
    if "GenAI" in employee["skills"]:
        print(f"Name: {employee['name']}")
        
total_salary = 0

for emp_id, employee in employees.items():
    total_salary += employee["salary"]
avg_salary = total_salary / len(employees)
print(total_salary)
print(avg_salary)

for emp_id, employee in employees.items():
    if employee["salary"] >= 60000:
        print(f"{employee['name']}: {employee['salary']}")
        
highest_salary = 0
highest_paid_employee = ""

for employee in employees.values():
    if employee["salary"] > highest_salary:
        highest_salary = employee["salary"]
        highest_paid_employee= employee["name"]
print(f"Highest paid employee: {highest_paid_employee}")
print(f"Highest salary: {highest_salary}")


d = {emp_id: employee["salary"] for emp_id, employee in employees.items() if employee["salary"] >= 60000}
print(d)
 
all_skills = set()
for emp_id, employee in employees.items(): 
     for skill in employee["skills"]:
            all_skills.add(skill)
print(all_skills)

for emp_id, employee in employees.items(): 
    if "Python" in employee["skills"] and "GenAI" in employee["skills"]:
         print(employee["name"])
            
            
print("------------EMPLOYEE ANALYZER--------------")
print