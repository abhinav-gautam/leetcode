# https://leetcode.com/problems/minimum-cost-to-split-into-ones/description/


class Solution:
    def minCost(self, n: int) -> int:
        costMap = {1: 0, 2: 1}

        for i in range(3, n + 1):
            if i % 2 == 0:
                a = i // 2
                costMap[i] = (a**2) + (costMap[a] * 2)
            else:
                a = i // 2
                b = i - a
                costMap[i] = (a * b) + costMap[a] + costMap[b]

        return costMap[n]


print(Solution().minCost(2))
print(Solution().minCost(3))
print(Solution().minCost(4))
print(Solution().minCost(5))
print(Solution().minCost(6))
