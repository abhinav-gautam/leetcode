# https://leetcode.com/contest/weekly-contest-469/problems/split-array-with-minimum-difference/

from typing import List


class Solution:

    def splitArray(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 2:
            return -1

        prefix_sum = [0] * (n + 1)
        for i in range(n):
            prefix_sum[i + 1] = prefix_sum[i] + nums[i]

        inc = [False] * n
        inc[0] = True
        for i in range(1, n):
            inc[i] = inc[i - 1] and nums[i - 1] < nums[i]

        dec = [False] * n
        dec[n - 1] = True
        for i in range(n - 2, -1, -1):
            dec[i] = dec[i + 1] and nums[i] > nums[i + 1]

        min_diff = float("inf")
        found = False

        for split in range(1, n):
            if inc[split - 1] and dec[split]:
                left_sum = prefix_sum[split]
                right_sum = prefix_sum[n] - prefix_sum[split]
                diff = abs(left_sum - right_sum)
                min_diff = min(min_diff, diff)
                found = True

        return min_diff if found else -1
