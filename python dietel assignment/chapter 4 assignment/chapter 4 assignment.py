def get_fareheint(celsius):
	for celsius in range(0, 101):
		fareheint = (9 / 5) * celsius + 32
	return fareheint

def get_product(*numbers):
	result = 1
	
	for num in numbers:
		result *= num
	return result

def guess_number(number):
	guess_number = 567
	number = int(input("enter a number between 1 - 1000:"))
	while number != guess_number:
		if number > guess_number:
			print("You guess")
		elif number < guess_number:

def second(hour,minutes, seconds):
	seconds