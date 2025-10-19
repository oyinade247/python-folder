
from book_functions import suggest_book, add_book,remove_book,update_book,show_books


def menu(database):
	prompt =""" 
		WELCOME TO BOOK SUGGESTION SYSTEM
		
		1 => Get suggestion

		2 => Add book

		3 => Remove book

		4 => update book

		5 => show all book	


		"""
	print(prompt)
	main_menu = input("Enter operations: ")
	match main_menu :
		case "1" : 
			suggested = suggest_book(database)
			print(f"Book for the day:\n Book Title: {suggested}")
			page = database.index(suggested)
			print(f"page: {page}")
			
			suggestion = input("Would you like me to suggest another book? ")
			if suggestion == "yes":
				suggested = suggest_book(database)
				print(f"Book for the day:\n Book Title: {suggested}")
				page = database.index(suggested)
				print(f"page: {page}")
			
			else:
				menu(database)
				
			menu(database)

		case "2" : 
			
			book = input("Enter a book title:")
			
			added = add_book(database,book)
			print(f"book added successfully,{added}")
			menu(database)

		case "3" :
			book = input("Enter the book title to remove: ")
			removed = remove_book(database,book)
			print(f"Book removed successfully")
			menu(database)

		case "4" :
			old_book = input("Enter the odd title: ")
			new_book = input("Enter the new title: ")
			updated = update_book(database,old_book,new_book)

			print(f"Book updated successfully {updated}!")
			menu(database)
			

		case "5" :
			total = show_books(database)
			print(total)
			
			
				
			
	




def main():

	database = ["To Kill a Mockingbird", "1984", "Pride and Prejudice", "The Great Gatsby", "Moby-Dick", "War and Peace", "Jane Eyre", "Crime and Punishment", "The Catcher in the Rye", "The Lord of the Rings"]

	menu(database)






main()

	
	