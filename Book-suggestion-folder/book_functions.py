import random
def suggest_book(database):
	index = random.randint(0, 9)
	book_suggestion = database[index]
	return book_suggestion
		
def add_book(database, book):
	database.append(book)
	return database

def remove_book(database,book):
	database.remove(book)
	return database

def update_book(database,old_book,new_book):
	replace =  database.index(old_book)
	database[replace] = new_book
	return database
	
def show_books(database):
	for book in database:
		return database