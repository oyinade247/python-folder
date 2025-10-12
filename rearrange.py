"""even = [] 
	for index in range(0, len(numbers), 2):
		if numbers[index] % 2 == 1:
			even.append(numbers[index])
	
	
	odd = []
	for num in range(-1, -7, -1):
		if numbers[num] % 2 == 1:
			odd.append(numbers[num])

	return even + odd"""


def rearrange_number(numbers):
	rearrange = [] * len(numbers)
	first = [0] 
	print(first)
	for index in range(len(numbers)):
		if index in numbers > first:			
			rearrange.append(numbers[index])
	return rearrange
		




num = [3, 14, 7, 21, 8, 78, 23]
print(rearrange_number(num))


		