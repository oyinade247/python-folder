def print_non_occurence(words):
	new_list = []
	word_list = list(words)
	print(word_list)
	for char in word_list:
		for letter in word_list:
			if char not in word_list:
				return char		


word = "little"

print( print_non_occurence(word));