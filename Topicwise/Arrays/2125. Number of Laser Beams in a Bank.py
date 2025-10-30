# https://leetcode.com/problems/number-of-laser-beams-in-a-bank/description/?envType=daily-question&envId=2025-10-27

from typing import List


class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        prev = bank[0].count("1")
        total = 0
        for i in range(1, len(bank)):
            curr = bank[i].count("1")
            if curr:
                total += curr * prev
                prev = curr
        return total


print(Solution().numberOfBeams(bank=["011001", "000000", "010100", "001000"]))
print(Solution().numberOfBeams(bank=["000", "111", "000"]))
