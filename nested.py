for i in range (1, 4):
    for j in range(1,4):
        print(i, j)
        
        
for row in range(1, 6):
    for cloumn in range(1, row + 1):
        print("*", end= "")
    print()

for row in range(5, 0, -1):
    for column in range(row):
        print("*", end= "")
    print()