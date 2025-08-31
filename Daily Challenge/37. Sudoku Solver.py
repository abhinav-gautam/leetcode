# https://leetcode.com/problems/sudoku-solver/description/?envType=daily-question&envId=2025-08-31


class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        self.board = board
        self.rowMap = {i: [] for i in range(9)}
        self.columnMap = {i: [] for i in range(9)}
        self.squareMap = {(i, j): [] for i in range(3) for j in range(3)}

        for i in range(9):
            for j in range(9):
                if self.board[i][j] != ".":
                    num = int(self.board[i][j])
                    self.addMap(i, j, num)

        print(self.solve(0, 0))
        print(self.board)

    def addMap(self, row, col, num):
        self.rowMap[row].append(num)
        self.columnMap[col].append(num)
        self.squareMap[(row // 3, col // 3)].append(num)

    def removeMap(self, row, col, num):
        self.rowMap[row].remove(num)
        self.columnMap[col].remove(num)
        self.squareMap[(row // 3, col // 3)].remove(num)

    def isValidEntry(self, row, col, num):
        if (
            num in self.rowMap[row]
            or num in self.columnMap[col]
            or num in self.squareMap[(row // 3, col // 3)]
        ):
            return False
        return True

    def solve(self, row, col):
        if col == 9:
            row += 1
            col = 0

        if row == 9:
            return True

        if self.board[row][col] != ".":
            return self.solve(row, col + 1)

        for i in range(1, 10):
            if self.isValidEntry(row, col, i):
                self.board[row][col] = str(i)
                self.addMap(row, col, i)

                if self.solve(row, col + 1):
                    return True

                self.board[row][col] = "."
                self.removeMap(row, col, i)
        return False


Solution().solveSudoku(
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

Solution().solveSudoku(
    board=[
        [".", ".", ".", ".", ".", ".", ".", ".", "."],
        [".", "9", ".", ".", "1", ".", ".", "3", "."],
        [".", ".", "6", ".", "2", ".", "7", ".", "."],
        [".", ".", ".", "3", ".", "4", ".", ".", "."],
        ["2", "1", ".", ".", ".", ".", ".", "9", "8"],
        [".", ".", ".", ".", ".", ".", ".", ".", "."],
        [".", ".", "2", "5", ".", "6", "4", ".", "."],
        [".", "8", ".", ".", ".", ".", ".", "1", "."],
        [".", ".", ".", ".", ".", ".", ".", ".", "."],
    ]
)
