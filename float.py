def only_floats(a, b):

	if type(a) and type(b) == float() :
		return 2

	elif type(a) and type(b) != float() :
		return 0
	

	else: 
		return 1


	

	
	
number_one = input("enter a number: ")

number_two = input("enter a number: ")

print(only_floats(number_one, number_two))

	