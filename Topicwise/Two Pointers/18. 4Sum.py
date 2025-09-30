# https://leetcode.com/problems/4sum/description/

from typing import List


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums = sorted(nums)
        n = len(nums)
        result = []
        for a in range(n - 3):
            for b in range(a + 1, n - 2):
                c = b + 1
                d = n - 1
                while c < d:
                    sum = nums[a] + nums[b] + nums[c] + nums[d]

                    if (
                        sum == target
                        and [nums[a], nums[b], nums[c], nums[d]] not in result
                    ):
                        result.append([nums[a], nums[b], nums[c], nums[d]])

                    if sum < target:
                        c += 1
                    else:
                        d -= 1
        return result


print(Solution().fourSum(nums=[1, 0, -1, 0, -2, 2], target=0))
print(Solution().fourSum(nums=[2, 2, 2, 2, 2], target=8))
