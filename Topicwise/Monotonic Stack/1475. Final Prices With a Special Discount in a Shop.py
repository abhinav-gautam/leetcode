# https://leetcode.com/problems/final-prices-with-a-special-discount-in-a-shop/description/

from typing import List


class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        stack = []

        for index, price in enumerate(prices):
            while stack and price <= prices[stack[-1]]:
                prev = stack.pop()
                prices[prev] -= price
            stack.append(index)

        return prices


print(Solution().finalPrices([8, 4, 6, 2, 3]))
print(Solution().finalPrices([1, 2, 3, 4, 5]))
print(Solution().finalPrices([10, 1, 1, 6]))
