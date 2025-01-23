import unittest
# palindrome.py
def is_palindrome(s):
    # Remove non-alphanumeric characters and convert to lowercase
    clean_s = ''.join(c for c in s if c.isalnum()).lower()
    
    # Check if the string is the same forwards and backwards
    return clean_s == clean_s[::-1]


class TestPalindrome(unittest.TestCase):
    def firstTest(self):
        self.assertTrue(is_palindrome("cock"))

if __name__ == '__main__':
    unittest.main()


