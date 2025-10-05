# https://leetcode.com/problems/water-bottles-ii/?envType=daily-question&envId=2025-10-02


class Solution:
    def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:
        drink = 0
        while numBottles > 0:
            if numBottles >= numExchange:
                drink += numExchange
                numBottles += 1 - numExchange
                numExchange += 1
            else:
                drink += numBottles
                break
        return drink
