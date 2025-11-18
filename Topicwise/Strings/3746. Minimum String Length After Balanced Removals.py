# https://leetcode.com/problems/minimum-string-length-after-balanced-removals/description/


class Solution:
    def minLengthAfterRemovals(self, s: str) -> int:
        a = s.count("a")
        b = s.count("b")

        return abs(a - b)


print(Solution().minLengthAfterRemovals("aabbab"))
