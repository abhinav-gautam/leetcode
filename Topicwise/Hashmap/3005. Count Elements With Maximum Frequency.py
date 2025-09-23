# https://leetcode.com/problems/count-elements-with-maximum-frequency/description/?envType=daily-question&envId=2025-09-22

from typing import List


class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        numsDict = {}
        for num in nums:
            if num in numsDict:
                numsDict[num] += 1
            else:
                numsDict[num] = 1
        maxNums = max(numsDict.values())
        count = 0
        for num in numsDict.values():
            if num == maxNums:
                count += 1

        return count * maxNums


print(Solution().maxFrequencyElements([1, 2, 2, 3, 1, 4]))
