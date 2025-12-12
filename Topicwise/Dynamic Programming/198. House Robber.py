# https://leetcode.com/problems/house-robber/description/

from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        maxProfit = 0
        prev1 = nums[0]
        prev2 = 0

        for i in range(1, len(nums)):
            maxProfit = max(prev1, prev2 + nums[i])
            prev2 = prev1
            prev1 = maxProfit

        return maxProfit


print(Solution().rob([2, 7, 9, 3, 1]))
print(Solution().rob([2, 1, 1, 2]))
print(Solution().rob([1, 2, 3, 1]))
