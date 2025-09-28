
passes = 0

failures = 0

count = 1

while(count <= 10):
	grade = int(input("Enter your result(Enter 1 for passes and enter two for failure) : "))
	count += 1

	if(grade == 1 ):
		passes = passes + 1

	elif(grade == 2):
		failures = failures + 1

	else:
		grade = int(input("Enter a valid result(Enter 1 for passes and enter two for failure) : "))
		count -= 1


print(passes)
print(failures)
 

