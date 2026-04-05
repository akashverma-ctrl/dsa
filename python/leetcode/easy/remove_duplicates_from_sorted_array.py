"""
Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same.
Consider the number of unique elements in nums to be k​​​​​​​​​​​​​​. After removing duplicates, return the number of unique elements k.
The first k elements of nums should contain the unique numbers in sorted order. The remaining elements beyond index k - 1 can be ignored.

Custom Judge:
    The judge will test your solution with the following code:

    int[] nums = [...]; // Input array
    int[] expectedNums = [...]; // The expected answer with correct length

    int k = removeDuplicates(nums); // Calls your implementation

    assert k == expectedNums.length;
    for (int i = 0; i < k; i++) {
        assert nums[i] == expectedNums[i];
    }
    If all assertions pass, then your solution will be accepted.

Example 1:
    Input: nums = [1,1,2]
    Output: 2, nums = [1,2,_]
    Explanation: Your function should return k = 2, with the first two elements of nums being 1 and 2 respectively.
    It does not matter what you leave beyond the returned k (hence they are underscores).

Example 2:
    Input: nums = [0,0,1,1,1,2,2,3,3,4]
    Output: 5, nums = [0,1,2,3,4,_,_,_,_,_]
    Explanation: Your function should return k = 5, with the first five elements of nums being 0, 1, 2, 3, and 4 respectively.
    It does not matter what you leave beyond the returned k (hence they are underscores).

Constraints:
    1 <= nums.length <= 3 * 104
    -100 <= nums[i] <= 100
    nums is sorted in non-decreasing order.
"""

import unittest

class DuplicateRemover:
    def removeDuplicates(self, nums: list[int]) -> int:
        nums_len = len(nums)
        if nums_len == 1:
            return 1
        i, j = 0, 0
        for i in range(len(nums) - 1):
            j = i + 1
            if nums[i] > nums[j]:
                break
            count = 0
            while nums[i] == nums[j]:
                if count > len(nums):
                    break
                count = count + 1
                temp = nums[j]
                for k in range(j, len(nums) - 1):
                    nums[k] = nums[k + 1]
                nums[len(nums) - 1] = temp
        return j


class TestDuplicateRemover(unittest.TestCase):
    def setUp(self):
        self.duplicate_remover = DuplicateRemover()

    def test_remove_duplicates_when_duplicates_given__expect_number_of_unique_elements(self):
        nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
        expected = 5
        actual = self.duplicate_remover.removeDuplicates(nums)
        self.assertEqual(expected, actual)

    def test_remove_duplicates_when_two_duplicates_given__expect_number_of_unique_elements(
        self,
    ):
        nums = [0, 4]
        expected = 2
        actual = self.duplicate_remover.removeDuplicates(nums)
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
