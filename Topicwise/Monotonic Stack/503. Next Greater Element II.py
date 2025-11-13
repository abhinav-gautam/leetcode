# https://leetcode.com/problems/next-greater-element-ii/description/

from typing import List


class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [-1] * n
        stack = []

        i = j = 0
        while i < n * 2 - 1:
            while stack and nums[j] > nums[stack[-1]]:
                prev = stack.pop()
                result[prev] = nums[j]
            stack.append(j)
            i += 1
            j += 1
            if j == n:
                j = 0
        return result


print(Solution().nextGreaterElements([1, 2, 1]))
print(Solution().nextGreaterElements([1, 2, 3, 4, 3]))
