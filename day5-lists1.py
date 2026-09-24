fruits = ["apple", "banana", "mango", "orange", "grapes"]
print(fruits)
print(fruits[1])
print(fruits[2])
print(fruits[-1])
print(len(fruits))

languages = ["Python", "Java", "C++"]
languages.append("javascript")
languages.insert(1, "GO")
languages[2] = "c#"
print(languages)


numbers = [10, 20, 30, 40, 50]

numbers.remove(30)
numbers.pop()
removed_number = numbers.pop()
print(numbers)
print(removed_number)

names = ["Rakshith", "Arun", "Priya", "John"]
for name in names:
    print(f"Hello {name}")
        
numbers = [12, 7, 9, 20, 33, 42, 55, 60]

for number in numbers:
    
    if number % 2 == 0:
        print(number)
    
    
 

