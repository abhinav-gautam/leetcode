from typing import List


class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        m = len(mat)
        n = len(mat[0])

        rows = {}
        cols = {}
        result = 0

        for i in range(m):
            for j in range(n):
                if i in rows:
                    rows[i] += mat[i][j]
                else:
                    rows[i] = mat[i][j]

                if j in cols:
                    cols[j] += mat[i][j]
                else:
                    cols[j] = mat[i][j]

        for i in range(m):
            for j in range(n):
                if mat[i][j] == 1 and rows[i] == 1 and cols[j] == 1:
                    result += 1

        return result


print(Solution().numSpecial([[1, 0, 0], [0, 0, 1], [1, 0, 0]]))
print(Solution().numSpecial([[1, 0, 0], [0, 1, 0], [0, 0, 1]]))
