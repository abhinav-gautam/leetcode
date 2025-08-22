# https://leetcode.com/problems/find-the-minimum-area-to-cover-all-ones-i/description/?envType=daily-question&envId=2025-08-22


class Solution(object):
    def minimumArea(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        minB = minL = float("inf")
        maxB = maxL = float("-inf")

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1:
                    minB = min(minB, i)
                    maxB = max(maxB, i)
                    minL = min(minL, j)
                    maxL = max(maxL, j)
        return (maxL - minL + 1) * (maxB - minB + 1)


print(Solution().minimumArea([[0, 1, 0], [1, 0, 1]]))
print(Solution().minimumArea([[1, 0], [0, 0]]))
