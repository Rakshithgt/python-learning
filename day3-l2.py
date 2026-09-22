Marks = int(input("Enter the Marks: "))

if 90 <= Marks <= 100:
    print("Grade A")
elif 80 <= Marks <= 89:
    print("Grade B")
elif 70 <= Marks <= 79:
    print("Grade C")
elif 60 <= Marks <= 69:
    print("Grade D")
elif 0 <= Marks <= 60:
    print("Grade F")
elif Marks > 100:
    print("invalid")
elif Marks < 0:
    print("Invalid")
    

correct_username = "admin"
correct_password = "python123"

correct_username = input("Enter the username: ")
correct_password = input("Enter the password: ")

if correct_username == "admin" and correct_password == "python123":
    print("Login successfull")
else:
    print("invalid username and password")
    
Emp_Name = input("Enter the Employee Name: ")
Salary = int(input("Enter the salary: "))
Years_of_Experience = int(input("Enter the Years of Exp: "))

Performance_Rating = int(input("Enter the performance rating: "))
if Performance_Rating >= 4 and Years_of_Experience >= 5:
    Bonus = 20 / 100 * Salary
elif Performance_Rating >= 3 and Years_of_Experience >= 3:
     Bonus = 10 / 100 * Salary
else:
   Bonus = 0

Total_salary = Bonus + Salary
print(f"the total salary is: {Total_salary}")
    
