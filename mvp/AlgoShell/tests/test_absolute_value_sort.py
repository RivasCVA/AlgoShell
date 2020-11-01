import unittest
from solutions import *

class AbsoluteValueSort(unittest.TestCase):
    def test_case_1(self):
        arr = [2,-7,-2,-2,0]

        expected = [0,-2,-2,2,-7]
        actual = abs_sort(arr)

        self.assertEqual(expected, actual)
    
    def test_case_2(self):
        arr = [-2,1]

        expected = [1,-2]
        actual = abs_sort(arr)

        self.assertEqual(expected, actual)
    
    def test_case_3(self):
        arr = [0,1,2]

        expected = [0,1,2]
        actual = abs_sort(arr)

        self.assertEqual(expected, actual)

    def test_case_4(self):
        arr = [2,-1,-1,-1]

        expected = [-1,-1,-1,2]
        actual = abs_sort(arr)

        self.assertEqual(expected, actual)

    def test_case_5(self):
        arr = [-2,3,5,-1,4]

        expected = [-1,-2,3,4,5]
        actual = abs_sort(arr)

        self.assertEqual(expected, actual)

    def test_case_6(self):
        arr = [4,-1,6,-4,2,-1]

        expected = [-1,-1,2,-4,4,6]
        actual = abs_sort(arr)

        self.assertEqual(expected, actual)
    
    def test_case_7(self):
        arr = [6,4,-5,0,-1,7,0]

        expected = [0,0,-1,4,-5,6,7]
        actual = abs_sort(arr)

        self.assertEqual(expected, actual)
    
    def test_case_8(self):
        arr = [-7,-2,-2,6,5,-6,-2,-6]

        expected = [-2,-2,-2,5,-6,-6,6,-7]
        actual = abs_sort(arr)

        self.assertEqual(expected, actual)

    def test_case_9(self):
        arr = [-4,9,-1,1,-1,2,-8,-6,3]

        expected = [-1,-1,1,2,3,-4,-6,-8,9]
        actual = abs_sort(arr)

        self.assertEqual(expected, actual)

if __name__ == '__main__':
    unittest.main()