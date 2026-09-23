#print numbers
for i in range(11):
    print(i)
    
 # print even numbers   
for number in range(1, 20):
    if number % 2 == 0:
        print(number)
    
#countdown
for j in range(10, 0, -1):
    print(j)
print("Happy new year!")


# characters in name

name = "Rakshithgt"

for character in name:
    print(character)
    
    
# 5 tables

number = int(input("Enter the number: "))

for i in range (0, 11, 1):
    result = number * i
    print(f"the tables of 5 is: {number}*{i} = {result}")

