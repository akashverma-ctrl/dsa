"""
Problem Statement

1. Two Sum
    Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
    You may assume that each input would have exactly one solution, and you may not use the same element twice.
    You can return the answer in any order.

Example 1:
    Input: nums = [2,7,11,15], target = 9
    Output: [0,1]
    Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

Example 2:
    Input: nums = [3,2,4], target = 6
    Output: [1,2]

Example 3:
    Input: nums = [3,3], target = 6
    Output: [0,1]

Constraints:
    2 <= nums.length <= 104
    -109 <= nums[i] <= 109
    -109 <= target <= 109
    Only one valid answer exists.


Follow-up: Can you come up with an algorithm that is less than O(n2) time complexity?
"""

import unittest


class TwoSum:
    def two_sum_dict(self, nums: list[int], target: int) -> list[int]:
        """
        This solution include a dict to store the mapping of number and it's index
        Time complexity: O(n)
        Space complexity: O(n)
        """
        result = {}
        for i, num in enumerate(nums):
            rem = target - num
            if rem in result:
                return [result[rem], i]
            result[num] = i
        # Since the problem guarantees exactly one solution, this line is unreachable but to make this funtion ready for any input, we can raise an exception if no solution is found.
        raise ValueError("No two sum solution found")


class TestTwoSum(unittest.TestCase):
    def setUp(self):
        self.two_sum = TwoSum()

    def test_two_sum_dict_when_vaild_input_given__expect_valid_target(self):
        nums = [2, 7, 11, 15]
        target = 9
        expected = [0, 1]
        actual = self.two_sum.two_sum_dict(nums, target)
        self.assertEqual(actual, expected)

    def test_two_sum_dict_when_invaild_input_given__expect_exception(self):
        nums = [2, 6, 11, 15]
        target = 9
        with self.assertRaises(ValueError):
            self.two_sum.two_sum_dict(nums, target)


if __name__ == "__main__":
    unittest.main()

    # # Uncomment below to run code locally
    # nums = [2,7,11,15]
    # target = 9
    # two_sum = TwoSum()
    # indexes = two_sum.two_sum_dict(nums, target)
    # print("Indices of the two numbers such that they add up to target are: ", indexes)
