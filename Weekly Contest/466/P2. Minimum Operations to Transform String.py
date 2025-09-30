# https://leetcode.com/contest/weekly-contest-466/problems/minimum-operations-to-transform-string/description/


class Solution:
    def minOperations(self, s: str) -> int:
        s = "".join(sorted([c for c in s]))
        ops = 0
        for i in range(len(s)):
            if s[i] == "a":
                continue

            if i == len(s) - 1:
                ops += ord("z") - ord(s[i]) + 1
                break

            ops = ops + ord(s[i + 1]) - ord(s[i])

        return ops


print(Solution().minOperations("gveqwv"))
print(Solution().minOperations("yz"))
print(Solution().minOperations("a"))
