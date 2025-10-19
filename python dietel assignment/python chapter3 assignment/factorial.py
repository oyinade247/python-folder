factorial = int(input("Enter any number: "))

count = 1
sum = 1


while count < factorial:
	sum += (factorial - count) * sum
	count = count + 1

print(sum)