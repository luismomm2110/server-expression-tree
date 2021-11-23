import unittest
from unittest import result

from handle_get_expression import *


class TestValidExpression(unittest.TestCase):
    def test_with_only_numbers(self):
        c = CheckExpression("11")
        result = c._check_if_has_wrong_characters()
        self.assertTrue(result)

    def test_with_something_beside_numbers_and_operators(self):
        c = CheckExpression("a1a2+1)")
        result = c._check_if_has_wrong_characters()
        self.assertFalse(result)

    def test_if_ends_without_number_before_parenthesis(self):
        c = CheckExpression("1+(2+)")
        result = c._check_if_ends_with_number_or_number_and_open_parentheses()
        self.assertFalse(result)

    def test_if_not_ends_with_operator(self):
        c = CheckExpression("1+2*")
        result = c._check_if_ends_with_number_or_number_and_open_parentheses()
        self.assertFalse(result)

    def test_if_has_valid_start_with_parentheses(self):
        c = CheckExpression("(1+1)")
        result = c._check_if_with_starts_with_number_or_open_parenteses()
        self.assertTrue(result)

    def test_if_valid_start_with_number(self):
        c = CheckExpression("1/3")
        result = c._check_if_with_starts_with_number_or_open_parenteses()
        self.assertTrue(result)

    def test_if_has_wrong_start(self):
        c = CheckExpression("+1")
        result = c._check_if_with_starts_with_number_or_open_parenteses()
        self.assertFalse(result)

    def test_if_operators_in_sequence_are_invalid(self):
        c = CheckExpression("1++1")
        result = c._check_if_has_not_operators_in_sequence()
        self.assertFalse(result)

    def test_if_numbers_with_more_than_five_digits_are_invalid(self):
        c = CheckExpression("111111")
        result = c._check_if_has_only_number_with_five_digits()
        self.assertFalse(result)

    def test_if_numbers_with_more_than_five_digits_in_expression_are_invalid(
            self):
        c = CheckExpression("111111+11")
        result = c._check_if_has_only_number_with_five_digits()
        self.assertFalse(result)

    def test_if_five_digits_are_valid(self):
        c= CheckExpression("11111*55555")
        result = c._check_if_has_only_number_with_five_digits()
        self.assertTrue(result)
        
if __name__ == '__main__':
    unittest.main()