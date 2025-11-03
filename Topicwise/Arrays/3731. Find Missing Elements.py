# https://leetcode.com/problems/find-missing-elements/description/
from typing import List
from collections import Counter


class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        count = Counter(nums)
        minInt = min(nums)
        maxInt = max(nums)
        result = []

        for i in range(minInt, maxInt):
            if i not in count:
                result.append(i)
        return result


print(Solution().findMissingElements([1, 4, 2, 5]))
print(Solution().findMissingElements([7, 8, 6, 9]))
print(Solution().findMissingElements([5, 1]))
