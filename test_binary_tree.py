from unittest import result, TestCase
import unittest

from BinaryTree import *


class TestBinaryTree(unittest.TestCase):
    def test_single_number(self):
        result = BinaryTree.create_tree_from_tokens(["32"])

        self.assertEqual(result.value, "32")