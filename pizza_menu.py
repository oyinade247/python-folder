def print_pizza_menu():
	prompt = """ 
		


		_______________________________________________________________________
		
		|   PIZZA TYPE 		| 	NUMBER OF SLICES 	| PRICE PER BOX|
		________________________________________________________________________
		
		|   SAPA SIZE		|	4			|	2500	|
		________________________________________________________________________

		| 	SMALL MONEY	|        6			|	2900	|
	        _________________________________________________________________________

		|  BIG BOYS 		|	8			|	4000	|
		 _________________________________________________________________________
		
		|	ODOGWU		|	12			|	5200	|
		________________________________________________________________________










			PIZZA TYPE MENU

			1 -> Sapa size (4 slices) for 2500
			
			2 -> Small money (6 slices) for 2900

			3 -> Big boys (8 slices) for 4000

			4 -> Odogwu (12 slices) for 5200
			
			5 -> Exit


		""";
	print(prompt);
	pizza = input("Enter pizza type whimps:")
	match pizza :
		case "1" : print_sapa_size()
		case "2" : print_small_money()
		case "3" : print_big_boy()
		case "4" : print_odogwu()
		case "5" : print("Existing")
		case _ :	
			print("You entered wrong");
			print_pizza_menu()


def print_sapa_size():
	print(""" WELCOME TO SAPA SIZE TYPE

	NUMBER OF SLICES -> 4
	PRICES PER BOX   -> 2500

	""")

	guest = input("How many guest are coming for your party: ")
	number_guest = int(guest)

	if number_guest < 4 :
		print("you entered wrong, it is less than the required slice!")
		print_sapa_size()
		
		

	box1 = number_guest / 4

	if box1 % number_guest != 0 :
		box1 = box1 +  1
		
		 
	left_over =  (box1 * 4)- number_guest
	price = 2500 * box1
		
	print(f'The number of boxes of pizza to buy is {box1}')
	print(f'The number of leftover slices after serving is {left_over}')
	print(f'The amount of boxes of pizza to buy is {price}');

		
	sapa_size = input("Press 0 to go back to Pizza menu: ")
	match sapa_size :
		case "0" : print_pizza_menu();
		case _ : 
			print("You entered wrong")
			print_sapa_size()



def print_small_money():
	prompt = """
	NUMBER OF SLICES -> 6
	PRICES PER BOX -> 2900
	""";

	print(prompt);

	guest = input("How many guest are you inviting ? ")
	
	number_guest = int(guest)

	if number_guest < 6 :
		print("you entered wrong, it is less than the requirement!")
		print_small_money()

	box1 = number_guest // 6

	if box1 % number_guest != 0 :
		box1 = box1 +  1
		
		 
	left_over =  (box1 * 6)- number_guest 
	price = 2900 * box1
	
	print(f'The number of boxes of pizza to buy is {box1}')
	print(f'The number of leftover slices after serving is {left_over}')
	print(f'The amount of boxes of pizza to buy is {price}');

	small_money = input("Press 0 to go back to Pizza menu: ")
	match small_money :
		case "0" : print_pizza_menu();
		case _ : 
			print("You entered wrong")
			print_small_money()

	


	

def print_big_boy():
	prompt = """
	NUMBER OF SLICES -> 8
	PRICES PER BOX -> 4000
	""";

	print(prompt);

	guest = input("How many guest are you inviting? ")
	number_guest = int(guest)

	if number_guest < 8 :
		print("you entered wrong, it is less than the requirement!")
		print_big_boy()

	box1 = number_guest // 8

	if box1 % number_guest != 0 :
			box1 = box1 +  1
		
		 
	leftOver =  (box1 * 8) - number_guest 
	price = 4000 * box1;
		
		
	print(f'The number of boxes of pizza to buy is {box1}')
	print(f'The number of leftover slices after serving is {left_over}')
	print(f'The amount of boxes of pizza to buy is {price}');

	big_boys = input("Press 0 to go back to Pizza menu: ")
	match big_boys :
		case "0" :  printPizzaType();
		case _ :
			print("You entered wrong")
			printSapaSize()


   



def print_odogwu():
	prompt = """
		NUMBER OF SLICES -> 12
		PRICES PER BOX -> 5200
	""";


	print(prompt);
	guest = input("How many guest are you inviting? ")
	number_guest = int(guest)
	
	if number_guest < 12 :
		print("you entered wrong, it is less than the requirement!")
		print_odogwu()



	box1 = number_guest / 12
	if box1 % number_guest != 0 :
		box1 = box1 +  1
		
		 
	leftOver =  (box1 * 12)- number_guest 
	price = 5200 * box1
		
	print(f'The number of boxes of pizza to buy is {box1}')
	print(f'The number of leftover slices after serving is {left_over}')
	print(f'The amount of boxes of pizza to buy is {price}');

	odogwu = input("Press 0 to go back to Pizza menu: "); 	
	match odogwu :
			case "0" : printPizzaType(); 
			case _ :
				print("You entered wrong")
				printOdogwu()



	


	
	












print_pizza_menu()


