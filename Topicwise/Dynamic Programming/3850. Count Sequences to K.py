# https://leetcode.com/problems/count-sequences-to-k/description/

from collections import defaultdict
from fractions import Fraction


class Solution:
    def countSequences(self, nums: List[int], k: int) -> int:
        dp = defaultdict(int)
        dp[Fraction(1, 1)] = 1

        for num in nums:
            next_dp = defaultdict(int)

            for val, count in dp.items():
                next_dp[val * num] += count

                next_dp[val / num] += count

                next_dp[val] += count

            dp = next_dp

        return dp[Fraction(k, 1)]
