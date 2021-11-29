import unittest
from unittest import result, TestCase

from CheckInput import *


class CheckInputTest(TestCase):
    def test_if_numbers_with_more_than_five_digits_in_input_are_invalid(self):
        c = CheckExpression("111111+11")
        result = c.check_if_has_number_too_long()
        self.assertTrue(result)

    def test_if_has_only_parentheses(self):
        c = CheckExpression("((1+1)) + 2")
        result = c.check_if_has_more_than_single_parentheses()
        self.assertTrue(result)