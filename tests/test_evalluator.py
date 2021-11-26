from unittest import result, TestCase
import unittest

from EvaluatePosfix import *

class TestEvaluator(unittest.TestCase):
	def test_simple_add(self):
		e = EvaluatePostFix()
		
		result = e.evaluate_posfix(['6', '3', '4', '*', '+', '2', '-'])

		self.assertEqual(result, '16')