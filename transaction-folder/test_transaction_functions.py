from unittest import TestCase
from transaction_functions import deposit,withdraw, show_transactions

class TestTransactionFunctions(TestCase):

	
	def test_that_deposit_function_will_return_updated_balance(self):
		actual = deposit(1000,200,[])
		expected = 1200
		self.assertEqual(actual,expected)

	def test_that_withdraw_function_will_work_as_expected(self):
		actual = withdraw(200, 1000, [])
		expected = 800
		self.assertEqual(actual, expected)

	def test_that_withdraw_will_not_work_with_amount_greater_than_balance(self):
		self.assertRaises(ValueError, withdraw, 1000, 200, [])

	
	def test_that_show_transaction_function_will_return_list_transaction_records(self):
		actual = show_transactions([])
		expected = "No transaction yet"
		self.assertEqual(actual, expected)
		actual = show_transactions(["i am a boy"])
		expected = ["i am a boy"]
		self.assertEqual(actual, expected)


