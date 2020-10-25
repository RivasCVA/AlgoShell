import unittest
from solutions import *

class IsPalindrome(unittest.TestCase):
    def test_case_1(self):
        string = 'abcdcba'

        expected = True
        actual = is_palindrome(string)

        self.assertEqual(expected, actual)

    def test_case_2(self):
        string = 'a'

        expected = True
        actual = is_palindrome(string)

        self.assertEqual(expected, actual)

    def test_case_3(self):
        string = 'ab'

        expected = False
        actual = is_palindrome(string)

        self.assertEqual(expected, actual)

    def test_case_4(self):
        string = 'aba'

        expected = True
        actual = is_palindrome(string)

        self.assertEqual(expected, actual)

    def test_case_5(self):
        string = 'abb'

        expected = False
        actual = is_palindrome(string)

        self.assertEqual(expected, actual)

    def test_case_6(self):
        string = 'abba'

        expected = True
        actual = is_palindrome(string)

        self.assertEqual(expected, actual)

    def test_case_7(self):
        string = 'abcdefghhgfedcba'

        expected = True
        actual = is_palindrome(string)

        self.assertEqual(expected, actual)

    def test_case_8(self):
        string = 'abcdefghihgfedcba'

        expected = True
        actual = is_palindrome(string)

        self.assertEqual(expected, actual)

    def test_case_9(self):
        string = 'abcdefghihgfeddcba'

        expected = False
        actual = is_palindrome(string)

        self.assertEqual(expected, actual)
        
class BracketMatch(unittest.TestCase):
    def test_case_1(self):
        text = ')'

        expected = 1
        actual = bracket_match(text)

        self.assertEqual(expected, actual)
        
    def test_case_2(self):
        text = '('

        expected = 1
        actual = bracket_match(text)
        
        self.assertEqual(expected, actual)
        
    def test_case_3(self):
        text = '(())'

        expected = 0
        actual = bracket_match(text)
        
        self.assertEqual(expected, actual)
        
    def test_case_4(self):
        text = '(()'

        expected = 1
        actual = bracket_match(text)
        
        self.assertEqual(expected, actual)
        
    def test_case_5(self):
        text = '())('

        expected = 2
        actual = bracket_match(text)
        
        self.assertEqual(expected, actual)
        
    def test_case_6(self):
        text = '))))'

        expected = 4
        actual = bracket_match(text)

        self.assertEqual(expected, actual)

    def test_case_7(self):
        text = ')('

        expected = 2
        actual = bracket_match(text)

        self.assertEqual(expected, actual)

    def test_case_8(self):
        text = '()()()()()'

        expected = 0
        actual = bracket_match(text)

        self.assertEqual(expected, actual)

class SentenceReverse(unittest.TestCase):
    def test_case_1(self):
        input = [" "," "]

        expected = [" "," "]
        actual = sentence_reverse(input)

        self.assertEqual(expected, actual)

    def test_case_2(self):

        input = ["a"," "," ","b"]

        expected = ["b"," "," ","a"]
        actual = sentence_reverse(input)

        self.assertEqual(expected, actual)

    def test_case_3(self):
        input = ["h","e","l","l","o"]

        expected = ["h","e","l","l","o"]
        actual = sentence_reverse(input)

        self.assertEqual(expected, actual)

    def test_case_4(self):
        input = ["p","e","r","f","e","c","t"," ","m","a","k","e","s"," ","p","r","a","c","t","i","c","e"]

        expected = ["p","r","a","c","t","i","c","e"," ","m","a","k","e","s"," ","p","e","r","f","e","c","t"]
        actual = sentence_reverse(input)

        self.assertEqual(expected, actual)

    def test_case_5(self):
        input = ["y","o","u"," ","w","i","t","h"," ","b","e"," ","f","o","r","c","e"," ","t","h","e"," ","m","a","y"]

        expected = ["m","a","y"," ","t","h","e"," ","f","o","r","c","e"," ","b","e"," ","w","i","t","h"," ","y","o","u"]
        actual = sentence_reverse(input)
      
        self.assertEqual(expected, actual)

    def test_case_6(self):
        input = ["g","r","e","a","t","e","s","t"," ","n","a","m","e"," ","f","i","r","s","t"," ","e","v","e","r"," ","n","a","m","e"," ","l","a","s","t"]

        expected = ["l","a","s","t"," ","n","a","m","e"," ","e","v","e","r"," ","f","i","r","s","t"," ","n","a","m","e"," ","g","r","e","a","t","e","s","t"]
        actual = sentence_reverse(input)

        self.assertEqual(expected, actual)

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

