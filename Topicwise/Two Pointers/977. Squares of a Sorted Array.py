# https://leetcode.com/problems/squares-of-a-sorted-array/description/

from typing import List


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        result = [0] * len(nums)
        i = 0
        k = j = len(nums) - 1

        while k >= 0:
            i2 = nums[i] ** 2
            j2 = nums[j] ** 2

            if i2 >= j2:
                result[k] = i2
                i += 1
            else:
                result[k] = j2
                j -= 1
            k -= 1

        return result


print(Solution().sortedSquares([-4, -1, 0, 3, 10]))
print(Solution().sortedSquares([-7, -3, 2, 3, 11]))
