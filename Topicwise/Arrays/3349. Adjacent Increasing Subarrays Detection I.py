# https://leetcode.com/problems/adjacent-increasing-subarrays-detection-i/description/?envType=daily-question&envId=2025-10-14
from typing import List


class Solution:
    def hasIncreasingSubarrays(self, nums: List[int], k: int) -> bool:
        prev, current = 0, 1
        for i in range(1, len(nums)):
            if nums[i - 1] < nums[i]:
                current += 1
            else:
                prev = current
                current = 1
            if (current >= k and prev >= k) or current >= k * 2:
                return True
        return False


print(Solution().hasIncreasingSubarrays(nums=[1, 2, 3, 4, 4, 4, 4, 5, 6, 7], k=5))
print(Solution().hasIncreasingSubarrays(nums=[2, 5, 7, 8, 9, 2, 3, 4, 3, 1], k=3))
print(Solution().hasIncreasingSubarrays(nums=[-15, 19], k=1))
