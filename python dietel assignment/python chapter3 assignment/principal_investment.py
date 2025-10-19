PRINCIPAL = 1000

INVESTMENT_RETURN = 0.07

years = 1

amount = 0

while(years <= 30):
	
	amount += PRINCIPAL * ((1 + INVESTMENT_RETURN) ** years)
	years += 1

	print("in year",years,"your investment has inreased to", amount)
	