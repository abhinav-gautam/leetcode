# https://leetcode.com/problems/successful-pairs-of-spells-and-potions/?envType=daily-question&envId=2025-10-08

from typing import List
import bisect


class Solution:
    def successfulPairs(
        self, spells: List[int], potions: List[int], success: int
    ) -> List[int]:
        result = []
        potions = sorted(potions)
        p_n = len(potions)
        for spell in spells:
            req = success / spell
            reqIndex = bisect.bisect_left(potions, req)
            result.append(p_n - reqIndex)
        return result


print(Solution().successfulPairs(spells=[5, 1, 3], potions=[1, 2, 3, 4, 5], success=7))
print(Solution().successfulPairs(spells=[3, 1, 2], potions=[8, 5, 8], success=16))
