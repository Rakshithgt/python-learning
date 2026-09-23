for number in range(1, 11):
    if number == 6:
        break

    print(number)
    
for number in range(1, 11):
    if number == 5:
        continue

    print(number)
    
for number in range (1, 21):
    if number % 3 == 0:
        continue
    print(number)

while True:
    password = input("Enter the password: ")
    if password == "python123":
        print("login successful")
        break
    print("Incorrect password. Try again.")
    