from unittest import TestCase
from book_functions import suggest_book,add_book,remove_book,update_book,show_books
	

class TestBookFunctions(TestCase):
	def test_that_suggest_book_is_returning_one_book(self):
		actual = suggest_book(["1984"])
		expected = "1984"
		self.assertEqual(actual,expected)

	def test_that_add_book_functions_is_adding_only_one_item(self):
		actual = add_book([],"Oyin")
		expected = ["Oyin"]
		self.assertEqual(actual, expected)

	def test_that_add_book_function_is_not_adding_existing_book(self):
		print("successfully ran add book function")
		actual = add_book(["1984"], "1984")
		
		expected = ["1984"]
		self.assertRaises(ValueError, actual, expected)

	def test_that_remove_book_function_has_been_removed(self):
		self.assertRaises(ValueError,remove_book, ["2"], "book")
		