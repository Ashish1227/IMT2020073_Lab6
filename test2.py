#!/usr/bin/python3
# Test case for multiplying two numbers
import unittest

from function import multiplication

class Testmult(unittest.TestCase):
    def test_list_int(self):
        """
        Test case to multiply two numbers
        """
        test_a = 4
        test_b = 23
        result = multiplication(test_a,test_b)
        self.assertEqual(result, 500)

if __name__ == '__main__':
    unittest.main()
