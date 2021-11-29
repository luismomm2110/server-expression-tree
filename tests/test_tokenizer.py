from unittest import result, TestCase
import unittest

from Tokenizer import *


class TestTokenizer(unittest.TestCase):
    def test_single_number(self):
        result = token_expressions("32")

        self.assertListEqual(result, ["32"])

    def test_simple_add(self):
        result = token_expressions("3+1")

        self.assertListEqual(result, ['3', '+', '1'])

    def test_add_two_digits(self):
        result = token_expressions("31+1")

        self.assertListEqual(result, ['31', '+', '1'])

    def test_with_three_operators(self):
        result = token_expressions("21/2+4*2")

        self.assertListEqual(result, ['21', '/', '2', '+', '4', '*', '2'])

    def test_with_middle_parentheses(self):
        result = token_expressions("1+(1+22)+2")

        self.assertListEqual(result,
                             ['1', '+', '(', '1', '+', '22', ')', '+', '2'])

    def test_with_parentheses_in_start(self):
        result = token_expressions("(1+2)+3")

        self.assertListEqual(result, ['(', '1', '+', '2', ')', '+', '3'])

    def test_with_parentheses_in_end(self):
        result = token_expressions("1+(3+2)")

        self.assertListEqual(result, ['1', '+', '(', '3', '+', '2', ')'])

    def test_float_number(self):
        result = token_expressions("2+3.1")

        self.assertListEqual(result, ['2', '+', '3.1'])