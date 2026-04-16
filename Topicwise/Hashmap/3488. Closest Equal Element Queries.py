# https://leetcode.com/problems/closest-equal-element-queries/description/?envType=daily-question&envId=2026-04-16

from typing import List
from collections import defaultdict
import bisect


class Solution:
    def solveQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        n = len(nums)
        posMap = defaultdict(list)

        for index, num in enumerate(nums):
            posMap[num].append(index)

        result = []

        for queryIndex in queries:
            posArr = posMap[nums[queryIndex]]

            if len(posArr) == 1:
                result.append(-1)
                continue

            posInPosArr = bisect.bisect_left(posArr, queryIndex)

            leftPos = posArr[(posInPosArr - 1) % len(posArr)]
            leftDistance = abs(queryIndex - leftPos)
            leftMinDistance = min(leftDistance, n - leftDistance)

            rightPos = posArr[(posInPosArr + 1) % len(posArr)]
            rightDistance = abs(queryIndex - rightPos)
            rightMinDistance = min(rightDistance, n - rightDistance)

            result.append(min(leftMinDistance, rightMinDistance))

        return result


print(Solution().solveQueries(nums=[1, 3, 1, 4, 1, 3, 2], queries=[0, 3, 5]))
