employee_1 = ("Rakshith", {"Python", "SQL", "GenAI", "Git", "Docker"})
employee_2 = ("Arun", {"Java", "SQL", "Git", "AWS", "Docker"})

name_1, skills_1 = employee_1
name_2, skills_2 = employee_2

print("------skills Report-------")
print(f"Employee 1: {employee_1}")
print(f"Employee 2: {employee_2}")
print(f"Rakshith Skills: {skills_1}")
print(f"Arun Skills: {skills_2}")
print(f"Common Skills: {skills_1 & skills_2}")
print(f"Only Rakshith: {skills_1 - skills_2}")
print(f"Only Arun: {skills_2 - skills_1}")
print(f"All Skills: {skills_1 | skills_2}")
print(f"Skills possessed by exactly one employee: {skills_1 ^ skills_2}")