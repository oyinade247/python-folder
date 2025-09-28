factorial = int(input("Enter any number: "))

count = 1
sum = 0
multiply = 1
while(count <= factorial):
	sum += (factorial - count) * multiply
	print(sum)