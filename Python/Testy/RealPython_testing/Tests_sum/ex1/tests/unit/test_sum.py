import timeit
import unittest
from __init__ import sum
from fractions import Fraction

class TestSum(unittest.TestCase):
    def test_list_int(self):
        """
        Test that  it can sum a list of integers
        """
        data = [1,2,3]
        result = sum(data)
        self.assertEqual(result, 6)
        
    def test_list_fraction(self):
        """
        Test that it can sum a list of fractions(ułamek)
        """
        
        data = [Fraction(1, 4), Fraction(1, 4), Fraction(2, 5)]
        result = sum(data)
        self.assertEqual(result, 1)
        
    def test_bad_type(self):
        """
        This test case will only pass if sum(data) raises a TypeError
        """
        data = "banana"
        with self.assertRaises(TypeError):
            result = sum(data)

#it starts the test in terminal
if __name__ == "__main__":
    unittest.main()
    