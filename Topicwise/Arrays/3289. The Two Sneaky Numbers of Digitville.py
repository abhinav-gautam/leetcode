# https://leetcode.com/problems/the-two-sneaky-numbers-of-digitville/description/?envType=daily-question&envId=2025-10-31

from typing import List
from collections import Counter


class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        counts = Counter(nums)
        result = []
        for key, value in counts.items():
            if value == 2:
                result.append(key)
        return result
