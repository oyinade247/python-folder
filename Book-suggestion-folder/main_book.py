
from book_functions import suggest_book, add_book,remove_book,update_book,show_books


def menu(database):
	prompt =""" 
		WELCOME TO BOOK SUGGESTION SYSTEM
		
		1 => Get suggestion

		2 => Add book

		3 => Remove book

		4 => update book

		5 => show all book

		6 => exit	


		"""
	print(prompt)
	main_menu = input("Enter operations: ")
	match main_menu :
		case "1" : 
			suggested = suggest_book(database)
			print(f"Book for the day:\n Book Title: {suggested}")
			page = database.index(suggested)
			print(f"page: {page}")
			
			suggestion = input("Would you like me to suggest another book? ").lower()
			if suggestion == "yes":
				suggested = suggest_book(database)
				print(f"Book for the day:\n Book Title: {suggested}")
				page = database.index(suggested)
				print(f"page: {page}")
			
			else:
				menu(database)
				
			menu(database)

		case "2" : 
			
			book = input("Enter a book title:").lower()
			
			database = add_book(database,book)
					
			print(f"book added successfully")
			for index, book in enumerate(database):
				print(f"{index} {book}")
				
			menu(database)

		case "3" :
			book = input("Enter the book title to remove: ").lower()
			removed = remove_book(database,book)
			print(f"Book removed successfully")
			menu(database)

		case "4" :
			old_book = input("Enter the odd title: ").lower()
			new_book = input("Enter the new title: ").lower()
			updated = update_book(database,old_book,new_book)

			print(f"Book updated successfully!")
			for index, book in enumerate(database):
				print(f"{index} {book}")
			menu(database)
			

		case "5" :
			total = show_books(database)
			for index, book in enumerate(total):
				print(f"{index} {book}")
			menu(database)

		case "6" : print("See you another day")

			
			
				
			
	




def main():

	database = ["to kill a mockingbird", "1984", "pride and prejudice", "the great gatsby", "moby-dick", "war and peace", "jane eyre", "crime and punishment", "the catcher in the rye", "the lord of the rings"]

	menu(database)






main()

	
	