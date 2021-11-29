import unittest
from unittest import result, TestCase

from convertToPostFix import *


class ConvertToPosfix(TestCase):
    def test_simple_add(self):
        c = ConvertorToPosfix(['1', '+', '1'])
        result = c.translate_infix_to_posfix()

        self.assertListEqual(result, ['1', '1', '+'])

    def test_double_digits_add(self):
        c = ConvertorToPosfix(['32', '+', '1'])
        result = c.translate_infix_to_posfix()

        self.assertListEqual(result, ['32', '1', '+'])

    def test_multplication(self):
        c = ConvertorToPosfix(['8', '-', '2', '*', '3'])
        result = c.translate_infix_to_posfix()

        self.assertListEqual(result, ['8', '2', '3', '*', '-'])

    def test_with_parentheses(self):
        c = ConvertorToPosfix(['(', '1', '-', '2', ')', '*', '3'])
        result = c.translate_infix_to_posfix()

        self.assertListEqual(result, ['1', '2', '-', '3', '*'])

    def test_with_float_number(self):
        c = ConvertorToPosfix(['1', '+', '3.2'])
        result = c.translate_infix_to_posfix()

        self.assertListEqual(result, ['1', '3.2', '+'])

    def test_with_negative_start(self):
        c = ConvertorToPosfix(['-', '1042', '+', '1'])
        result = c.translate_infix_to_posfix()
        
        self.assertListEqual(result, ["-1042", "1", "+"])

    def test_with_negative_after_operator(self):
        c = ConvertorToPosfix(["3", "*", "-", "2"])
        result = c.translate_infix_to_posfix()
        
        self.assertListEqual(result, ["3", "-2", "*"])