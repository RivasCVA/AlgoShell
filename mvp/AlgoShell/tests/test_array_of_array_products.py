import unittest
from solutions import array_of_array_products

class ArrayOfArrayProducts(unittest.TestCase):
    def test_case_1(self):
        input = []
        expected = []

        actual = array_of_array_products(input)

        self.assertEqual(expected, actual)
    
    def test_case_2(self):
        input = [1]
        expected = []

        actual = array_of_array_products(input)

        self.assertEqual(expected, actual)    

    def test_case_3(self):
        input = [2,2]
        expected = [2,2]

        actual = array_of_array_products(input)

        self.assertEqual(expected, actual)
    
    def test_case_4(self):
        input = [2,7,3,4]
        expected = [84,24,56,42]

        actual = array_of_array_products(input)

        self.assertEqual(expected, actual)    

    def test_case_5(self):
        input = [2,3,0,982,10]
        expected = [0,0,58920,0,0]

        actual = array_of_array_products(input)

        self.assertEqual(expected, actual)
    
    def test_case_6(self):
        input = [-3,17,430,-6,5,-12,-11,5]
        expected = [-144738000,25542000,1009800,-72369000,86842800,-36184500,-39474000,86842800]

        actual = array_of_array_products(input)

        self.assertEqual(expected, actual)

if __name__ == '__main__':
    unittest.main()