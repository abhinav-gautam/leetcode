# https://leetcode.com/problems/happy-number/description/


# Hashmap approach
class Solution:
    def isHappy(self, n: int) -> bool:
        numsDict = set()

        while True:
            sum = 0
            while n:
                sum += (n % 10) ** 2
                n = n // 10

            n = sum
            if sum == 1:
                return True
            if sum in numsDict:
                return False
            numsDict.add(sum)


# Two pointer approach
class Solution:
    def sumOfSquareDigits(self, n: int) -> bool:
        sum = 0
        while n:
            sum += (n % 10) ** 2
            n = n // 10
        return sum

    def isHappy(self, n: int) -> bool:
        slow = self.sumOfSquareDigits(n)
        fast = self.sumOfSquareDigits(self.sumOfSquareDigits(n))

        while True:
            if slow == 1:
                return True
            if slow == fast:
                return False
            slow = self.sumOfSquareDigits(slow)
            fast = self.sumOfSquareDigits(self.sumOfSquareDigits(fast))


print(Solution().isHappy(19))
print(Solution().isHappy(2))
print(Solution().isHappy(7))
print(Solution().isHappy(1))
print(Solution().isHappy(3))
