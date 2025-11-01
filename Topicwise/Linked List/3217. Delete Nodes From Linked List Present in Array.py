# https://leetcode.com/problems/delete-nodes-from-linked-list-present-in-array/?envType=daily-question&envId=2025-11-01

# Definition for singly-linked list.
from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def modifiedList(
        self, nums: List[int], head: Optional[ListNode]
    ) -> Optional[ListNode]:
        numsSet = set(nums)
        while head.val in numsSet:
            head = head.next
        curr = head
        nxt = head
        while curr and curr.next:
            if curr.next.val not in numsSet:
                curr = curr.next
                nxt = curr
            else:
                nxt = curr.next
                while nxt and nxt.val in numsSet:
                    nxt = nxt.next
                curr.next = nxt
                curr = nxt

        return head


print(Solution().modifiedList(nums=[1, 2, 3], head=[1, 2, 3, 4, 5]))
