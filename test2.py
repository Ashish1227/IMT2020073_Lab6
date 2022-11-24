#!/usr/bin/python3
# Test case for multiplying two numbers
import unittest

from function import multiplication

class Testmult(unittest.TestCase):
    
    """
    Test case to multiply two numbers
    """
    
    def test_list_int(self):
        test_a = 4
        test_b = 23
        result = multiplication(test_a,test_b)
        self.assertEqual(result, 500)
        
    def test_list_int2(self):
        test_a = 4
        test_b = 45
        result = multiplication(test_a,test_b)
        self.assertEqual(result, 500)
        
    def test_list_int3(self):
        test_a = 0
        test_b = 12
        result = multiplication(test_a,test_b)
        self.assertEqual(result, 5)

if __name__ == '__main__':
    unittest.main()
