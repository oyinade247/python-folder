import random
def random_number(number):
	for number in range(10):
		print(random.randint(1,51))		


def get_length(number):
	number_element = 0
	for index in number:
		number_element += 1
	return number_element



def get_even_length(number):
	add_even = 0
	for index in range(0, len(number), 2):
		add_even += number[index]
	return add_even


def get_odd_length(number):
	add_odd = 0
	for index in range(1,len(number), 2):
		add_odd += number[index]
	return add_odd


def multiply_element(number):
	multiply = 1;
	for index in range(2,len(number), 2):
		multiply *= number[index];
	return multiply



def get_average(number):
	total = 0
	count = 0
	sum = 0	
	for index in range(len(number)):
		sum += number[index]
		count += 1
	total = sum / count
	return total



def get_largest(number):
	largest = number[0]
	for index in range(len(number)):
		if largest < number[index]:
		 largest = number[index]
	return largest


def get_smallest(number):
	smallest = number[0]
	for index in range(len(number)):
		if smallest > number[index]:
			smallest = number[index]
	return smallest



def get_first_last(words):
	for word in words:
		if len(word) > 2 and word[0] == word[-1] :
			return word

		



def get_sequential(numbers):
	count = 0
	for index in range(len(number)):
		count += 1
	return number

	

def add_third(numbers):
	add_third = 0
	for number in range(2,len(numbers),2):
		add_third += numbers[number]
	return add_third

def calculate(numbers):
	add_all = 0
	

		




	
	
		 
	








number1 = ["dod", "epe"]
print( get_first_last(number1))
