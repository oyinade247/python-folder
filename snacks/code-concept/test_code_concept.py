from unittest import TestCase
from code_concept_functions import create_tuple

class TestMyFunctions(TestCase):
	def test_that_create_tuple_functions_work_as_expected(self):
		numbers = (1,2,3)
		added_number = (4,)
		actual = create_tuple(numbers, added_number)
		expected = (1,2,3,4)
		self.assertEqual(actual, expected)



	