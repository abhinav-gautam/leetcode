# https://leetcode.com/problems/minimum-removals-to-achieve-target-xor/description/


class Solution:
    def minRemovals(self, nums, target):
        total_xor = 0
        for num in nums:
            total_xor ^= num

        need = total_xor ^ target

        INF = float("inf")
        dp = {0: 0}

        for num in nums:
            new_dp = dp.copy()
            for x in dp:
                nx = x ^ num
                if nx not in new_dp:
                    new_dp[nx] = dp[x] + 1
                else:
                    new_dp[nx] = min(new_dp[nx], dp[x] + 1)
            dp = new_dp

        return dp[need] if need in dp else -1
