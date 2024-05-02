import unittest
from calc import addition, subtraction, multiplication, division, getEvenOrOddStatus, getPositiveorNegativeStatus

class TestCalc(unittest.TestCase):

    def test_add(self):
        expected = addition(10, 20)
        self.assertEqual(expected, 30)

    def test_sub(self):
        expected = subtraction(20, 10)
        self.assertEqual(expected, 10)
        expected = subtraction(-10, 10)
        self.assertEqual(expected, -20)


    def test_multiply(self):
        expected = multiplication(7,8)
        self.assertEqual(expected, 56)

    def test_div(self):
        expected = division(20,10)
        self.assertEqual(expected, 2)
        expected = division(10,20)
        self.assertEqual(expected,0)

    
    def test_even_odd(self):
        expected = getEvenOrOddStatus(7)
        self.assertEqual(expected, "Odd")
        expected = getEvenOrOddStatus(8)
        self.assertEqual(expected, "Even")
    
    def test_even_odd(self):
        expected = getPositiveorNegativeStatus(7)
        self.assertEqual(expected, "Positive")
        expected = getPositiveorNegativeStatus(-8)
        self.assertEqual(expected, "Negative")
        expected = getPositiveorNegativeStatus(0)
        self.assertEqual(expected, "Positive")