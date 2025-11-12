# https://leetcode.com/problems/daily-temperatures/description/
from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        ans = [0] * len(temperatures)

        for index, temp in enumerate(temperatures):
            while stack and temp > temperatures[stack[-1]]:
                prev = stack.pop()
                ans[prev] = index - prev
            stack.append(index)

        return ans


print(Solution().dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73]))
print(Solution().dailyTemperatures([30, 40, 50, 60]))
print(Solution().dailyTemperatures([30, 60, 90]))
