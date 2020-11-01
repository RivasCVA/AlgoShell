import unittest
from solutions import *

class NumberOfPaths(unittest.TestCase):
    def test_case_1(self):
        n = 1

        expected = 1
        actual = num_of_paths_to_dest(n)

        self.assertEqual(expected, actual)
    
    def test_case_2(self):
        n = 2

        expected = 1
        actual = num_of_paths_to_dest(n)

        self.assertEqual(expected, actual)
    
    def test_case_3(self):
        n = 3

        expected = 2
        actual = num_of_paths_to_dest(n)

        self.assertEqual(expected, actual)
    
    def test_case_4(self):
        n = 4

        expected = 5
        actual = num_of_paths_to_dest(n)

        self.assertEqual(expected, actual)
    
    def test_case_5(self):
        n = 6

        expected = 42
        actual = num_of_paths_to_dest(n)

        self.assertEqual(expected, actual)
    
    def test_case_6(self):
        n = 17

        expected = 35357670
        actual = num_of_paths_to_dest(n)

        self.assertEqual(expected, actual)

if __name__ == '__main__':
    unittest.main()