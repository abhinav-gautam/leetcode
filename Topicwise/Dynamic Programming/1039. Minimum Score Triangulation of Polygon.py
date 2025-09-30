# https://leetcode.com/problems/minimum-score-triangulation-of-polygon/description/?envType=daily-question&envId=2025-09-29
from typing import List


class Solution:
    def minScoreTriangulation(self, values: List[int]) -> int:
        n = len(values)
        memo = [[float("inf")] * n for _ in range(n)]

        def dfs(i, j):
            if j - i < 2:
                return 0
            if memo[i][j] != float("inf"):
                return memo[i][j]
            res = []
            for k in range(i + 1, j):
                res.append(values[i] * values[j] * values[k] + dfs(i, k) + dfs(k, j))
            memo[i][j] = min(res)
            return memo[i][j]

        return dfs(0, n - 1)


print(Solution().minScoreTriangulation([1, 2, 3]))
