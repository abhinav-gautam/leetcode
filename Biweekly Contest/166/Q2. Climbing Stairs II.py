# https://leetcode.com/contest/biweekly-contest-166/problems/climbing-stairs-ii/description/

from typing import List


class Solution:
    def climbStairs(self, n: int, costs: List[int]) -> int:
        n = len(costs)
        dp = [float("inf")] * (n + 1)
        dp[0] = 0

        for i in range(1, n + 1):
            for jump in (1, 2, 3):
                j = i - jump
                if j >= 0:
                    dp[i] = min(dp[i], dp[j] + costs[i - 1] + jump * jump)

        return dp[n]
