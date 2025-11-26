# https://leetcode.com/problems/number-of-islands/description/

from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])

        def dfs(grid, row, col):
            if row >= m or row < 0 or col >= n or col < 0 or grid[row][col] == "0":
                return 0

            grid[row][col] = "0"

            dfs(grid, row + 1, col)
            dfs(grid, row, col + 1)
            dfs(grid, row - 1, col)
            dfs(grid, row, col - 1)

            return 1

        count = 0
        for i in range(m):
            for j in range(n):
                count += dfs(grid, i, j)

        return count


print(
    Solution().numIslands(
        grid=[
            ["1", "1", "1", "1", "0"],
            ["1", "1", "0", "1", "0"],
            ["1", "1", "0", "0", "0"],
            ["0", "0", "0", "0", "0"],
        ]
    )
)

print(
    Solution().numIslands(
        grid=[
            ["1", "1", "0", "0", "0"],
            ["1", "1", "0", "0", "0"],
            ["0", "0", "1", "0", "0"],
            ["0", "0", "0", "1", "1"],
        ]
    )
)
