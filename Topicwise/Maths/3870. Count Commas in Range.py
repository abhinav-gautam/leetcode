# https://leetcode.com/problems/count-commas-in-range/description/


class Solution:
    def countCommas(self, n: int) -> int:
        commas = 0
        start = 1000
        comma_count = 1

        while start <= n:
            end = start * 1000 - 1
            count = max(0, min(n, end) - start + 1)
            commas += count * comma_count

            start *= 1000
            comma_count += 1

        return commas


print(Solution().countCommas(1002))
