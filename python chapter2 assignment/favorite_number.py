#create a variable to save a secret number
#prompt user to guess the secret number
#check if the user guess the number correctly or not and display the output


favorite_number = 7


guess = int(input("Guess a number (1-10): " ))

if(guess == favorite_number):
	print("That's my favorite number")

else:
	print("Nice try,guess again!")