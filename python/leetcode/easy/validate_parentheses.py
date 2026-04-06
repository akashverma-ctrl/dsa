"""
20. Valid Parentheses
    Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
    An input string is valid if:
        Open brackets must be closed by the same type of brackets.
        Open brackets must be closed in the correct order.
        Every close bracket has a corresponding open bracket of the same type.


Example 1:
    Input: s = "()"
    Output: true

Example 2:
    Input: s = "()[]{}"
    Output: true

Example 3:
    Input: s = "(]"
    Output: false

Example 4:
    Input: s = "([])"
    Output: true

Example 5:
    Input: s = "([)]"
    Output: false

Constraints:
    1 <= s.length <= 104
    s consists of parentheses only '()[]{}'.
"""

import unittest


class ValidParenthesesFinder:
    def isValid(self, s: str) -> bool:
        brackets = {
            ")": "(",
            "}": "{",
            "]": "[",
        }
        stack = []
        for bkt in s:
            if bkt in ("(", "{", "["):
                stack.append(bkt)
            else:
                if stack:
                    if brackets[bkt] != stack.pop():
                        return False
                else:
                    return False
        if stack:
            return False
        return True


class TestValidParenthesesFinder(unittest.TestCase):
    def setUp(self):
        self.valid_parentheses_finder = ValidParenthesesFinder()

    def test_is_valid_when_valid_parentheses_given__expect_true(self):
        s = "()[]{}"
        expected = True
        actual = self.valid_parentheses_finder.isValid(s)
        self.assertEqual(actual, expected)

    def test_is_valid_when_invalid_parentheses_given__expect_false(self):
        s = "([)]"
        expected = False
        actual = self.valid_parentheses_finder.isValid(s)
        self.assertEqual(actual, expected)


if __name__ == "__main__":
    unittest.main()
