def greet(name):
    print(f"Hello {name}!")
greet("Rakshith")
greet("Arun")


def add(a, b):
    result = a + b
    return result
answer = add(20, 30)
print(answer)


def check_number(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "odd"
 
print(check_number(10))
print(check_number(7))


def find_largest(a, b):
    if a > b:
        return a
    elif b > a:
        return b
    else:
        return a
largest = find_largest(20, 50)
print(largest)
print(largest * 2)


def calculate_salary(salary, bonus_percentage):
    bonus_amount = salary * (bonus_percentage / 100)
    total_salary = salary + bonus_amount
    return bonus_amount, total_salary
bonus, total_salary = calculate_salary(6000, 20)
print(total_salary)
print(bonus)