def salary_report(*salaries):
    total = 0
    highest = salaries[0]
    lowest = salaries[0]
    
    for salary in salaries:
        total += salary
        if salary > highest:
            highest = salary
        if salary < lowest:
            lowest = salary

    number_of_salaries = len(salaries)
    average = total / number_of_salaries
    return total, average, highest, lowest

total, average, highest, lowest = salary_report(
    50000,
    60000,
    75000,
    45000
)

print(f"Total: {total}")
print(f"Average: {average}")
print(f"Highest: {highest}")
print(f"Lowest: {lowest}")