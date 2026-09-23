correct_password = "python123"
attempts = 0

while True:
    password = input("Enter the password: ")
    
    if password == correct_password:
        print("login successful")
        break
    
    attempts += 1
    attempts_left = 3 - attempts
    
    if attempts == 3:
        print("account is locked")
        break 
    
    print(f"invalid password. Attempts left: {attempts_left}")