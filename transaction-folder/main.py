from transaction_functions import deposit, withdraw, show_transactions


def menu(account_balance, database):
	prompt = """
		WELCOME TO TRANSACTION LOG APP
		Press any key from 1 - 3:

		1 => Deposit
		
		2 => Withdraw

		3 => Transaction history

		4 => Exit
		""";
	print(prompt)
	transaction_menu = input("Enter any key from 1- 4: ")
	match transaction_menu:
		case "1":
			amount = float(input("Enter deposit amount: "))
			account_balance = deposit(amount, account_balance, database)
			menu(account_balance, database)
		case "2":
			amount = float(input("Enter withdrawal amount: "))
			account_balance = withdraw(amount, account_balance, database)
			menu(account_balance, database)
		case "3":
			transactions = show_transactions(database)
			for transaction in transactions:
				print(transaction)
			menu(account_balance, database)
		case "4":
			print(f"Final balance: {account_balance}")
			print("Thank you for using Transaction log app.")
			
			

		


def main():
	account_balance = 0
	database = []
	menu(account_balance, database)


main()