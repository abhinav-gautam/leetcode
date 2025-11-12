# https://leetcode.com/problems/minimum-number-of-operations-to-make-all-array-elements-equal-to-1/description/?envType=daily-question&envId=2025-11-12

from typing import List
import math


class Solution:
    def minOperations(self, nums: List[int]) -> int:
        totalOps = float("inf")
        ones = nums.count(1)

        if ones:
            return len(nums) - ones

        for i in range(0, len(nums)):
            g = nums[i]
            for j in range(i + 1, len(nums)):
                g = math.gcd(g, nums[j])
                if g == 1:
                    totalOps = min(totalOps, j - i)
                    break
        if totalOps == float("inf"):
            return -1
        else:
            return totalOps + len(nums) - 1


print(Solution().minOperations([2, 6, 3, 4]))
print(Solution().minOperations([6, 10, 15]))
print(Solution().minOperations([2, 10, 6, 14]))
