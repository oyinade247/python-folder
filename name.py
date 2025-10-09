def get_length(word):
	length = 0
	for char in str(word):
		length += 1
	return length


def get_reverse(word):
	reversed = ""
	for char in str(word):
		reversed = char + reversed
	return reversed

def get_seconds(number):
	seconds = 60 * number
	hour = number / 60

	return (hour, seconds)


def get_vowel(word):
	vowel = ["a","e","i","o","u"]
	vowel_count = " "
	vowel_length = 0
	
	for char in word.lower():
		if char in vowel:
			vowel_length += 1
			vowel_count += char
			
			
	return vowel_length, vowel_count
				
		
		
	





first_name = input("Enter your name ? ")
#time = int(input("enter minutes:"))

#print(get_length(first_name))
#print(get_reverse(first_name))
#print(get_seconds(time))
print(get_vowel(first_name))




	
	