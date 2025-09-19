# https://leetcode.com/problems/design-spreadsheet/description/?envType=daily-question&envId=2025-09-19


class Spreadsheet:

    def __init__(self, rows: int):
        self.spreadSheet = {}

    def setCell(self, cell: str, value: int) -> None:
        self.spreadSheet[cell] = value

    def resetCell(self, cell: str) -> None:
        self.spreadSheet[cell] = 0

    def getValue(self, formula: str) -> int:
        x = formula.split("+")[0][1:]
        y = formula.split("+")[1]

        if x[0].isalpha():
            x = self.spreadSheet.get(x, 0)
        else:
            x = int(x)

        if y[0].isalpha():
            y = self.spreadSheet.get(y, 0)
        else:
            y = int(y)

        return x + y


Spreadsheet(4).getValue("=X+Y")
