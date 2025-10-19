first_number = int(input("Enter a number: "))

largest = first_number

smallest = first_number

count = 1
sum = 0
multiply = 1

while count <= 3 :

	second_number = int(input("Enter a number:"))
	count = count + 1
	sum += second_number	
	multiply *= second_number	

	if(largest < second_number):
		largest = second_number

	

	if(smallest < second_number):
		largest = second_number


print("The largest number is",largest)

print("The smallest number is",smallest)






average = sum / 2

print("The sum is",sum)

print("The average is",average)

print("The product is",multiply)