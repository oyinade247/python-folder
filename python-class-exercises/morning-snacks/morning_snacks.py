def square_number(numbers):
	return numbers ** 2
	
numbers = [1,2,3,4,5]

squared_numbers = list(map(square_number, numbers))
print(squared_numbers)



def length_of_string(words):
	return len(words)


word = ["Apple", "Banana","Cherry"]

length_word = list(map(length_of_string,word))
print(length_word)




def print_even_numbers(numbers):
	return numbers %  2 == 0
	
number = [1,2,3,4,5,6]

get_even_number = list(filter(print_even_numbers, number))
print(get_even_number)



def print_words_with_five_characters(words):
	if len(words) > 5 :
		return words

word = ["apple", "banana", "kiwi", "grapes", "cherry"]

length_of_five = list(filter(print_words_with_five_characters, word))
print(length_of_five)



from functools import reduce

def add_hypen_to_strings(words, word):
	return words + "-" + word

word = ["i", "love", "python", "snacks"]

add_hyphen = reduce(add_hypen_to_strings, word)
print(add_hyphen)



