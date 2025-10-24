def convert_type(numbers):
	if type(numbers) == str:
		return int(numbers)

number = ["1", "2", "3"]
converted = list(map(convert_type,number))
print(converted)


def add_number(numbers):
	return numbers + 10

number = [0,5,10,15]
added_numbers = list(map(add_number,number))
print(added_numbers)


def convert_to_fahrenheit(numbers):
	return numbers + (numbers * 1.8 + 32)

celsius = [0,20,37,100]
converted_number = list(map(convert_to_fahrenheit, celsius))
print(converted_number)



def remove_values(numbers):
	if type(numbers) == int:
		return numbers

number = [1, None, 3,None, 5]
removed = list(filter(remove_values,number))
print(removed)




def extract_divisible_numbers(numbers):
	return numbers % 3 == 0

number = [1,3,4,6,9,12]
divisible_number = list(filter(extract_divisible_numbers, number))
print(divisible_number)



def print_positive_number(numbers):
	return numbers > 0

number = [-2,-1,0,1,2]
positive_numbers = list(filter(print_positive_number,number))
print(positive_numbers)



def return_greater_number(numbers):
	if numbers["age"] > 25:
		return numbers


my_dict = [{"name" : "Alice", "age": 30},    {"name": "Bob", "age": 20}]
age = list(filter(return_greater_number,my_dict ))
print(age)


from functools import reduce
def reduce_numbers(numbers, number):
	return numbers + number

number = [1,2,3,4,5]
shrinked_number = reduce(reduce_numbers,number)
print(shrinked_number)



from functools import reduce
def print_product_of_numbers(numbers, product):
	return numbers * product

number = [2,3,4]
multiplied_numbers = reduce( print_product_of_numbers,number)
print(multiplied_numbers)



from functools import reduce
def highest_value(numbers, number):
	if number > numbers:
		return number
	else:
		return numbers

max = [3,7,2,9,1]
max_number = reduce(highest_value, max)
print(max_number)





from functools import reduce
def concatenate_string(words,word):
	return words + word

word = ["Hello", "","World"]
joined_word = reduce(concatenate_string, word)
print(joined_word)




from functools import reduce
def merge_lists(first_list, second_list):
	return first_list | second_list
	

list = [{"a": 1}, {"b": 2}, {"c":3}]
joined_list = reduce(merge_lists,list)
print(joined_list)







from functools import reduce
def sum_square(numbers,number):
	return numbers[0] * number

number = [1,2,3]
squared = reduce(sum_square,number)
print(squared)














