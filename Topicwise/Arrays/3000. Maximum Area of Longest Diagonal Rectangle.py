# https://leetcode.com/problems/maximum-area-of-longest-diagonal-rectangle/description/?envType=daily-question&envId=2025-08-26
import math


class Solution(object):
    def areaOfMaxDiagonal(self, dimensions):
        """
        :type dimensions: List[List[int]]
        :rtype: int
        """

        maxArea = 0
        maxDiagonal = 0

        for dimension in dimensions:
            diagonal = math.sqrt(dimension[0] ** 2 + dimension[1] ** 2)
            area = dimension[0] * dimension[1]
            if diagonal > maxDiagonal:
                maxDiagonal = diagonal
                maxArea = area
            elif diagonal == maxDiagonal:
                maxArea = max(area, maxArea)
        return maxArea


print(Solution().areaOfMaxDiagonal([[9, 3], [8, 6]]))
print(Solution().areaOfMaxDiagonal([[3, 4], [4, 3]]))
