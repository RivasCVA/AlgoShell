import unittest
from solutions import *

class ShortestWordEditPath(unittest.TestCase):
    def test_case_1(self):
        source = 'bit'
        target = 'dog'
        words = ['put', 'but', 'big', 'pot', 'pog', 'dog', 'log']

        expected = 5
        actual = shortest_word_edit_path(source, target, words)

        self.assertEqual(actual, expected)

    def test_case_2(self):
        source = 'no'
        target = 'go'
        words = ['to']

        expected = -1
        actual = shortest_word_edit_path(source, target, words)

        self.assertEqual(actual, expected)

    def test_case_3(self):
        source = 'bit'
        target = 'pog'
        words = ['but', 'put', 'big', 'pot', 'pog', 'pig', 'dog', 'lot']

        expected = 3
        actual = shortest_word_edit_path(source, target, words)

        self.assertEqual(actual, expected)

    def test_case_4(self):
        source = 'aa'
        target = 'bb'
        words = ['ab', 'bb']

        expected = 2
        actual = shortest_word_edit_path(source, target, words)

    def test_case_5(self):
        source = 'abc'
        target = 'ab'
        words = ['abc', 'ab']

        expected = -1
        actual = shortest_word_edit_path(source, target, words)

    def test_case_6(self):
        source = 'aa'
        target = 'bbb'
        words = ['ab', 'bb']

        expected = -1
        actual = shortest_word_edit_path(source, target, words)

if __name__ == '__main__':
    unittest.main()
