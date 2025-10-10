# https://leetcode.com/problems/taking-maximum-energy-from-the-mystic-dungeon/description/?envType=daily-question&envId=2025-10-10

from typing import List


class Solution:
    def maximumEnergy(self, energy: List[int], k: int) -> int:
        n = len(energy)
        dp = [0] * n

        for i in range(n - 1, -1, -1):
            if i + k >= n:
                dp[i] = energy[i]
            else:
                dp[i] = energy[i] + dp[i + k]

        return max(dp)


print(Solution().maximumEnergy(energy=[5, 2, -10, -5, 1], k=3))
print(Solution().maximumEnergy(energy=[-2, -3, -1], k=2))
