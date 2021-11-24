import unittest
from unittest import result, TestCase

from convertToPostFix import *


class ConvertToPostfixTest(TestCase):
    def test_simple_add(self):
        c = ConvertorToPostfix()
        result = c.translate_infix_to_postfix(['1', '+', '1'])

        self.assertListEqual(result, ['1', '1', '+'])
