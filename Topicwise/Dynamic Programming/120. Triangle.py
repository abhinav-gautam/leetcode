# https://leetcode.com/problems/triangle/description/?envType=daily-question&envId=2025-09-25

from typing import List


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        for i in range(1, len(triangle)):
            for j in range(len(triangle[i])):
                if j >= len(triangle[i - 1]):
                    parent = float("inf")
                else:
                    parent = triangle[i - 1][j]
                if j - 1 < 0:
                    adjacentParent = float("inf")
                else:
                    adjacentParent = triangle[i - 1][j - 1]
                minDistance = min(
                    parent + triangle[i][j],
                    adjacentParent + triangle[i][j],
                )
                triangle[i][j] = minDistance
        return min(triangle[len(triangle) - 1])


print(Solution().minimumTotal([[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]]))
print(Solution().minimumTotal([[-10]]))
