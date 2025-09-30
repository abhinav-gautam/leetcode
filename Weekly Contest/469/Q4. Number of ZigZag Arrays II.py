# https://leetcode.com/contest/weekly-contest-469/problems/number-of-zigzag-arrays-ii/description/


class Solution:
    def zigZagArrays(self, n: int, l: int, r: int) -> int:
        MOD = 10**9 + 7
        m = r - l + 1
        if n == 1:
            return m % MOD
        dp_up = [0] * m
        dp_down = [0] * m
        for j in range(m):
            dp_up[j] = j % MOD
            dp_down[j] = (m - 1 - j) % MOD
        for _ in range(3, n + 1):
            new_up = [0] * m
            new_down = [0] * m
            prefix_up = [0] * (m + 1)
            prefix_down = [0] * (m + 1)
            for j in range(m):
                prefix_up[j + 1] = (prefix_up[j] + dp_up[j]) % MOD
                prefix_down[j + 1] = (prefix_down[j] + dp_down[j]) % MOD
            total_up = prefix_up[m]
            for j in range(m):
                new_up[j] = prefix_down[j] % MOD
                new_down[j] = (total_up - prefix_up[j + 1]) % MOD
            dp_up, dp_down = new_up, new_down
        return (sum(dp_up) + sum(dp_down)) % MOD


print(Solution().zigZagArrays(3, 4, 5))
