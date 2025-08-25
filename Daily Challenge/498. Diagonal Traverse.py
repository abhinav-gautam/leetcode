# https://leetcode.com/problems/diagonal-traverse/description/?envType=daily-question&envId=2025-08-25


class Solution(object):
    def findDiagonalOrder(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[int]
        """
        i = j = 0
        result = []
        inc = "j"
        m = len(mat)
        n = len(mat[0])
        while True:
            if len(result) == m * n:
                break
            result.append(mat[i][j])
            if inc == "j":
                if j + 1 < n:
                    j += 1
                else:
                    i += 1
                    inc = "i"
                    continue
                if i - 1 < 0:
                    inc = "i"
                    continue
                i -= 1
            if inc == "i":
                if i + 1 < m:
                    i += 1
                else:
                    j += 1
                    inc = "j"
                    continue
                if j - 1 < 0:
                    inc = "j"
                    continue
                j -= 1
        return result


print(Solution().findDiagonalOrder([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
print(Solution().findDiagonalOrder([[1, 2], [3, 4]]))
