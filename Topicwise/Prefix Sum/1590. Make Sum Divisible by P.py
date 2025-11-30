# https://leetcode.com/problems/make-sum-divisible-by-p/description/?envType=daily-question&envId=2025-11-30

from typing import List


class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        total = sum(nums)
        requiredRem = total % p
        if requiredRem == 0:
            return 0

        n = len(nums)
        remainders = {0: -1}
        ans = n
        prefix = 0

        for i, num in enumerate(nums):
            prefix = (prefix + num) % p
            target = (prefix - requiredRem) % p
            print(num, prefix, target)

            if target in remainders:
                ans = min(ans, i - remainders[target])

            remainders[prefix] = i

        return ans if ans < n else -1


print(Solution().minSubarray(nums=[3, 1, 4, 2], p=6))
