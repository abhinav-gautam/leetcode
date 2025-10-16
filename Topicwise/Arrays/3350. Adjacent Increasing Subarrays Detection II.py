# https://leetcode.com/problems/adjacent-increasing-subarrays-detection-ii/description/?envType=daily-question&envId=2025-10-15

from typing import List


class Solution:
    def maxIncreasingSubarrays(self, nums: List[int]) -> int:
        prev = 0
        current = 1
        k = 0
        for i in range(1, len(nums)):
            if nums[i - 1] < nums[i]:
                current += 1
            else:
                prev = current
                current = 1
            k = max(min(prev, current), k, current // 2)
        return k


print(Solution().maxIncreasingSubarrays(nums=[2, 5, 7, 8, 9, 2, 3, 4, 3, 1]))
print(Solution().maxIncreasingSubarrays(nums=[1, 2, 3, 4, 4, 4, 4, 5, 6, 7]))
