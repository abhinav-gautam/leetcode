# https://leetcode.com/problems/max-area-of-island/description/

from typing import List


class Solution:
    def dfs(self, grid, row, col):
        if (
            row < 0
            or row >= len(grid)
            or col < 0
            or col >= len(grid[0])
            or grid[row][col] == 0
        ):
            return 0

        grid[row][col] = 0

        area = 1

        area += self.dfs(grid, row - 1, col)
        area += self.dfs(grid, row + 1, col)
        area += self.dfs(grid, row, col - 1)
        area += self.dfs(grid, row, col + 1)

        return area

    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxArea = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    area = self.dfs(grid, i, j)
                    maxArea = max(maxArea, area)
        return maxArea
