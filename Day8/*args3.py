def employee_skills(name, *skills):
    print(f"Employee: {name}")
    print("skills:")
    
    for skill in skills:
        print(skill)
    return name, skills
        
employee_skills(
    "Rakshith",
    "Python",
    "SQL",
    "GenAI",
    "Docker"
)
