"""
Given an integer x, return true if x is a palindrome, and false otherwise.

Example 1:
    Input: x = 121
    Output: true
    Explanation: 121 reads as 121 from left to right and from right to left.

Example 2:
    Input: x = -121
    Output: false
    Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.

Example 3:
    Input: x = 10
    Output: false
    Explanation: Reads 01 from right to left. Therefore it is not a palindrome.

Constraints:
    -231 <= x <= 231 - 1

Follow up: Could you solve it without converting the integer to a string?
"""

import unittest


class PalindromeFinder:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        temp = x
        reverse = 0
        while temp:
            rem = temp % 10
            reverse = reverse * 10 + rem
            temp = temp // 10
        return x == reverse


class TestPalindromeFinder(unittest.TestCase):
    def setUp(self):
        self.palindrome_finder = PalindromeFinder()

    def test_is_palindrome_when_palindrome_input_given__expect_true(self):
        x = 121
        expected = True
        actual = self.palindrome_finder.isPalindrome(x)
        self.assertEqual(actual, expected)

    def test_is_palindrome_when_negative_input_given__expect_false(self):
        x = -121
        expected = False
        actual = self.palindrome_finder.isPalindrome(x)
        self.assertEqual(actual, expected)

    def test_is_palindrome_when_non_palindrome_input_given__expect_false(self):
        x = 10
        expected = False
        actual = self.palindrome_finder.isPalindrome(x)
        self.assertEqual(actual, expected)

    def test_is_palindrome_when_0_given__expect_true(self):
        x = 0
        expected = True
        actual = self.palindrome_finder.isPalindrome(x)
        self.assertEqual(actual, expected)


if __name__ == "__main__":
    unittest.main()
