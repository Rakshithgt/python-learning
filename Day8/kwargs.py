def show_employee(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")


show_employee(
    name="Rakshith",
    age=28,
    salary=60000,
    department="GenAI"
)

def create_profile(**kwargs):
    return kwargs
 
profile = create_profile(
    name="Rakshith",
    role="Developer",
    active=True
)

print(profile)


def employee_report(name, **details):
    print(f"Employee: {name}")
    
    for key, value in details.items():
        print(f"{key}: {value}")
        
employee_report(
    "Rakshith",
    age=28,
    salary=60000,
    department="GenAI",
    location="Bengaluru"
)


def developer_profile(name, *skills, **details):
    print(f"Name: {name}")

    print("Skills:")
    for skill in skills:
        print(skill)

    print("Details:")
    for key, value in details.items():
        print(f"{key}: {value}")

    
    
    
developer_profile(
    "Rakshith",
    "Python",
    "SQL",
    "GenAI",
    "Docker",
    age=28,
    experience=5,
    role="GenAI Developer"
)
