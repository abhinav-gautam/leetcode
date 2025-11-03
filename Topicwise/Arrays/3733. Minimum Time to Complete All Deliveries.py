# https://leetcode.com/problems/minimum-time-to-complete-all-deliveries/description/

from typing import List
from math import gcd


class Solution:

    def minimumTime(self, d: List[int], r: List[int]) -> int:
        d1, d2 = d
        r1, r2 = r

        def lcm(a, b):
            return a // gcd(a, b) * b

        lo = d1 + d2
        hi = lo
        while True:
            hi *= 2
            t = hi
            l = lcm(r1, r2)
            avail1 = t - (t // r1)
            avail2 = t - (t // r2)
            union_avail = t - (t // l)
            if avail1 >= d1 and avail2 >= d2 and union_avail >= d1 + d2:
                break

        lbound, rbound = lo, hi
        while lbound < rbound:
            mid = (lbound + rbound) // 2
            l = lcm(r1, r2)
            avail1 = mid - (mid // r1)
            avail2 = mid - (mid // r2)
            union_avail = mid - (mid // l)
            if avail1 >= d1 and avail2 >= d2 and union_avail >= d1 + d2:
                rbound = mid
            else:
                lbound = mid + 1

        return lbound


print(Solution().minimumTime(d=[3, 1], r=[2, 3]))
print(Solution().minimumTime(d=[2, 2], r=[3, 4]))
print(Solution().minimumTime(d=[1, 1], r=[3, 2]))
