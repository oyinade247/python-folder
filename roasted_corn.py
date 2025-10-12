def get_sum(numbers):
	sum = 0
	for number in numbers:
		square = number ** 2
		sum += square
		
	return sum



def get_square(numbers):
	square = []
	for number in numbers:
		multiply = number * number
		square.append(multiply)
	return square 


def multiple_string(letters, number):
	if type(number) == int:
		return letters * number
	if type(number) == float :
		return letters
	

def get_largest(numbers):
	max = numbers[0]
	for number in numbers:
		if number > max:
			max = number
		return max

def get_smallest(numbers):
	min = numbers[0]
	for number in range(len(numbers)):
		if numbers < min:
			min = numbers[number]
		return min

		

def get_vowels(letters):
	vowel = "aeiou"
	vowels = ""
	for char in str(letters):
		if char in vowel:
			vowels += char
	return vowels



def get_longest_word(words):
	longest_word = words[0]
	for word in words:
		if len(word) > len(longest_word):
			longest_word = word
	return longest_word


def adding_suffix(word):
	if len(word) >= 3 and "ing" not in word:
		word += "ing"
	elif "ing" in word:
		word += "ly"
	elif len(word) < 3:
		return word
		
	return word


		
	








			

num2 = {1, 2, 3, 4}
print(get_smallest( num2))


