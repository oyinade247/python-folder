number = int(input("Enter a number :  "))


divided_number  = ""

while number > 0:
	 remainder = number % 10
	 divided_number = str(remainder) + " " + divided_number
	 number = number // 10

print(divided_number)