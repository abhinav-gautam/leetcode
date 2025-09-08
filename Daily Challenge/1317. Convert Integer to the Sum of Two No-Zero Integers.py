# https://leetcode.com/problems/convert-integer-to-the-sum-of-two-no-zero-integers/description/?envType=daily-question&envId=2025-09-08


class Solution:
    def isZeroInteger(self, num):
        return "0" in str(num)

    def getNoZeroIntegers(self, n: int) -> list[int]:

        for i in range(n):
            compliment = n - i

            if self.isZeroInteger(i) or self.isZeroInteger(compliment):
                continue

            return [i, compliment]


print(Solution().getNoZeroIntegers(11))
print(Solution().getNoZeroIntegers(2))
