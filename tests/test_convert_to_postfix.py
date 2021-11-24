import unittest
from unittest import result, TestCase

from convertToPostFix import *


class ConvertToPostfixTest(TestCase):
    def test_simple_add(self):
        c = ConvertorToPostfix(['1', '+', '1'])
        result = c.translate_infix_to_postfix()

        self.assertListEqual(result, ['1', '1', '+'])
