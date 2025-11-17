# https://leetcode.com/problems/number-of-substrings-with-only-1s/description/?envType=daily-question&envId=2025-11-16


class Solution:
    def numSub(self, s: str) -> int:
        total = 0
        mod = 10**9 + 7
        current = 0

        for char in s:
            if char == "1":
                current += 1
            else:
                total += current * (current + 1) // 2
                current = 0
        if current:
            total += current * (current + 1) // 2

        return total % mod


print(Solution().numSub("0110111"))
print(Solution().numSub("101"))
print(Solution().numSub("111111"))
