# https://leetcode.com/problems/maximum-total-damage-with-spell-casting/description/?envType=daily-question&envId=2025-10-11

from typing import List
from collections import Counter


class Solution:
    def maximumTotalDamage(self, power: List[int]) -> int:
        freq = Counter(power)
        keys = sorted(freq)
        n = len(keys)

        dp = [0] * n
        dp[0] = freq[keys[0]] * keys[0]

        for i in range(1, n):
            take = freq[keys[i]] * keys[i]
            left, right, ans = 0, i - 1, -1
            while left <= right:
                mid = (left + right) // 2
                if keys[mid] <= keys[i] - 3:
                    ans = mid
                    left = mid + 1
                else:
                    right = mid - 1
            if ans >= 0:
                take += dp[ans]
            dp[i] = max(dp[i - 1], take)

        return dp[-1]


print(Solution().maximumTotalDamage([1, 1, 3, 4]))
print(Solution().maximumTotalDamage([7, 1, 6, 6]))
