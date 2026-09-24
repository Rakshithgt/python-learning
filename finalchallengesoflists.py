marks = [78, 45, 89, 32, 67, 90, 55, 38, 76, 89]

total = sum(marks)
number_of_students = len(marks)
average_marks = total / number_of_students
highest_marks = max(marks)
Lowest_marks = min(marks)

passed_student = 0
failed_student = 0
for mark in marks:
    if mark >= 40:
       passed_student += 1
    else:
        failed_student += 1
        
num = [mark for mark in marks if mark >= 75]

unique_number = []

for mark in marks:
    if mark not in unique_number:
        unique_number.append(mark)
unique_numbers = unique_number.copy()
unique_numbers.sort()
sorted_marks = marks.copy()
sorted_marks.sort()


        
print("------ MARKS REPORT ------")
print(f"All Marks: {marks}")
print(f"Number of Students: {number_of_students}")
print(f"Total Marks: {total}")
print(f"Average Marks: {average_marks}")
print(f"Highest Mark: {highest_marks}")
print(f"Lowest Mark: {Lowest_marks}")
print(f"Passed Students: {passed_student}")
print(f"Failed Students: {failed_student}")
print(f"Marks >= 75: {num}")
print(f"Unique Marks: {unique_number}")
print(f"Sorted Marks: {sorted_marks}")
print(f"Unique: {unique_numbers}")
print(f"Second_highest: {unique_numbers[-2]}")

        
    
    
    