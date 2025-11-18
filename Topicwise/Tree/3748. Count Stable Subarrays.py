# https://leetcode.com/problems/count-stable-subarrays/description/

from typing import List
import bisect


class Fenwick:
    def __init__(self, n: int):
        self.n = n
        self.bit = [0] * (n + 1)

    def add(self, i: int, delta: int):
        while i <= self.n:
            self.bit[i] += delta
            i += i & -i

    def sum(self, i: int) -> int:
        s = 0
        while i > 0:
            s += self.bit[i]
            i -= i & -i
        return s

    def range_sum(self, l: int, r: int) -> int:
        if r < l:
            return 0
        return self.sum(r) - self.sum(l - 1)


class Solution:
    def countStableSubarrays(
        self, nums: List[int], queries: List[List[int]]
    ) -> List[int]:
        n = len(nums)
        reach = [0] * n
        reach[-1] = n - 1
        for i in range(n - 2, -1, -1):
            if nums[i] <= nums[i + 1]:
                reach[i] = reach[i + 1]
            else:
                reach[i] = i

        idx_by_reach = list(range(n))
        idx_by_reach.sort(key=lambda i: reach[i])

        qlist = []
        for qi, (l, r) in enumerate(queries):
            qlist.append((r, l, qi))
        qlist.sort()

        bit_count = Fenwick(n)
        bit_len = Fenwick(n)
        bit_idx = Fenwick(n)

        ans = [0] * len(queries)
        ptr = 0

        for R, L, qi in qlist:
            while ptr < n and reach[idx_by_reach[ptr]] < R:
                i = idx_by_reach[ptr]
                pos = i + 1
                length_i = reach[i] - i + 1
                bit_count.add(pos, 1)
                bit_len.add(pos, length_i)
                bit_idx.add(pos, pos)
                ptr += 1

            Lpos = L + 1
            Rpos = R + 1

            c2 = bit_count.range_sum(Lpos, Rpos)
            sum_len_case2 = bit_len.range_sum(Lpos, Rpos)
            sum_idx_case2 = bit_idx.range_sum(Lpos, Rpos)

            total_positions = R - L + 1
            c1 = total_positions - c2

            sum_indices_total = (Lpos + Rpos) * total_positions // 2
            sum_indices_case1 = sum_indices_total - sum_idx_case2

            sum_case1 = c1 * (R + 1) - (sum_indices_case1 - c1)

            ans[qi] = sum_case1 + sum_len_case2

        return ans
