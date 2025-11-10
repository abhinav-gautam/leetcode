# https://leetcode.com/problems/minimum-distance-between-three-equal-elements-ii/description/

from typing import List


class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        indexMap = {}
        minDistance = float("inf")

        for i, x in enumerate(nums):
            indexMap.setdefault(x, []).append(i)

        for indices in indexMap.values():
            if len(indices) >= 3:
                for i in range(len(indices) - 2):
                    distance = (
                        abs(indices[i] - indices[i + 1])
                        + abs(indices[i + 1] - indices[i + 2])
                        + abs(indices[i + 2] - indices[i])
                    )
                    minDistance = min(minDistance, distance)

        if minDistance == float("inf"):
            return -1

        return minDistance


print(Solution().minimumDistance([1, 2, 1, 1, 3]))
print(Solution().minimumDistance([1, 1, 2, 3, 2, 1, 2]))
print(Solution().minimumDistance([1]))
print(Solution().minimumDistance([5, 3, 5, 5, 5]))
