#prompt two user to enter their age 
#collect the two user's age ranging from 1 to 80
#calculate how many years ago that the first user input is twice as old as the second user input



fathers_age = int(input("Enter your age papa junior(from 1 - 80) :"))
son_age = int(input("Enter your age junior(from 1 -80)"))

calculate_years_ago = son_age * 2

if(fathers_age < calculate_years_ago):
	print(calculate_years_ago - fathers_age)
else:
    print(fathers_age - calculate_years_ago )