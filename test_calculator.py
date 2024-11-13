import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

    def test_add(self):
        self.assertEqual(self.calc.add(3, 2), 5)

    def test_add2(self):
        self.assertEqual(self.calc.add(-1, 5), 4)
    
    def test_subtract(self):
        self.assertEqual(self.calc.subtract(5, 2), 3) 

    def test_subtract2(self):
        self.assertEqual(self.calc.subtract(10, 5), 5)

    def test_multiply(self):
        self.assertEqual(self.calc.multiply(3, 4), 12)

    def test_multiply2(self):
        self.assertEqual(self.calc.multiply(0, 7), 0) 

    def test_divide(self):
        self.assertEqual(self.calc.divide(8, 2), 4)

    def test_divide2(self):
        self.assertEqual(self.calc.divide(6, 2), 3)

    def test_modulo(self):
        self.assertEqual(self.calc.modulo(10, 3), 1)
    
    def test_modulo2(self):
        self.assertEqual(self.calc.modulo(8, 4), 0)

if __name__ == '__main__':
    unittest.main()