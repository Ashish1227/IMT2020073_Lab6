#!/usr/bin/python3
# Test case for multiplying two numbers
import unittest
from function import muliplication

class TestMult(unittest.TestCase):
  
    def test_list_int(self):
        """
        Test case to multiply two numbers
        """
        test_a = 2
        test_b = 4
        result = multiplication(test_a,test_b)
        self.assertEqual(result, 8)

if __name__ == '__main__':
    unittest.main()
