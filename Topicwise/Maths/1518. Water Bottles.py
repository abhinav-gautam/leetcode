# https://leetcode.com/problems/water-bottles/description/?envType=daily-question&envId=2025-10-01


class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        empty = numBottles
        drink = numBottles
        while empty >= numExchange:
            d = empty // numExchange
            drink += d
            empty = d + empty % numExchange
        return drink


print(Solution().numWaterBottles(9, 3))
print(Solution().numWaterBottles(15, 4))
