# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/description/


class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        buy = prices[0]
        sell = prices[0]
        profit = 0

        for i in range(len(prices)):
            if prices[i] < buy:
                buy = prices[i]
                sell = prices[i]
            if prices[i] > sell:
                sell = prices[i]
                profit += sell - buy
                buy = prices[i]

        return profit


print(Solution().maxProfit([7, 1, 5, 3, 6, 4]))
