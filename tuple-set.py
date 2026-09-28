data = ("Rakshith", 28, "Python", "AI", "GenAI")

name, age, *skills = data

print(name)
print(age)
print(skills)

x = 100
y = 200

x, y = y, x

print(x)
print(y)

employees = {"A", "B", "C", "D", "E"}
python_team = {"A", "C", "E"}
java_team = {"B", "D"}

print(python_team.issubset(employees))
print(employees.issuperset(java_team))
print(python_team.isdisjoint(java_team))

