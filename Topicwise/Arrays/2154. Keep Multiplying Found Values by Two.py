# https://leetcode.com/problems/keep-multiplying-found-values-by-two/description/?envType=daily-question&envId=2025-11-19

from typing import List


class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        counter = set(nums)

        while original in counter:
            original *= 2

        return original


print(Solution().findFinalValue(nums=[5, 3, 6, 1, 12], original=3))
