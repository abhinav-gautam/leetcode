# https://leetcode.com/problems/flood-fill/description/

from typing import List


class Solution:
    def floodFill(
        self, image: List[List[int]], sr: int, sc: int, color: int
    ) -> List[List[int]]:
        original = image[sr][sc]

        if original == color:
            return image

        def dfs(image, row, col):
            if (
                row < 0
                or row >= len(image)
                or col < 0
                or col >= len(image[0])
                or image[row][col] != original
            ):
                return image

            image[row][col] = color

            dfs(image, row - 1, col)
            dfs(image, row + 1, col)
            dfs(image, row, col - 1)
            dfs(image, row, col + 1)

            return image

        return dfs(image, sr, sc)


print(
    Solution().floodFill(image=[[1, 1, 1], [1, 1, 0], [1, 0, 1]], sr=1, sc=1, color=2)
)
print(Solution().floodFill(image=[[0, 0, 0], [0, 0, 0]], sr=0, sc=0, color=0))
