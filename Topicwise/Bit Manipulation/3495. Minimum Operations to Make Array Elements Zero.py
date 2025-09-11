# https://leetcode.com/problems/minimum-operations-to-make-array-elements-zero/description/?envType=daily-question&envId=2025-09-06

import math


class Solution:
    def minOperations(self, queries):
        ans = 0
        for start, end in queries:
            total = 0
            base = 0
            if start > 1:
                base = int(math.log2(start - 1) // 2)

            mul = base + 1
            beg = 4 ** (base + 1)

            if beg > end:
                ans += math.ceil(((end - start + 1) * mul) / 2.0)
                continue

            total += (beg - start) * mul

            while True:
                nxt = beg * 4
                mul += 1
                if nxt - 1 >= end:
                    total += (end - beg + 1) * mul
                    break
                else:
                    total += (nxt - beg) * mul
                beg *= 4

            ans += math.ceil(total / 2.0)

        return ans
