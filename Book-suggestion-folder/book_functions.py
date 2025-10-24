import random
def suggest_book(database):
	index = random.randint(0, 0)
	book_suggestion = database[index]
	return book_suggestion

		
def add_book(database, book):
	if book not in database:
		database.append(book)
	else:
		raise ValueError("Book does not exist")		
	return database


def remove_book(database,book):
	if book not in database:
		raise ValueError("Book is not in list")	
	database.remove(book)
	return database

def update_book(database,old_book,new_book):
	replace =  database.index(old_book)
	database[replace] = new_book
	return database

	
def show_books(database):
	return database
	