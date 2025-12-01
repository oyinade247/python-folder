import unittest
from credit_card import *


class MyTestCase(unittest.TestCase):
    def test_that_reverse_user_digit_works_as_expected(self):
        number = "1234"
        actual = reverse_user_input(number)
        expected = [4, 3, 2, 1]
        self.assertEqual(actual, expected)

    def test_that_double_second_digit_works_as_expected(self):
        number = [4,3,2,1]
        actual = double_second_digit(number)
        expected = [8,4, 0]
        self.assertEqual(actual, expected)

    def test_that_sum_second_digit_works_as_expected(self):
        number = [8,4,0]
        actual = sum_second_digit(number)
        expected = 12
        self.assertEqual(actual, expected)