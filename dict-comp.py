employees = {
    "Rakshith": 60000,
    "Arun": 45000,
    "Priya": 75000,
    "John": 40000
}

salaries = {employees: salary for employees, salary in employees.items() if salary > 50000}
print(salaries)