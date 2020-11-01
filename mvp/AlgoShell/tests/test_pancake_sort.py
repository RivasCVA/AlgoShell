import unittest
from solutions import *

class PancakeSort(unittest.TestCase):
    def test_case_1(self):
        arr = [1]

        expected = [1]
        actual = pancake_sort(arr)

        self.assertEqual(expected, actual)
    
    def test_case_2(self):
        arr = [1,2]

        expected = [1,2]
        actual = pancake_sort(arr)

        self.assertEqual(expected, actual)
    
    def test_case_3(self):
        arr = [1,3,1]

        expected = [1,1,3]
        actual = pancake_sort(arr)

        self.assertEqual(expected, actual)

    def test_case_4(self):
        arr = [3,1,2,4,6,5]

        expected = [1,2,3,4,5,6]
        actual = pancake_sort(arr)

        self.assertEqual(expected, actual)

    def test_case_5(self):
        arr = [10,9,8,7,6,5,4,3,2,1]

        expected = [1,2,3,4,5,6,7,8,9,10]
        actual = pancake_sort(arr)

        self.assertEqual(expected, actual)

    def test_case_6(self):
        arr = [10,9,8,6,7,5,4,3,2,1,9,10,8,7,6,5,4,3,2,1,10,9,8,7,6,5,4,3,2,1]

        expected = [1,1,1,2,2,2,3,3,3,4,4,4,5,5,5,6,6,6,7,7,7,8,8,8,9,9,9,10,10,10]
        actual = pancake_sort(arr)

        self.assertEqual(expected, actual)

if __name__ == '__main__':
    unittest.main()