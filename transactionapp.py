def menu(amount, database):
	prompt = """
		WELCOME TO TRANSACTION LOG APP
		Press any key from 1 - 3:

		1 => Deposit
		
		2 => Withdraw

		3 => Transaction history

		4 => Balance

		5 => Exiting
		""";
	print(prompt)
	transaction_menu = input("Enter any key from 1- 4: ")
	match transaction_menu:
		case "1": deposit(amount, database)
		case "2": withdraw(amount, database)
		case "3": history(amount,database)
		case "4": balance(amount,database)
		case "5": print("Exiting...")
		case _ : 
			print("You entered wrong ")
			menu(amount,database)



def deposit(amount, database):
	print("DEPOSIT ANY AMOUNT")
	amount1 = int(input("Enter any amount to deposit: "))

	print(f"Deposited successfully, you deposited $ {amount1}")
	amount += amount1
	transaction = f"deposited ${amount1} | new Balance: ${amount}"
	database.append(transaction)

	print(f"Your new account balance is $ {amount}")
	menu(amount, database)


def withdraw(amount, database):
	print ("WITHDRAW  ANY AMOUNT")
	withdraw = int(input("Enter withdrawal amount:"))

	if withdraw > amount:
		print("insufficient funds")
		withdraw()

	print(f"Debited successfully, you withdrew ${withdraw}")
	amount -= withdraw
	print(f"Your new account balance is $ {amount}.")
	transaction = f"withdraw ${withdraw} | new balance : ${amount}"
	database.append(transaction)
	menu(amount, database)



def history(amount, database):
	print("TRANSACTION HISTORY")
	for history in database:
		print(history)
	menu(amount, database)



def balance(amount,database):
	if amount == 0:
		print("You have $0 in your account")
	print(f"your remaining balance is ${amount}")
	menu(amount,database)



def main():
	amount = 0
	database = []
	menu(amount, database)



	





main()