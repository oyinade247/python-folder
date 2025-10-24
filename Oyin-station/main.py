from station_functions import sell_petrol,sell_diesel,sell_kerosene,sell_gas,show_total
def main_menu(liters, amount,database):
	prompt = """
		WELCOME TO OYINADE STATION
		1 => Buy petroleum
		
		2 => Show Transaction History


		""";
	print(prompt)
	main_menu = input("Enter operation: ")
	match main_menu:
		case "1" :petroleum(database)

		case "2" :transaction_history(database)

			
def petroleum(database):
	prompt = """
		AVAILABLE PETROLEUM

		1. petrol => 650/liter

		2. Diesel => 720/liter

		3. Kerosene => 550/liter

		4. Gas      => 480//liter

		""";
	print(prompt)
	petroleum = input("Press any key from 1 - 4: ")
	match petroleum:
		case "1" :
			liters = 0 
			amount = 0

			choice = input("Liter or amount: ").lower()
			if choice == "liter" :
				liters = int(input("How many liters of petrol are you buying: "))
			elif choice == "amount" :
				amount = int(input("How much petrol are you buying: "))
		
			total = sell_petrol(liters,amount,database)

			print(f"	CUSTOMER TRANSACTION RECEIPT\n 		=====================")
			print(f"	product:    {total[0]}\n	Amount:     {total [1] }\n 	liters:     {total[2]}L\n	Thank you for your patronage")
			

			main_menu(liters, amount,database)

		case "2" : 
			liters = 0 
			amount = 0

			choice = input("Liter or amount: ").lower()
			if choice == "liter" :
				liters = int(input("How many liters of disel are you buying: "))
			elif choice == "amount" :
				amount = int(input("How much disel are you buying: "))
			
			total = sell_diesel(liters,amount,database)

			print(f"	CUSTOMER TRANSACTION RECEIPT\n 		=====================")
			print(f"	product:    {total[0]}\n	Amount:     {total [1] }\n 	liters:     {total[2]}L\n	Thank you for your patronage")
			main_menu(liters, amount,database)



		case "3" :
			liters = 0 
			amount = 0

			choice = input("Liter or amount: ").lower()
			if choice == "liter" :
				liters = int(input("How many liters of kerosene are you buying: "))
			elif choice == "amount" :
				amount = int(input("How much kerosene are you buying: "))
			
			total = sell_kerosene(liters,amount,database)

			print(f"	CUSTOMER TRANSACTION RECEIPT\n 		=====================")
			print(f"	product:    {total[0]}\n	Amount:     {total [1] }\n 	liters:     {total[2]}L\n	Thank you for your patronage")
			main_menu(liters, amount,database)



		case "4" :
			liters = 0 
			amount = 0

			choice = input("Liter or amount: ").lower()
			if choice == "liter" :
				liters = int(input("How many liters of gas are you buying: "))
			elif choice == "amount" :
				amount = int(input("How much gas are you buying: "))
			total = sell_gas(liters,amount,database)

			print(f"	CUSTOMER TRANSACTION RECEIPT\n 		=====================")
			print(f"	product:    {total[0]}\n	Amount:     {total [1] }\n 	liters:     {total[2]}L\n	Thank you for your patronage")
			main_menu(liters, amount,database)



#def transaction_history(database):
	
			




			






def main():
	amount = 0
	liters = 0
	database = []
	main_menu(liters, amount,database)

main()		