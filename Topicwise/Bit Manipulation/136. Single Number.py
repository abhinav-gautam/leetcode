# https://leetcode.com/problems/single-number/description/
from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        xor = 0
        for num in nums:
            xor ^= num
        return xor


print(Solution().singleNumber([4, 1, 2, 1, 2]))
