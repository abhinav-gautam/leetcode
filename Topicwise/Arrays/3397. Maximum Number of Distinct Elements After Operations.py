# https://leetcode.com/problems/maximum-number-of-distinct-elements-after-operations/description/?envType=daily-question&envId=2025-10-18

from typing import List


class Solution:
    def maxDistinctElements(self, nums: List[int], k: int) -> int:
        nums = sorted(nums)

        nums[0] += -k
        maxValue = nums[0]

        for i in range(1, len(nums)):
            req = nums[i] - maxValue - 1
            if -k <= req <= k:
                nums[i] -= req
            elif req < nums[i]:
                nums[i] += -k
            maxValue = max(maxValue, nums[i])
        return len(list(set(nums)))


print(Solution().maxDistinctElements(nums=[1, 2, 2, 3, 3, 4], k=2))
print(Solution().maxDistinctElements(nums=[4, 4, 4, 4], k=1))
print(Solution().maxDistinctElements(nums=[7, 7, 7, 7, 9], k=1))
print(Solution().maxDistinctElements(nums=[1, 1, 1, 1, 1, 1, 1, 1, 5, 5, 5], k=3))
print(Solution().maxDistinctElements(nums=[7, 10, 10], k=2))
print(Solution().maxDistinctElements(nums=[10, 10, 10, 5, 10], k=1))
