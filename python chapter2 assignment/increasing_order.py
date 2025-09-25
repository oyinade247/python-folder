#collect three numbers from user in floating points
#check for the lowest number and highest number
#reassign the first user input to another new variable name
 
#compare the variable to the second and third user input to check for the middle number

#reassign the second and third number to the new variable

#display the output



number_one = float(input("Enter the number: "))

number_two = float(input("Enter the number: "))

number_three = float(input("Enter the number: "))



minimum_number = min(number_one, number_two, number_three)

maximum_number = max(number_one, number_two, number_three)



middle_number = number_one
if(middle_number > number_two or middle_number >number_three):
	middle_number = number_two
	middle_number = number_three	


#print the minimum,middle and the maximum number
print("The minimum number",minimum_number)

print("The middle number ", middle_number)

print("The maximum number",maximum_number)