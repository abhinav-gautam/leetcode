# https://leetcode.com/problems/3sum-closest/description/

from typing import List
import bisect


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums = sorted(nums)
        n = len(nums)
        minGap = float("inf")
        closestSum = 0
        for i in range(n - 2):
            left = i + 1
            right = n - 1
            while left < right:
                sum = nums[i] + nums[left] + nums[right]
                gap = abs(target - sum)

                if gap < minGap:
                    closestSum = sum
                    minGap = gap

                if sum > target:
                    right -= 1
                else:
                    left += 1

        return closestSum


print(Solution().threeSumClosest([-1, 2, 1, -4], 1))
print(Solution().threeSumClosest(nums=[0, 0, 0], target=1))
print(Solution().threeSumClosest(nums=[1, 1, -1], target=2))
print(Solution().threeSumClosest(nums=[10, 20, 30, 40, 50, 60, 70, 80, 90], target=1))
