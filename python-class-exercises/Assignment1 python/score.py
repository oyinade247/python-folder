#prompt user to enter their score
# collect user score
#Check if the user score is greater than 90 or equals to 90 and give the result as A
#Check again if the user score is greater than 80 and less than or equals  to 89 and give the result as B
#Check again if the user score is greater than 70 and less than or equals  to 79 and give the result as C
#Check again if the user score is greater than 60 and less than or equals  to 69 and give the result as D
# else output F



count = 1
total = 0

while(count <= 3):
	score = int(input("Enter your score: "))
	count += 1

	total += score

average = total // 3

print("The average score is",average) 


if(total >= 90):
	 print("Your grade is","A")
	
elif(total >= 80 and total <= 89):
	 print("Your grade is","B")
	
elif(total >= 70 and total <= 79):
	 print("Your grade is","C")
	
elif(total >= 60 and total <= 69):
 	print("Your grade is","D")
	

else:
	print("Your grade is","F")

