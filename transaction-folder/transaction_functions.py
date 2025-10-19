def deposit(amount, account_balance, database):
	account_balance += amount
	transaction = f"Deposited: {amount} | New balance : {account_balance}"
	database.append(transaction)
	return account_balance


def withdraw(amount, account_balance, database):
	if amount > account_balance:
		raise ValueError("insufficient funds")

	account_balance -= amount
	
	transaction = f"Withdrew: {amount} | New balance : {account_balance}"
	database.append(transaction)
	return account_balance

def show_transactions(database):
	if len(database) == 0:
		return "No transaction yet"
	return database

	