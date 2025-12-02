# https://leetcode.com/problems/fibonacci-number/description/


class Solution:
    def fib(self, n: int) -> int:
        if n < 2:
            return n

        prev1 = 1
        prev2 = 0

        current = 0

        for _ in range(2, n + 1):
            current = prev1 + prev2
            prev2 = prev1
            prev1 = current

        return current
