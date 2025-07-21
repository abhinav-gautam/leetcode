# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        buying_price = prices[0]
        selling_price = prices[0]
        max_profit = 0

        for i in range(0, len(prices) - 1):
            if prices[i] < buying_price:
                buying_price = prices[i]
                selling_price = prices[i]
            if prices[i] > selling_price and prices[i] - buying_price > max_profit:
                selling_price = prices[i]
                max_profit = selling_price - buying_price

        return max_profit


print(Solution().maxProfit([7, 1, 5, 3, 6, 4]))
