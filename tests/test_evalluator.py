from unittest import result, TestCase
import unittest

from EvaluatePosfix import *


class TestEvaluator(unittest.TestCase):
    def test_simple_add(self):
        e = EvaluatePostFix(['6', '3', '4', '*', '+', '2', '-'])

        result = e.evaluate_posfix()

        self.assertEqual(result, '16')

    def test_complex_expression(self):
        e = EvaluatePostFix(['46', '8', '4', '*', '2', '/', '+'])

        result = e.evaluate_posfix()

        self.assertEqual(result, '62')

    def test_complex_expression(self):
        e = EvaluatePostFix([
            '3',
        ])

        result = e.evaluate_posfix()

        self.assertEqual(result, '62')