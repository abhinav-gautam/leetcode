# https://leetcode.com/problems/count-number-of-trapezoids-i/description/?envType=daily-question&envId=2025-12-02
from typing import List


class Solution:
    def countTrapezoids(self, points: List[List[int]]) -> int:
        coords = {}
        MOD = 10**9 + 7
        total = 0
        for _, y in points:
            if y in coords:
                coords[y] += 1
            else:
                coords[y] = 1

        values = list(coords.values())
        first = values[0]
        sum = first * (first - 1) // 2

        for i in range(1, len(values)):
            current = values[i]
            if current > 1:
                currentSum = current * (current - 1) // 2
                total += sum * currentSum
                sum += currentSum

        return total % MOD


print(Solution().countTrapezoids([[1, 0], [2, 0], [3, 0], [2, 2], [3, 2]]))
print(Solution().countTrapezoids([[0, 0], [1, 0], [0, 1], [2, 1]]))
print(Solution().countTrapezoids([[87, -39], [12, -94], [-30, -11], [-76, -11]]))
print(
    Solution().countTrapezoids(
        [[-73, -72], [-1, -56], [-92, 30], [-57, -89], [-19, -89], [-35, 30], [64, -72]]
    )
)
