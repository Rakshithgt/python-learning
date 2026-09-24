numbers = [45, 12, 78, 34, 89, 23, 67]

total = sum(numbers)
print(total)
averge = total / len(numbers)
print(averge)
minimum = min(numbers)
maximum = max(numbers)
print(minimum)
print(maximum)
numbers.sort()
print(numbers)

even_count = 0
odd_count = 0

for number in numbers:
    if number % 2 == 0:
        even_count += 1
    else:
        odd_count += 1
        
print(even_count)
print(odd_count)


numbers = [45, 12, 78, 34, 89, 23, 67]

greater_than_50 = []

for number in numbers:
    if number >= 50:
        greater_than_50.append(number)
print(greater_than_50)

numbers = [1, 2, 3, 4, 5]

squares = []
for number in numbers:
    square = number ** 2
    squares.append(square)
print(squares)


languages = ["Python", "Java", "C++", "Go"]

language = input("enter the languages: ")
if language == languages:
    print("python is available")
else:
    print("python is not available")
    
    
numbers = [2, 4, 6, 8, 10]
doubled = []

for number in numbers:
    double = number * 2
    doubled.append(double)
print(doubled)