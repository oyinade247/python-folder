gallon = 0

sum_gallon = 0

sum_miles = 0

while(gallon != -1 ):
	gallon = int(input("Enter the gallons used(-1 to end):"))
	sum_gallon += gallon

	miles = int(input("Enter the miles driven: "))
	sum_miles +=miles

	each_trip = miles / gallon
	print("The miles per gallon for each trip is", each_trip)

	if(gallon == -1):
		total_trip = sum_gallon / sum_miles 
		print("The total miles per gallon for each trip is", total_trip)










	