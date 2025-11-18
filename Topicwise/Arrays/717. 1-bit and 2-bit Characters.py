# https://leetcode.com/problems/1-bit-and-2-bit-characters/description/?envType=daily-question&envId=2025-11-18
from typing import List


class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        i = 0

        while i < len(bits) - 1:
            if bits[i] == 1:
                i += 1
            i += 1

        return i == len(bits) - 1


print(Solution().isOneBitCharacter([1, 0, 0]))
print(Solution().isOneBitCharacter([1, 1, 1, 0]))
