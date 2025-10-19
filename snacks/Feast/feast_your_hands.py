def get_third(numbers):

	numbers.pop([2])

	return numbers



def change_last_color(words):
	words.insert(2, "yellow")
	
	return words

def add_word(words):
	words.append("purple")
	
	return words


def element(numbers):
	numbers.remove(3)
	
	return numbers

def return_list(words):
	counter = 0
	count = 0
	new_list = []

	for char in words:
		count += 1
		if char in words:
			new_list.append(len(char))
			counter += 1
			count += 1
	return counter


def sort_list(numbers):

	numbers.sort()
	return numbers


def new_list(numbers):
	new_number = []
	
	for number in numbers:
		if number % 2 == 0:
			new_number.append(number)
	return new_number

def get_combine(numbers, number):
	
	combine = numbers + number
	return combine


def list_strings(words):
	
	new_word_list = []
	count = 0
	for char in words:
		count += 1
		if len(char) == 3:
			new_word_list.append(char)
	return new_word_list

	




		

nums = ["lamb","dod","eggs","mon","jor"]
print(return_list(nums))