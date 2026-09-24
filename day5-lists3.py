numbers = [1, 2, 3, 4, 5]

squares = [number ** 2 for number in numbers ]

print(squares)


numbers = [10, 15, 20, 25, 30, 35, 40]

num = [number for number in numbers if number % 2 == 0]

print(num)

numbers = [45, 12, 78, 34, 89, 23, 67]

num = [number for number in numbers if number > 50]

print(num)