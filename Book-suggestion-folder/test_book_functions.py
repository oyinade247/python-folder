from unittest import TestCase
from book_functions import suggest_book,add_book,remove_book,update_book,show_books
	

class TestBookFunctions(TestCase):
	def test_that_suggest_book_function_works_as_expected(self):
		booklist = ["semicolon is good"]
		actual = suggest_book(booklist)
		expected =  "semicolon is good"
		self.assertEqual(actual, expected)

	def test_that_sugggest_book_returns_only_one_book(self):
		booklist = ["semicolon is good"]
		actual = suggest_book(booklist)
		expected = "semicolon is good"
		self.assertEqual(actual, expected)

	def test_that_you_can_add_a_book(self):
		booklist = ["semicolon is good"]
		book = "Oyin is a babe"
		actual = add_book(booklist,book)
		expected = ["semicolon is good", "oyin is a babe"]
		self.assertEqual(actual, expected)

	def test_that_book_can_be_added_in_any_case_character(self):
		booklist = []
		book = "OyIN Is a bAbE"
		actual = add_book(booklist,book)
		expected = ["oyin is a babe"]
		self.assertEqual(actual, expected)


	def test_that_add_book_function_does_not_add_existing_book(self):
		self.assertRaises(ValueError , add_book, ["semicolon is good"], "semicolon is good")


	def test_that_remove_book_function_work_as_expected(self):
		booklist = ["semicolon is good"]
		book = "semicolon is good"
		actual =  remove_book(booklist,book)
		expected = []
		self.assertEqual(actual, expected)

	def test_that_book_can_be_removed_in_any_case_character(self):
		booklist = ["semicolon is good"]
		book = "seMicOlon is gOOd"
		actual =  remove_book(booklist,book)
		expected = []
		self.assertEqual(actual, expected)

	def test_that_you_can_not_remove_book_that_does_not_exist(self):
		self.assertRaises(ValueError,remove_book, ["oyin"],"oyinaad3")


		
	def test_update_book_function_works_as_expected(self):
		booklist = ["semicolon is good"]
		old_book = "semicolon is good"
		new_book = "I am able"
		actual = update_book(booklist,old_book,new_book)
		expected = ["i am able"]
		self.assertEqual(actual, expected)

	def test_that_book_can_be_updated_in_any_case_character(self):
		booklist = ["semicolon is good"]
		old_book = "semiCOlon is goOd"
		new_book = "I aM abLe"
		actual = update_book(booklist,old_book,new_book)
		expected = ["i am able"]
		self.assertEqual(actual, expected)


	def test_that_book_cannot_be_updated_if_they_do_not_exist(self):
		self.assertRaises(ValueError,update_book, [],"oyin","oyinaade")


	def test_that_show_book_work_as_expected(self):
		booklist = ["semicolon is good"]
		actual = show_books(booklist)
		expected = ["semicolon is good"]
		self.assertEqual(actual, expected)

		

		
		

		

		
		


	









		


		
		
		
		

	
		