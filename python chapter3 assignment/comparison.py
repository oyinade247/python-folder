number_one = int(input("Enter first integer"))

number_two = int(input("Enter second integer"))

if(number_one == number_two and number_one != number_two):
	print(number_one, 'is equal to' , number_two)

	#print(number_one , "is not equal to", number_two)


elif(number_one < number_two or number_one > number_two):
	print(number_one, 'is less than' , number_two)
	#print(number_one, 'is greater than' , number_two)

elif(number_one <= number_two or number_one >= number_two):
	print(number_one, 'is less than and equals to' , number_two)
	#print(number_one, 'is greater than and equals to' , number_two)