# https://leetcode.com/problems/house-robber-ii/description/

from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        # Robbing from house 0 to n-1
        maxProfit1 = 0
        prev1 = nums[0]
        prev2 = 0

        for i in range(1, len(nums) - 1):
            maxProfit1 = max(prev1, prev2 + nums[i])
            prev2 = prev1
            prev1 = maxProfit1

        # Robbing from house 1 to n
        maxProfit2 = 0
        prev1 = nums[1]
        prev2 = 0

        for i in range(2, len(nums)):
            maxProfit2 = max(prev1, prev2 + nums[i])
            prev2 = prev1
            prev1 = maxProfit2

        return max(maxProfit1, maxProfit2, nums[0])
