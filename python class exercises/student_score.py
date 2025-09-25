student_score_one = int(input("Enter a number: "))

student_score_two = int(input("Enter a number : "))

student_score_three = int(input("Enter a number: "))

largest_two = student_score_one

if(largest_two < student_score_two):
	largest_two = student_score_two

if(largest_two > student_score_three):
	largest_two = student_score_three

print("The largest student score is ", largest_two)




