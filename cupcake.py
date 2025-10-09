def get_smallest(number):
	smallest = number[0]
	for index in range(len(number)):
		if smallest > number[index]:
			smallest = number[index]
	return smallest


def get_average(number):
	total = 0
	count = 0
	sum = 0	
	for index in range(len(number)):
		sum += number[index]
		count += 1
	total = sum / count
	return total

def get_occurence(number, target_number):
	target_count = 0
	for index in range(len(number)):
		if number[index] == target_number:
			target_count += 1
	return target_count


def get_element(number, target_number):
	target_count = 0
	for index in range(len(number)):
		if number[index] == target_number:		
			return True

def get_first_element(number):
	first_list = number[0]
	for index in range(len(number)):
		first_list = number[0]
	return first_list

def get_last_element(number):
	last_list = number[0]
	for index in range(len(number)):
		last_list = number[index]
	return last_list	

def get_length(number):
	number_element = 0
	for index in number:
		number_element += 1
	return number_element
	

def get_middle(number):
	first_element = 0
	middle_number = 0
	last_index = len(number) - 1
	for index in range (len(number)):
		if last_index % 2 == 0:
			first_element = last_index // 2
			middle_number = first_element + 1
	return middle_number
			
			

	

	







number1 = [5, 7, 12, 6, 12, 2]
print(get_middle(number1))

		
	