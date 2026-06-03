"""
35. Search Insert Position
    Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.
    You must write an algorithm with O(log n) runtime complexity.

Example 1:
    Input: nums = [1,3,5,6], target = 5
    Output: 2

Example 2:
    Input: nums = [1,3,5,6], target = 2
    Output: 1

Example 3:
    Input: nums = [1,3,5,6], target = 7
    Output: 4

Constraints:
    1 <= nums.length <= 104
    -104 <= nums[i] <= 104
    nums contains distinct values sorted in ascending order.
    -104 <= target <= 104
"""


class InsertPositionFinder:
    def searchInsert(self, nums: list[int], target: int) -> int:
        for i, num in enumerate(nums):
            if num >= target:
                return i
        return i + 1


import unittest


class TestInsertPositionFinder(unittest.TestCase):
    def setUp(self):
        self.insert_position_finder = InsertPositionFinder()

    def test_searchInsert_when_target_occurs_in_nums__expect_index_of_target(self):
        nums = [1, 3, 5, 6]
        target = 5
        expected = 2
        actual = self.insert_position_finder.searchInsert(nums, target)
        self.assertEqual(expected, actual)

    def test_searchInsert_when_target_does_not_occur_in_nums__expect_index_where_target_would_be_inserted(
        self,
    ):
        nums = [1, 3, 5, 6]
        target = 2
        expected = 1
        actual = self.insert_position_finder.searchInsert(nums, target)
        self.assertEqual(expected, actual)

    def test_searchInsert_when_target_is_greater_than_all_elements_in_nums__expect_length_of_nums(
        self,
    ):
        nums = [1, 3, 5, 6]
        target = 7
        expected = len(nums)
        actual = self.insert_position_finder.searchInsert(nums, target)
        self.assertEqual(expected, actual)

    def test_searchInsert_when_target_is_less_than_all_elements_in_nums__expect_zero(
        self,
    ):
        nums = [1, 3, 5, 6]
        target = 0
        expected = 0
        actual = self.insert_position_finder.searchInsert(nums, target)
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
