# https://leetcode.com/problems/find-n-unique-integers-sum-up-to-zero/?envType=daily-question&envId=2025-09-07


class Solution:
    def sumZero(self, n: int) -> list[int]:
        sum = 0
        result = []
        for i in range(1, n):
            result.append(i)
            sum += i
        result.append(-sum)
        return result
