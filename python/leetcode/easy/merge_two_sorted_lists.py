"""
You are given the heads of two sorted linked lists list1 and list2.
Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.
Return the head of the merged linked list.

Example 1:
    Input: list1 = [1,2,4], list2 = [1,3,4]
    Output: [1,1,2,3,4,4]

Example 2:
    Input: list1 = [], list2 = []
    Output: []

Example 3:
    Input: list1 = [], list2 = [0]
    Output: [0]

Constraints:
    The number of nodes in both lists is in the range [0, 50].
    -100 <= Node.val <= 100
    Both list1 and list2 are sorted in non-decreasing order.
"""


# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class ListMerger:
    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        i = list1
        j = list2
        result = None
        k = result
        if not list1 and not list2:
            return None

        while i and j:
            if i.val < j.val:
                if not result:
                    result = ListNode(i.val)
                    k = result
                else:
                    k.next = ListNode(i.val)
                    k = k.next
                i = i.next
            else:
                if not result:
                    result = ListNode(j.val)
                    k = result
                else:
                    k.next = ListNode(j.val)
                    k = k.next
                j = j.next
        while i:
            if not result:
                result = ListNode(i.val)
                k = result
            else:
                k.next = ListNode(i.val)
                k = k.next
            i = i.next
        while j:
            if not result:
                result = ListNode(j.val)
                k = result
            else:
                k.next = ListNode(j.val)
                k = k.next
            j = j.next
        return result


import unittest

class TestListMerger(unittest.TestCase):
    def setUp(self):
        self.merger = ListMerger()

    def test_merge_two_lists(self):
        # Test case 1
        list1 = ListNode(1)
        list1.next = ListNode(2)
        list1.next.next = ListNode(4)

        list2 = ListNode(1)
        list2.next = ListNode(3)
        list2.next.next = ListNode(4)

        result = self.merger.mergeTwoLists(list1, list2)
        values = []
        while result:
            values.append(result.val)
            result = result.next
        self.assertEqual(values, [1, 1, 2, 3, 4, 4])

        # Test case 2
        list1 = None
        list2 = None
        result = self.merger.mergeTwoLists(list1, list2)
        self.assertIsNone(result)

        # Test case 3
        list1 = None
        list2 = ListNode(0)
        result = self.merger.mergeTwoLists(list1, list2)
        values = []
        while result:
            values.append(result.val)
            result = result.next
        self.assertEqual(values, [0])

if __name__ == "__main__":
    unittest.main()