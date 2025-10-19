def print_main_menu():
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
	match transaction_menu :
		case "1": deposit()	
			
		case "2": withdraw()

		case "3": history()
						
			
		case "4": balance()

		case "5" : print("Exiting")

		case _ : 
			print("you entered wrong! enter the correct number")
			print_main_menu()


def deposit(amount, account, transaction = []):
	print("DEPOSIT ANY AMOUNT")
	amount1 = int(input("Enter any amount to deposit: "))

	print(f"Deposited successfully, you deposited $ {amount1}")
	amount += amount1
	transaction = f"deposited ${amount1} | new Balance: ${amount}"
	transaction_database.append(transaction)

	print(f"Your new account balance is $ {amount}")
	print_main_menu()




def withdraw(amount, account_balance,transaction = []):
	print ("WITHDRAW  ANY AMOUNT")
	withdraw = int(input("Enter withdrawal amount:"))

	if withdraw > amount:
		print("insufficient funds")
		withdraw()

	print(f"Debited successfully, you withdew ${withdraw}")
	amount -= withdraw
	print(f"Your new account balance is $ {amount}.")
	transaction = f"withdraw ${withdraw} | new balance : ${amount}"
	transaction_database.append(transaction)

	print_main_menu()


def history(transaction = []):
	global transaction_database
	print("TRANSACTION HISTORY")
	for history in transaction_database:
		print(history)
	print_main_menu()



def balance(amount):
	if balance == 0:
		print("You have $0 in your account")
	print (f"your remaining balance is ${amount}")
	print_main_menu()
	
	














print_main_menu()

