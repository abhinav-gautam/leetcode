# https://leetcode.com/contest/weekly-contest-469/problems/number-of-zigzag-arrays-i/


class Solution:
    def zigZagArrays(self, n: int, l: int, r: int) -> int:
        MOD = 10**9 + 7
        m = r - l + 1

        dp_up = [0] * m
        dp_down = [0] * m

        for i in range(m):
            for j in range(m):
                if i < j:
                    dp_up[j] = (dp_up[j] + 1) % MOD
                elif i > j:
                    dp_down[j] = (dp_down[j] + 1) % MOD

        for length in range(3, n + 1):
            new_up = [0] * m
            new_down = [0] * m

            prefix_up = [0] * (m + 1)
            prefix_down = [0] * (m + 1)
            for j in range(m):
                prefix_up[j + 1] = (prefix_up[j] + dp_up[j]) % MOD
                prefix_down[j + 1] = (prefix_down[j] + dp_down[j]) % MOD

            for j in range(m):
                if dp_up[j]:
                    new_down[:j] = [(new_down[x] + dp_up[j]) % MOD for x in range(j)]

                if dp_down[j]:
                    new_up[j + 1 :] = [
                        (new_up[x] + dp_down[j]) % MOD for x in range(j + 1, m)
                    ]

            dp_up, dp_down = new_up, new_down

        return (sum(dp_up) + sum(dp_down)) % MOD
