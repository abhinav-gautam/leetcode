# https://leetcode.com/problems/increment-submatrices-by-one/description/?envType=daily-question&envId=2025-11-14
from typing import List


# Brute force
class Solution:
    def rangeAddQueries(self, n: int, queries: List[List[int]]) -> List[List[int]]:
        matrix = [[0 for _ in range(n)] for _ in range(n)]
        for query in queries:
            row1, col1, row2, col2 = query
            for i in range(row1, row2 + 1):
                for j in range(col1, col2 + 1):
                    matrix[i][j] += 1

        return matrix


# 2D difference array
class Solution:
    def rangeAddQueries(self, n: int, queries: List[List[int]]) -> List[List[int]]:
        matrix = [[0] * (n) for _ in range(n)]

        for query in queries:
            row1, col1, row2, col2 = query

            matrix[row1][col1] += 1
            if col2 + 1 < n:
                matrix[row1][col2 + 1] -= 1
            if row2 + 1 < n:
                matrix[row2 + 1][col1] -= 1
            if row2 + 1 < n and col2 + 1 < n:
                matrix[row2 + 1][col2 + 1] += 1

        for i in range(n):
            for j in range(n):
                top = 0
                left = 0
                diagonal = 0

                if i > 0:
                    top = matrix[i - 1][j]
                if j > 0:
                    left = matrix[i][j - 1]
                if i > 0 and j > 0:
                    diagonal = matrix[i - 1][j - 1]

                matrix[i][j] += top + left - diagonal
        return matrix


print(Solution().rangeAddQueries(n=3, queries=[[1, 1, 2, 2], [0, 0, 1, 1]]))
