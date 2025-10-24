def sell_petrol(liters,amount,database):
	if liters:
		amount = liters * 650
	if amount:
		liters = amount // 650
	transaction = ["petrol", amount, liters]
	database.append(transaction)
	return transaction

def sell_diesel(liters,amount,database):
	if liters:
		amount =amount = liters * 720
	if amount:
		liters = amount // 720
	transaction = ["disel", amount, liters]
	database.append(transaction)
	return transaction

def sell_kerosene(liters,amount,database):
	if liters:
		amount =amount = liters * 550
	if amount:
		liters = amount // 550
	transaction = ["kerosene", amount, liters]
	database.append(transaction)
	return transaction

def sell_gas(liters,amount,database):
	if liters:
		amount =amount = liters * 480
	if amount:
		liters = amount // 480
	transaction = ["gas", amount, liters]
	database.append(transaction)
	return transaction

def show_total(database):
	return database




	
		
	
	
	