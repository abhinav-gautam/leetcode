# https://leetcode.com/problems/maximum-running-time-of-n-computers/description/?envType=daily-question&envId=2025-12-01

from typing import List


class Solution:
    def maxRunTime(self, n: int, batteries: List[int]) -> int:
        batteries.sort()
        total = sum(batteries)

        while batteries[-1] > total // n:
            n -= 1
            total -= batteries.pop()

        return total // n
