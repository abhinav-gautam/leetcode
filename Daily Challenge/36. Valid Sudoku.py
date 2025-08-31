# https://leetcode.com/problems/valid-sudoku/description/?envType=daily-question&envId=2025-08-30


class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """

        rowMap = {i: [] for i in range(9)}
        columnMap = {i: [] for i in range(9)}
        squareMap = {(i, j): [] for i in range(3) for j in range(3)}

        for i in range(9):
            for j in range(9):
                num = board[i][j]
                square_i = i // 3
                square_j = j // 3
                if num == ".":
                    continue

                if num in rowMap[i]:
                    return False
                else:
                    rowMap[i].append(num)

                if num in columnMap[j]:
                    return False
                else:
                    columnMap[j].append(num)

                if num in squareMap[(square_i, square_j)]:
                    return False
                else:
                    squareMap[(square_i, square_j)].append(num)
        return True


print(
    Solution().isValidSudoku(
        board=[
            ["5", "3", ".", ".", "7", ".", ".", ".", "."],
            ["6", ".", ".", "1", "9", "5", ".", ".", "."],
            [".", "9", "8", ".", ".", ".", ".", "6", "."],
            ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
            ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
            ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
            [".", "6", ".", ".", ".", ".", "2", "8", "."],
            [".", ".", ".", "4", "1", "9", ".", ".", "5"],
            [".", ".", ".", ".", "8", ".", ".", "7", "9"],
        ]
    )
)
