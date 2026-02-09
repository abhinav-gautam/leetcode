# https://leetcode.com/problems/minimum-difference-between-highest-and-lowest-of-k-scores/?envType=daily-question&envId=2026-01-25

from typing import List


class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        minDiff = float("inf")

        for i in range(len(nums) - k + 1):
            diff = nums[i + k - 1] - nums[i]
            minDiff = min(diff, minDiff)

        return minDiff


print(Solution().minimumDifference([9, 4, 1, 7], k=2))
