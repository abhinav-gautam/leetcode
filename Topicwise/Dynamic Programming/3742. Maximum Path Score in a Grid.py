# https://leetcode.com/problems/maximum-path-score-in-a-grid/
from typing import List


class Solution:
    def maxPathScore(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])

        score = [[0] * n for _ in range(m)]
        cost = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    score[i][j] = 1
                    cost[i][j] = 1
                elif grid[i][j] == 2:
                    score[i][j] = 2
                    cost[i][j] = 1

        NEG_INF = float("-inf")
        dp = [[[NEG_INF] * (k + 1) for _ in range(n)] for _ in range(m)]

        if cost[0][0] <= k:
            dp[0][0][cost[0][0]] = score[0][0]

        for i in range(m):
            for j in range(n):
                for c in range(cost[i][j], k + 1):
                    val = NEG_INF
                    if i > 0 and dp[i - 1][j][c - cost[i][j]] != NEG_INF:
                        val = max(val, dp[i - 1][j][c - cost[i][j]] + score[i][j])
                    if j > 0 and dp[i][j - 1][c - cost[i][j]] != NEG_INF:
                        val = max(val, dp[i][j - 1][c - cost[i][j]] + score[i][j])
                    dp[i][j][c] = max(dp[i][j][c], val)

        ans = max(dp[m - 1][n - 1])
        return ans if ans != NEG_INF else -1
