first_number = int(input("Enter a number: "))

second_number = int(input("Enter a number: "))

third_number = int(input("Enter a number: "))

fourth_number = int(input("Enter a number: "))



number_one = first_number 

if( number_one > second_number):
	number_one = second_number

elif(number_one > third_number):
	number_one = third_number

elif(number_one > fourth_number):
	number_one = fourth_number



number_four = first_number

if( number_four < second_number):
	number_four = second_number

elif(number_four < third_number):
	number_four = third_number

elif(number_four < fourth_number):
	number_four = fourth_number


sum = first_number + second_number + third_number + fourth_number

highest_lowest = number_one + number_four


median = (sum - highest_lowest) // 2

mean =  sum // 4

print("The median is" ,median)

print("The sum is",sum)

print("The mean is",mean)