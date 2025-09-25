#prompt user to enter five digits
#create a box to store each of the number
#divide the number by 10 to extract the remainder and the save it to the box you want store the numbers into. Divide the number by 10 again until it turns zero



number = int(input("Enter five digits: "))
remainder = ""


divided_number = number % 10
remainder = str(divided_number) + " " + remainder 
number = number // 10


divided_number = number % 10
remainder = str(divided_number) + " " + remainder
number = number // 10

divided_number = number % 10
remainder = str(divided_number) + " " + remainder
number = number // 10

divided_number = number % 10
remainder = str(divided_number) + " " + remainder
number = number // 10

print(remainder)










