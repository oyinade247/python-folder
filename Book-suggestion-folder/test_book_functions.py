from unittest import TestCase
from book_functions import suggest_book
	

class TestBookFunctions(TestCase):
	def test_that_suggest_book_is_returning_one_book(self):
		actual = suggest_book(["1984"])
		expected = "1984"
		self.assertEqual(actual,expected)