#without global variable
count = 0

def increase_count(count):
    count += 1
    return count
    
count = increase_count(count)
count = increase_count(count)
count = increase_count(count)

print(count)

#with global variable
count = 0

def increase_count():
    global count
    count += 1
    return count
    
count = increase_count()
count = increase_count()
count = increase_count()

print(count)