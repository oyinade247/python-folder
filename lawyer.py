import random
def random_number(number, number2):
	for index in random.sample(range(number, number2)):
		return index


def get_length(number):
	number_element = 0
	for index in number:
		number_element += 1
	return number_element



def get_even_length(number):
	sum = 0
	#length = len(number) - 1
	for index in range(0, len(number), 2):
		sum += number[index]
	return sum


def get_odd_length(number):
	sum = 0
	for index in range(0,len(number), 1):
		#if number[index] % 2 == 0 :
			sum += number[index]
	return sum









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






def get_sequential(number):
	count = 0
	for index in range(len(number)):
		count += 1
	return number

	


def get_even(numbers):
	even = 0
	
	for number in numbers:
		if number % 2 == 1:
			even =+ 1

	list = [0] * even
	store = 0
	for index in range(0, len(numbers)):
		if numbers[index] % 2 == 1:
			list[store] = numbers[index]
			store += 1
	return store
	
	
		 
	








number1 = [2, 3, 4, 1,8, 10 ]
print(get_even(number1))
