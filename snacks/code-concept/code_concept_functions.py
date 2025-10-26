def create_tuple(numbers, digit):
	new_tuple = ()
	for num in numbers:
		new_tuple += (num,)
	new_tuple += (digit)
	return new_tuple
		

number_one = (1,3,4,5,7)
print(create_tuple(number_one,(5,)))


def change_element(numbers):
	new_tuple_2 = ()
	change_to_list = list(numbers)
	change_to_list[2][1] = 99
	for num in change_to_list:
		new_tuple_2 += (num,)
	return new_tuple_2
		

new_tuple = (1, 2, [3, 4], 5)	
print(change_element(new_tuple))



def add_fruit(words):
	new_tuple = ()
	change_to_tuple = list(words)
	change_to_tuple.append("mango")
	for fruit in change_to_tuple:
		new_tuple += (fruit,) 
	return new_tuple


fruits = ('apple', 'banana', 'cherry')
print( add_fruit(fruits))




def unpack_tuple(*numbers):
	for num in numbers:
		pass
	return num
	

numb = (10, 20, 30, 40)

print(unpack_tuple(*numb))



#def sum_three_list(numbers):
	#new_list = []
	#for num in n:
		

#numbers = [ [2, 3, 4],  [1, 5, 7],  [4, 6, 8] ]
#print(sum_three_list())

#def sum_element_in_row():




# filter

def get_even_number(numbers):
	return numbers % 2 == 0

numb = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
even_numbers = list(filter(get_even_number,numb))
print(even_numbers)


def get_five_letters(words):
	return  len(words) > 5

word = ["cat", "elephant", "tiger", "lion"]
five_letters = list(filter(get_five_letters,word))
print(five_letters)



#def get_higher_than_two(numbers):
		

	#return len(numbers) > 2

#greater =  [(1, 'A'), (4, 'B'), (2, 'C')]
#highest = list(filter(get_higher_than_two, greater))
#print(highest)


def get_divisible_number(numbers):
	return numbers % 3 == 0 and numbers % 5 == 0

num = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50]
divisible_numbers = list(filter(get_divisible_number,num))
print(divisible_numbers)



def palindrome(words):
	return words == str(words)[::-1]

word =  ['level', 'world', 'madam', 'python']
palindromes = list(filter(palindrome, word))
print(palindromes)


#map

def convert_string(words):
	return words.upper()

word = ['python', 'java', 'c++'] 
converted_string = list(map(convert_string,word))
print(converted_string)



def square_numbers(numbers):
	return numbers ** 2

numbers = [1,2,3,4,5,6,7,8,9,10]
squared_numbers = list(map( square_numbers,numbers ))
print(squared_numbers)


#def capitalize_names(names):
	#for name in names:
		#name.upper()
	#return name

	
#words = ['john', 'mary','steve']
#capital_name = list(map(capitalize_names, words))
#print(capital_name)
	


def add_tax(numbers): 
	return numbers + 0.10

number = [100, 200, 300]
percentage = list(map(add_tax,number))
print(percentage)


#reduce 

from functools import reduce

def sum_number(numbers,num):
	return numbers + num

num = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50]
sum_of_numbers = reduce( sum_number, num)
print(sum_of_numbers)



from functools import reduce

def find_max(numbers,number):
	if number > numbers:
		return number
	else:
		return numbers

number = [3, 5, 9, 2, 8]
highest = reduce(find_max, number)
print(highest)


from functools import reduce

def concatenate_string(words, word):
	return words + " " + word
	
sentence = ['I', 'love', 'Python'] 
concantenated = reduce(concatenate_string, sentence)
print(concantenated)


#
from functools import reduce

def product_and_squares(numbers):
	square = numbers ** 2
	return square

numb = [1, 2, 3, 4]
squared = list(map(product_and_squares, numb)) 
def get_product(squared, product):
	return squared * product

product = reduce(get_product,numb)
print(product)









	













	



		






	
	
 














