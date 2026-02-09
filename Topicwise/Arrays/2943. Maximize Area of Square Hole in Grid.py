# https://leetcode.com/problems/maximize-area-of-square-hole-in-grid/?envType=daily-question&envId=2026-01-15

from typing import List


class Solution:
    def maxLen(self, bars):
        count = length = 2

        for i in range(1, len(bars)):
            if bars[i] - bars[i - 1] == 1:
                count += 1
            else:
                count = 2
            length = max(count, length)
        return length

    def maximizeSquareHoleArea(
        self, n: int, m: int, hBars: List[int], vBars: List[int]
    ) -> int:
        hBars.sort()
        vBars.sort()

        side = min(self.maxLen(hBars), self.maxLen(vBars))

        return side**2
