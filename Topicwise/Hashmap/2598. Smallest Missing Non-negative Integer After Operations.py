# https://leetcode.com/problems/smallest-missing-non-negative-integer-after-operations/description/?envType=daily-question&envId=2025-10-16

from typing import List
from collections import Counter


class Solution:
    def findSmallestInteger(self, nums: List[int], value: int) -> int:
        modMap = Counter([x % value for x in nums])
        modArr = []
        mex = 0

        for key, val in modMap.items():
            for i in range(val):
                num = key + value * i
                modArr.append(num)

        for num in sorted(modArr):
            if num == mex:
                mex += 1

        return mex


# print(Solution().findSmallestInteger(nums=[1, -10, 7, 13, 6, 8], value=5))
# print(Solution().findSmallestInteger(nums=[1, -10, 7, 13, 6, 8], value=7))
print(Solution().findSmallestInteger(nums=[3, 0, 3, 2, 4, 2, 1, 1, 0, 4], value=5))
