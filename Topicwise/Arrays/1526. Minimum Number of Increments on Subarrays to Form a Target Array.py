# https://leetcode.com/problems/minimum-number-of-increments-on-subarrays-to-form-a-target-array/description/?envType=daily-question&envId=2025-10-30

from typing import List


class Solution:
    def minNumberOperations(self, target: List[int]) -> int:
        res = prev = 0
        for x in target:
            if x > prev:
                res += x - prev
            prev = x
        return res
