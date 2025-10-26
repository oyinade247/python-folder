import random
def suggest_book(database):
	index = random.randint(0, 0)
	book_suggestion = database[index]
	return book_suggestion

		
def add_book(database, book):
	if book in database:
		raise ValueError("Book does not exist")		
	database.append(book.lower())	
	return database


def remove_book(database,book):
	if book.lower() not in database:
		raise ValueError("Book is not in list")	
	database.remove(book.lower())
	return database

def update_book(database,old_book,new_book):
	if old_book.lower() not in database:
		raise ValueError("Book is not in the list")
	replace =  database.index(old_book.lower())
	database[replace] = new_book.lower()
	return database

	
def show_books(database):
	return database
	

#print(remove_book(["oyin"], "OyIn") == [])