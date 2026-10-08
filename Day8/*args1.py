def show_numbers(*args):
    for number in args:
        print(number)
    return number

show_numbers(10, 20, 30, 40, 50)

# add a number
def calculate_total(*args):
    total = 0
    for number in args:
        total += number
    return total

print(calculate_total(10, 20))
print(calculate_total(10, 20, 30))
print(calculate_total(1, 2, 3, 4, 5))

# largest number
def find_largest(*args):
    highest = args[0]
    for number in args:
        if number > highest:
            highest = number
    return highest

print(find_largest(10, 50, 20, 90, 30))
print(find_largest(-10, -50, -3, -20))