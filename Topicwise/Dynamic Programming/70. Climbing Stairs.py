# https://leetcode.com/problems/climbing-stairs/description/


class Solution:
    def climbStairs(self, n: int) -> int:
        # f(n) = f(n-1) + f(n-2)
        if n < 3:
            return n

        prev1 = 2
        prev2 = 1
        current = 0

        for _ in range(3, n + 1):
            current = prev1 + prev2
            prev2 = prev1
            prev1 = current

        return current


print(Solution().climbStairs(2))
print(Solution().climbStairs(4))
