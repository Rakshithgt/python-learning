name = input("enter the name: ")
last_name = input("enter the last_name: ")
birth_year = input("enter the birth_year: ")

correct_name = (last_name.strip())
last_name1 = correct_name.replace("g t", "gt")


band_generator = name + "." + last_name1 + birth_year
print(band_generator)
