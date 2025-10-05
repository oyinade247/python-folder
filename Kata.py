import math

def is_even(number):
	if number % 2 == 0 :
		return True

	return False


def is_prime(number):
	count = 2
	while count < number :
		if number % count == 0:
			return False
	return True


def positive_difference(number_one, number_two):
	store = 0
	if number_one < number_two:
		store = number_two - number_one
		return store
	elif number_two < number_one:
			store = number_one - number_two
			return store

def get_quotient(number_one, number_two):
	if number_two == 0: 
		return 0
	return number_one / number_two



def factor(number):
	count_factor = 0
	count = 1
	while count < number :
		if number % count == 0 :
			count_factor += 1
			count += 1
			
	print(count_factor)
	

def is_square(number):
	square = math.sqrt(number)
	if square * square == number :
		return True
	return False
	



def is_palindrome(number):
	reversed_number = ""
	for char in str(number):
		reversed_number = char + reversed_number
	return reversed_number == str(number)
	
		
			

def factorial( number):
	sum = 1
	count = 1
	while count < number :
		sum += (number - count) * sum
		count += 1
	return sum


def square(number):
	store = number * number;
	return store;


number_on = 4
number_tw = 0

print(get_quotient(number_on, number_tw))	
