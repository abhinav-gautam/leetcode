# https://leetcode.com/problems/smallest-number-with-all-set-bits/description/?envType=daily-question&envId=2025-10-29


class Solution:
    def smallestNumber(self, n: int) -> int:
        length = len(bin(n).split("b")[1])
        return int("1" * length, 2)


print(Solution().smallestNumber(5))
