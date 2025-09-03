# https://leetcode.com/problems/find-the-number-of-ways-to-place-people-ii/description/?envType=daily-question&envId=2025-09-03


class Solution:
    def numberOfPairs(self, points: list[list[int]]) -> int:
        points.sort(key=lambda x: (-x[0], x[1]))
        n = len(points)
        count = 0

        for i in range(n - 1):
            y1 = points[i][1]
            yMax = float("inf")
            for j in range(i + 1, n):
                y2 = points[j][1]

                if yMax > y2 and y2 >= y1:
                    count += 1
                    yMax = y2
                    if y1 == y2:
                        break

        return count


print(Solution().numberOfPairs([[3, 1], [1, 3], [1, 1]]))
