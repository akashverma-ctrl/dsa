"""
14. Longest Common Prefix
    Write a function to find the longest common prefix string amongst an array of strings.
    If there is no common prefix, return an empty string "".

Example 1:
    Input: strs = ["flower","flow","flight"]
    Output: "fl"

Example 2:
    Input: strs = ["dog","racecar","car"]
    Output: ""
    Explanation: There is no common prefix among the input strings.

Constraints:
    1 <= strs.length <= 200
    0 <= strs[i].length <= 200
    strs[i] consists of only lowercase English letters if it is non-empty.
"""

import unittest


class longestCommonPrefixFinder:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        if len(strs) == 1:
            return strs[0]
        common = strs[0]
        for i in range(1, len(strs)):
            common = self._get_common_in_list(common, strs[i])
        return common

    def _get_common_in_list(self, lst1, lst2):
        common = ""
        len1 = len(lst1)
        len2 = len(lst2)
        min_len = len1 if len1 < len2 else len2
        for i in range(min_len):
            if lst1[i] == lst2[i]:
                common = common + lst1[i]
            else:
                break
        return common


class TestLongestCommonPrefixFinder(unittest.TestCase):
    def setUp(self):
        self.longest_common_prefix_finder = longestCommonPrefixFinder()

    def test_longest_common_prefix_when_valid_input_given__expect_common_prefix(self):
        strs = ["flower", "flow", "flight"]
        expected = "fl"
        actual = self.longest_common_prefix_finder.longestCommonPrefix(strs)
        self.assertEqual(actual, expected)

    def test_longest_common_prefix_when_no_common_prefix_given__expect_empty_string(
        self,
    ):
        strs = ["dog", "racecar", "car"]
        expected = ""
        actual = self.longest_common_prefix_finder.longestCommonPrefix(strs)
        self.assertEqual(actual, expected)

    def test_longest_common_prefix_when_single_string_given__expect_same_string(self):
        strs = ["single"]
        expected = "single"
        actual = self.longest_common_prefix_finder.longestCommonPrefix(strs)
        self.assertEqual(actual, expected)


if __name__ == "__main__":
    unittest.main()
