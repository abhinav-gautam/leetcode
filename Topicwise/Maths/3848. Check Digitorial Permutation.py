# https://leetcode.com/problems/check-digitorial-permutation/description/

from collections import Counter
from math import factorial


class Solution:
    def isDigitorialPermutation(self, n: int) -> bool:
        digitorials = ["1", "2", "145", "40585"]

        n_count = Counter(str(n))

        for d in digitorials:
            if Counter(d) == n_count:
                return True

        return False
