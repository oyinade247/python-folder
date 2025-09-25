#prompt user to enter a number
#check if user input can be divided by 2 and the remainder becomes zero 
#check if the user input can be divided by 2 and the remainder becomes one
#display the result


number = int(input("Enter any number: "))

if(number %  2 == 0):
	print("Even")

elif(number % 2 == 1):
	print("Odd")
	