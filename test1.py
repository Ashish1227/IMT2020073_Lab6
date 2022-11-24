#!/usr/bin/python3
# Test case for multiplying two numbers
import unittest
from function import muliplication

class TestMult(unittest.TestCase):
  
    """
    Test cases to multiply two numbers
    """
  
    def test_list_int(self):
        test_a = 2
        test_b = 4
        result = multiplication(test_a,test_b)
        self.assertEqual(result, 8)
       
    def test_list_int2(self):
        test_a = 3
        test_b = 4
        result = multiplication(test_a,test_b)
        self.assertEqual(result, 12)
       
    def test_list_int3(self):
        test_a = 8
        test_b = 2
        result = multiplication(test_a,test_b)
        self.assertEqual(result, 16)      

if __name__ == '__main__':
    unittest.main()
