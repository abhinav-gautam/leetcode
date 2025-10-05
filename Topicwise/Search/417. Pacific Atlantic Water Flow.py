# https://leetcode.com/problems/pacific-atlantic-water-flow/description/?envType=daily-question&envId=2025-10-05

from typing import List


class Solution:
    def dfs(self, x, y, visited):
        directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        visited.add((x, y))
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < self.m and 0 <= ny < self.n:
                if (nx, ny) not in visited and self.heights[x][y] <= self.heights[nx][
                    ny
                ]:
                    self.dfs(nx, ny, visited)

    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        self.m = len(heights)
        self.n = len(heights[0])
        self.heights = heights
        pacific, atlantic = set(), set()

        for i in range(self.n):
            self.dfs(0, i, pacific)
            self.dfs(self.m - 1, i, atlantic)
        for i in range(self.m):
            self.dfs(i, 0, pacific)
            self.dfs(i, self.n - 1, atlantic)

        return list(pacific.intersection(atlantic))


print(
    Solution().pacificAtlantic(
        [
            [1, 2, 2, 3, 5],
            [3, 2, 3, 4, 4],
            [2, 4, 5, 3, 1],
            [6, 7, 1, 4, 5],
            [5, 1, 1, 2, 4],
        ]
    )
)
print(Solution().pacificAtlantic([[1, 1], [1, 1], [1, 1]]))
