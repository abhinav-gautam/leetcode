# https://leetcode.com/problems/find-the-number-of-ways-to-place-people-i/description/?envType=daily-question&envId=2025-09-02


class Solution:
    def numberOfPairs(self, points: list[list[int]]) -> int:
        n = len(points)
        count = 0

        for i in range(n):
            x1, y1 = points[i]
            for j in range(n):
                if i == j:
                    continue
                x2, y2 = points[j]

                if x1 > x2 or y1 < y2:
                    continue

                flag = True
                for k in range(n):
                    if k == i or k == j:
                        continue
                    x, y = points[k]
                    if x >= x1 and x <= x2 and y <= y1 and y >= y2:
                        flag = False
                        break

                if flag:
                    count += 1

        return count


print(Solution().numberOfPairs([[3, 1], [1, 3], [1, 1]]))
print(Solution().numberOfPairs([[1, 1], [2, 2], [3, 3]]))
print(Solution().numberOfPairs([[6, 2], [4, 4], [2, 6]]))
print(Solution().numberOfPairs([[0, 1], [1, 3], [6, 1]]))
