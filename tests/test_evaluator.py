from unittest import result, TestCase
import unittest

from EvaluatePosfix import *


class TestEvaluator(unittest.TestCase):
    def test_simple_add(self):
        e = EvaluatePostFix(['2', '14', '+'])

        result = e.evaluate_posfix()

        self.assertEqual(result, '16.0')

    def test_complex_expression(self):
        e = EvaluatePostFix(['46', '8', '4', '*', '2', '/', '+'])

        result = e.evaluate_posfix()
        self.assertEqual(result, '62.0')

    def test_with_float(self):
        e = EvaluatePostFix(['2.3', '2', '+'])
        result = e.evaluate_posfix()

        self.assertEqual(result, '4.3')
