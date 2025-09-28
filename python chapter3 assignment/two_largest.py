first_number = int(input("Enter any number: "))


count = 1
first_largest = first_number
second_largest = first_number

while count <= 10 :
	second_number = int(input("Enter any number: "))
	count = count + 1
	
	if first_largest < second_number :
		first_largest = second_number

	elif first_largest > second_number :
		second_largest = second_number

print(first_number)
print(second_number)



