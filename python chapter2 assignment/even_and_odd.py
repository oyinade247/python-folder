#prompt user to enter a number

number = int(input("Enter any number: "))

#check if user input can be divided by 2 and the remainder becomes zero 
if(number %  2 == 0):
	print("Even")

#check if the user input can be divided by 2 and the remainder becomes one
elif(number % 2 == 1):
	print("Odd")
	