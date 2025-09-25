#prompt user to enter three number each 
#sum the three numbers,get the average number of the three and multiply the three numbers
#reassign the first number to a new variable and check if the new variable is greater than the second number and then reassign the second number to the new #variable,do the same for the third number
#display the result

first_number = int(input("Enter any number: "))

second_number = int(input("Enter any number: "))

third_number = int(input("Enter any number: "))


sum = first_number + second_number + third_number

average = ((first_number + second_number + third_number) / 3)

product = first_number * second_number * third_number


  
smallest = first_number

if(smallest > second_number):
	 smallest = second_number

if(smallest > third_number):
	smallest = third_number

print("The smallest number is", smallest)



highest = first_number

if(highest < second_number):
	 highest = second_number

if(highest < third_number):
	highest = third_number

print("The highest number is", highest)

print("The sum of ", sum)

print("The average is ", average)

print("The product is ", product)







