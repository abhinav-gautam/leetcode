# https://leetcode.com/problems/count-unguarded-cells-in-the-grid/description/?envType=daily-question&envId=2025-11-02
from typing import List


class Solution:
    def countUnguarded(
        self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]
    ) -> int:
        wallsSet = set()
        guardSet = set()
        for wall in walls:
            wallsSet.add((wall[0], wall[1]))
        for guard in guards:
            guardSet.add((guard[0], guard[1]))

        visibleSet = set()
        for guard in guards:
            # Horizontal - right
            for i in range(guard[1], n):
                if (guard[0], i) in wallsSet or (
                    guard[1] != i and (guard[0], i) in guardSet
                ):
                    break
                visibleSet.add((guard[0], i))
            # Horizontal - left
            for i in range(guard[1], -1, -1):
                if (guard[0], i) in wallsSet or (
                    guard[1] != i and (guard[0], i) in guardSet
                ):
                    break
                visibleSet.add((guard[0], i))
            # Vertical - down
            for i in range(guard[0], m):
                if (i, guard[1]) in wallsSet or (
                    guard[0] != i and (i, guard[1]) in guardSet
                ):
                    break
                visibleSet.add((i, guard[1]))
            # Vertical - up
            for i in range(guard[0], -1, -1):
                if (i, guard[1]) in wallsSet or (
                    guard[0] != i and (i, guard[1]) in guardSet
                ):
                    break
                visibleSet.add((i, guard[1]))
        return (m * n) - len(visibleSet) - len(walls)


print(
    Solution().countUnguarded(
        m=4, n=6, guards=[[0, 0], [1, 1], [2, 3]], walls=[[0, 1], [2, 2], [1, 4]]
    )
)
