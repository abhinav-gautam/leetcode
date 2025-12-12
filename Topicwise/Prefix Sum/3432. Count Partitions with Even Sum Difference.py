# https://leetcode.com/problems/count-partitions-with-even-sum-difference/description/?envType=daily-question&envId=2025-12-05

from typing import List


class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        total = sum(nums)
        n = len(nums)

        count = 0
        roll = nums[0]
        for i in range(1, n):
            diff = 2 * roll - total
            if diff % 2 == 0:
                count += 1
            roll += nums[i]

        return count


print(Solution().countPartitions([10, 10, 3, 7, 6]))
print(Solution().countPartitions([1, 2, 2]))
print(Solution().countPartitions([2, 4, 6, 8]))
