# print 1 to 10 using while.

number = 1

while number <= 10:
    print(number)
    number = number + 1 
 

# even numbers

number = 2 

while number <= 20:
    print(number)
    number = number + 2 
    
# Countdown

number = 10

while number >= 1:
    print(number)
    number -= 1
    
print("GO!")

# sum of number

number = 1
total = 0

for number in range(1, 6):
    total = number + total
    print(f"the total value is: {total}")
    
number = 1
total = 0

while number <= 5:
    total += number
    number += 1
print(total)
 
