def get_fareheint(celsius):
	for celsius in range(0, 101):
		fareheint = (9 / 5) * celsius + 32
	return fareheint

def get_product(*numbers):
	result = 1
	
	for num in numbers:
		result *= num
	return result

def seconds_since_midnight(seconds):