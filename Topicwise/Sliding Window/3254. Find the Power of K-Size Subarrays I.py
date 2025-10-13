# https://leetcode.com/problems/find-the-power-of-k-size-subarrays-i/description/
from typing import List


class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        left = right = 0
        n = len(nums)
        result = [-1] * (n - k + 1)

        while right < n:
            if right > 0 and nums[right] - nums[right - 1] != 1:
                left = right
            while left < right and right - left + 1 > k:
                left += 1
            if right - left + 1 == k:
                result[right - k + 1] = nums[right]
            right += 1
        return result


# print(Solution().resultsArray(nums=[1, 2, 3, 4, 3, 2, 5], k=3))
# print(Solution().resultsArray(nums=[3, 2, 3, 2, 3, 2], k=2))
# print(Solution().resultsArray(nums=[2, 2, 2, 2, 2], k=4))
# print(Solution().resultsArray(nums=[1, 30, 31, 32], k=3))
print(Solution().resultsArray(nums=[3, 2, 43, 44, 45], k=3))
