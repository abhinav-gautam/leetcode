# https://leetcode.com/problems/check-if-digits-are-equal-in-string-after-operations-i/?envType=daily-question&envId=2025-10-23


class Solution:
    def hasSameDigits(self, s: str) -> bool:
        while len(s) > 2:
            new = ""
            for i in range(1, len(s)):
                new += str(((int(s[i - 1]) + int(s[i])) % 10))
            s = new

        return s[0] == s[1]


print(Solution().hasSameDigits("3902"))
