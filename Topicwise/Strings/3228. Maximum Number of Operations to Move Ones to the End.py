# https://leetcode.com/problems/maximum-number-of-operations-to-move-ones-to-the-end/description/?envType=daily-question&envId=2025-11-13


class Solution:
    def maxOperations(self, s: str) -> int:
        count = 0
        ones = 0

        for i in range(len(s) - 1):
            if s[i] == "1":
                ones += 1
                if s[i + 1] == "0":
                    count += ones
        return count


print(Solution().maxOperations("1001101"))
print(Solution().maxOperations("00111"))
