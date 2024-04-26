import unittest
from calc import addition

class TestCalc(unittest.TestCase):

    def test_add(self):
        expected = addition(10, 20)
        self.assertEqual(expected, 30) 