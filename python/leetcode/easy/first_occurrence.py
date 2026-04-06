"""
Find the Index of the First Occurrence in a String
    Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

Example 1:
    Input: haystack = "sadbutsad", needle = "sad"
    Output: 0
    Explanation: "sad" occurs at index 0 and 6.
    The first occurrence is at index 0, so we return 0.

Example 2:
    Input: haystack = "leetcode", needle = "leeto"
    Output: -1
    Explanation: "leeto" did not occur in "leetcode", so we return -1.


Constraints:
    1 <= haystack.length, needle.length <= 104
    haystack and needle consist of only lowercase English characters.
"""


class FirstOccurrenceFinder:
    def strStr(self, h: str, n: str) -> int:
        k = 0
        i = 0
        index = 0
        while i < len(h):
            if h[i] == n[k]:
                if i + len(n) <= len(h):
                    if h[i : i + len(n)] == n:
                        return i
            i = i + 1
        return -1


import unittest


class TestFirstOccurrenceFinder(unittest.TestCase):
    def setUp(self):
        self.first_occurrence_finder = FirstOccurrenceFinder()

    def test_strStr_when_needle_occurs_in_haystack__expect_index_of_first_occurrence(
        self,
    ):
        haystack = "sadbutsad"
        needle = "sad"
        expected = 0
        actual = self.first_occurrence_finder.strStr(haystack, needle)
        self.assertEqual(expected, actual)

    def test_strStr_when_needle_does_not_occur_in_haystack__expect_negative_one(self):
        haystack = "leetcode"
        needle = "leeto"
        expected = -1
        actual = self.first_occurrence_finder.strStr(haystack, needle)
        self.assertEqual(expected, actual)

    def test_strStr_when_needle_occurs_once_in_haystack__expect_index_of_first_occurrence(
        self,
    ):
        haystack = "hello"
        needle = "ll"
        expected = 2
        actual = self.first_occurrence_finder.strStr(haystack, needle)
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
