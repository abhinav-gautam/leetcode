# https://leetcode.com/problems/maximum-subarray/description/

from typing import List


# Kadane's Algorithm
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        currentMax = 0
        maxTillNow = float("-inf")

        for num in nums:
            currentMax = max(num, currentMax + num)
            maxTillNow = max(maxTillNow, currentMax)

        return maxTillNow


print(Solution().maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
