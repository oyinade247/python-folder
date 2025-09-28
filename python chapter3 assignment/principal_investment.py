principal = 1000

investment_return = 0.07

years = 1

amount = 0

while(years <= 30):
	
	amount += principal * ((1 + investment_return) * years)
	years += 1

	print("in year",years,"your investment has inreased to", amount)
	