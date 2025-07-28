# https://leetcode.com/problems/zigzag-conversion/description/


class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """

        final = ""
        if numRows == 1:
            return s

        for currentRow in range(numRows):
            i = currentRow
            while i < len(s):
                if (numRows - currentRow - 1) * 2 != 0:
                    final += s[i]
                    i += (numRows - currentRow - 1) * 2
                if currentRow != 0 and i < len(s):
                    final += s[i]
                    i += currentRow * 2
        return final


print(Solution().convert("PAYPALISHIRING", 3))
print(Solution().convert("PAYPALISHIRING", 4))
print(Solution().convert("A", 1))
