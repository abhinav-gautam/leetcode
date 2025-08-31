# https://leetcode.com/problems/alice-and-bob-playing-flower-game/description/?envType=daily-question&envId=2025-08-29


class Solution(object):
    def flowerGame(self, n, m):
        """
        :type n: int
        :type m: int
        :rtype: int
        """
        even_n = n // 2
        odd_n = n - even_n

        even_m = m // 2
        odd_m = m - even_m

        return even_n * odd_m + odd_n * even_m


print(Solution().flowerGame(n=3, m=2))
