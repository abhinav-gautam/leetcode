# https://leetcode.com/problems/add-two-numbers/


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """

        i, j = 0, 0
        carry = 0
        sum = []

        while i < len(l1) or j < len(l2):
            digit_sum = 0
            if i == j:
                digit_sum = l1[i] + l2[j] + carry
            elif i > j:
                digit_sum = l1[i] + carry
            elif j > i:
                digit_sum = l2[j] + carry

            carry = digit_sum // 10
            remainder = digit_sum % 10
            sum.append(remainder)

            if i == len(l1) - 1 and j == len(l2) - 1:
                break

            if i < len(l1) - 1:
                i += 1

            if j < len(l2) - 1:
                j += 1

        if carry != 0:
            sum.append(carry)

        return sum


# print(Solution().addTwoNumbers([2, 4, 3], [5, 6, 4]))
# print(Solution().addTwoNumbers([0], [0]))
print(Solution().addTwoNumbers([9, 9, 9, 9, 9, 9, 9], [9, 9, 9, 9]))
