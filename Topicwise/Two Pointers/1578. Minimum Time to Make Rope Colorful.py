# https://leetcode.com/problems/minimum-time-to-make-rope-colorful/description/?envType=daily-question&envId=2025-11-03

from typing import List


class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        i, j = 0, 1
        totalTime = 0
        while j < len(colors):
            if colors[i] == colors[j]:
                maxT = t = neededTime[i]
                while j < len(colors) and colors[i] == colors[j]:
                    maxT = max(maxT, neededTime[j])
                    t += neededTime[j]
                    j += 1
                totalTime += t - maxT
            i = j
            j += 1
        return totalTime


print(Solution().minCost(colors="abaac", neededTime=[1, 2, 3, 4, 5]))
print(Solution().minCost(colors="abc", neededTime=[1, 2, 3]))
print(Solution().minCost(colors="aabaa", neededTime=[1, 2, 3, 4, 1]))
