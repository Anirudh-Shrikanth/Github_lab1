import sys
import os
import unittest

# Get the path to the project's root directory
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(project_root)

from src import calculator


class TestCalculator(unittest.TestCase):

    def test_fun1(self):
        self.assertEqual(calculator.fun1(2, 3), 5)
        self.assertEqual(calculator.fun1(5, 0), 5)
        
        self.assertEqual(calculator.fun1(-1, 1), 0)
        self.assertEqual(calculator.fun1(-1, -1), -2)

    def test_fun2(self):
        self.assertEqual(calculator.fun2(2, 3), -1)
        self.assertEqual(calculator.fun2(5, 0), 5)
        self.assertEqual(calculator.fun2(-1, 1), -2)
        self.assertEqual(calculator.fun2(-1, -1), 0)

    def test_fun3(self):
        self.assertEqual(calculator.fun3(2, 3), 6)
        self.assertEqual(calculator.fun3(5, 0), 0)
        self.assertEqual(calculator.fun3(-1, 1), -1)
        self.assertEqual(calculator.fun3(-1, -1), 1)

    def test_fun4(self):
        self.assertEqual(calculator.fun4(2, 3, 5), 10)
        self.assertEqual(calculator.fun4(5, 0, -1), 4)
        self.assertEqual(calculator.fun4(-1, -1, -1), -3)
        self.assertEqual(calculator.fun4(-1, -1, 100), 98)

    def test_fun5(self):
        # Basic division tests
        self.assertEqual(calculator.fun5(6, 2), 3.0)
        self.assertEqual(calculator.fun5(10, 4), 2.5)
        self.assertEqual(calculator.fun5(-8, 2), -4.0)
        self.assertEqual(calculator.fun5(8, -2), -4.0)
        self.assertEqual(calculator.fun5(-8, -2), 4.0)
        self.assertEqual(calculator.fun5(0, 5), 0.0)
        
        # Test division by zero raises exception
        with self.assertRaises(ZeroDivisionError):
            calculator.fun5(5, 0)
        
        # Test invalid input types
        with self.assertRaises(ValueError):
            calculator.fun5("5", 2)
        with self.assertRaises(ValueError):
            calculator.fun5(5, "2")

    def test_fun6(self):
        # Basic power tests
        self.assertEqual(calculator.fun6(2, 3), 8)
        self.assertEqual(calculator.fun6(5, 2), 25)
        self.assertEqual(calculator.fun6(3, 0), 1)
        self.assertEqual(calculator.fun6(4, 0.5), 2.0)
        self.assertEqual(calculator.fun6(-2, 3), -8)
        self.assertEqual(calculator.fun6(-2, 2), 4)
        self.assertEqual(calculator.fun6(10, -1), 0.1)
        
        # Test invalid input types
        with self.assertRaises(ValueError):
            calculator.fun6("2", 3)
        with self.assertRaises(ValueError):
            calculator.fun6(2, "3")

    def test_fun7(self):
        # Basic modulo tests
        self.assertEqual(calculator.fun7(10, 3), 1)
        self.assertEqual(calculator.fun7(15, 4), 3)
        self.assertEqual(calculator.fun7(20, 5), 0)
        self.assertEqual(calculator.fun7(-7, 3), 2)
        self.assertEqual(calculator.fun7(7, -3), -2)
        self.assertEqual(calculator.fun7(-7, -3), -1)
        
        # Test modulo by zero raises exception
        with self.assertRaises(ZeroDivisionError):
            calculator.fun7(10, 0)
        
        # Test invalid input types
        with self.assertRaises(ValueError):
            calculator.fun7("10", 3)
        with self.assertRaises(ValueError):
            calculator.fun7(10, "3")

    def test_fun8(self):
        # Basic absolute value tests
        self.assertEqual(calculator.fun8(5), 5)
        self.assertEqual(calculator.fun8(-5), 5)
        self.assertEqual(calculator.fun8(0), 0)
        self.assertEqual(calculator.fun8(3.14), 3.14)
        self.assertEqual(calculator.fun8(-3.14), 3.14)
        self.assertEqual(calculator.fun8(-100), 100)
        
        # Test invalid input types
        with self.assertRaises(ValueError):
            calculator.fun8("5")
        with self.assertRaises(ValueError):
            calculator.fun8([5])

    def test_fun9(self):
        # Basic square root tests
        self.assertEqual(calculator.fun9(4), 2.0)
        self.assertEqual(calculator.fun9(9), 3.0)
        self.assertEqual(calculator.fun9(16), 4.0)
        self.assertEqual(calculator.fun9(0), 0.0)
        self.assertEqual(calculator.fun9(1), 1.0)
        self.assertAlmostEqual(calculator.fun9(2), 1.414, places=3)
        self.assertEqual(calculator.fun9(0.25), 0.5)
        
        # Test negative number raises exception
        with self.assertRaises(ValueError):
            calculator.fun9(-4)
        with self.assertRaises(ValueError):
            calculator.fun9(-1)
        
        # Test invalid input types
        with self.assertRaises(ValueError):
            calculator.fun9("4")
        with self.assertRaises(ValueError):
            calculator.fun9([4])


if __name__ == '__main__':
    unittest.main()