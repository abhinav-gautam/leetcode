# https://leetcode.com/problems/largest-perimeter-triangle/description/?envType=daily-question&envId=2025-09-28

from typing import List


class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums = sorted(nums)
        n = len(nums)
        for i in range(n - 1, 1, -1):
            if nums[i] < nums[i - 1] + nums[i - 2]:
                maxSum = nums[i] + nums[i - 1] + nums[i - 2]
                return maxSum
        return 0


print(Solution().largestPerimeter([2, 1, 2]))
print(Solution().largestPerimeter([3, 2, 3, 4]))
