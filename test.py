import unittest
from calc import addition, substraction, division

class TestCalc(unittest.TestCase):

    def test_add(self):
        expected = addition(10, 20)
        self.assertEqual(expected, 30)

    def test_sub(self):
        expected = substraction(20, 10)
        self.assertEqual(expected, 10)
        expected = substraction(-10, 10)
        self.assertEqual(expected, -20)

    def test_div(self):
        expected = division(20,10)
        self.assertEqual(expected, 2)
        expected = division(10,20)
        self.assertEqua(expected,0)

