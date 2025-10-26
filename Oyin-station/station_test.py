from unittest import TestCase
from station_functions import sell_petrol,sell_diesel,sell_kerosene,sell_gas

class TestMyFunctions(TestCase):
	def test_that_sell_petrol_liters_works_as_expected(self):
		liters = 2
		amount =  0
		actual = sell_petrol(liters,amount ,[])
		expected = ["petrol", 1300, 2]
		self.assertEqual(actual,expected)

	def test_that_sell_petrol_amount_works_as_expected(self):
		liters = 0
		amount = 1300
		database = []
		actual = sell_petrol(liters,amount ,[])
		expected = ["petrol", 1300, 2]
		self.assertEqual(actual,expected)


	def test_that_you_cannot_enter_liters_in_any_other_case(self):
		self.assertRaises(TypeError,sell_petrol,"awee", "wewe", [])		


	def test_that_sell_disel_liters_works_as_expected(self):
		liters = 2
		amount =  0
		actual = sell_diesel(liters,amount ,[])
		expected = ["diesel", 1440, 2]
		self.assertEqual(actual,expected)


	def test_that_sell_disel_amount_works_as_expected(self):
		liters = 0
		amount =  1440
		actual = sell_diesel(liters,amount ,[])
		expected = ["diesel", 1440, 2]
		self.assertEqual(actual,expected)


	def test_that_you_cannot_enter_liter_and_amount_in_any_other_case(self):
		self.assertRaises(TypeError,sell_diesel,"awee", "wewe", [])


	def test_that_sell_kerosene_liters_works_as_expected(self):
		liters = 2
		amount =  0
		actual = sell_kerosene(liters,amount ,[])
		expected = ["kerosene", 1100, 2]
		self.assertEqual(actual,expected)


	def test_that_sell_kerosene_amount_works_as_expected(self):
		liters = 0
		amount =  1100
		actual = sell_kerosene(liters,amount ,[])
		expected = ["kerosene", 1100, 2]
		self.assertEqual(actual,expected)

	
	def test_that_you_cannot_enter_liter_and_amount_test_in_any_other_case(self):
		self.assertRaises(TypeError,sell_kerosene,"awee", "wewe", [])


	def test_that_sell_gas_liters_works_as_expected(self):
		liters = 2
		amount =  0
		actual = sell_gas(liters,amount ,[])
		expected = ["gas", 960, 2]
		self.assertEqual(actual,expected)

	def test_that_sell_gas_amount_works_as_expected(self):
		liters = 0
		amount =  960
		actual = sell_gas(liters,amount ,[])
		expected = ["gas", 960, 2]
		self.assertEqual(actual,expected)









