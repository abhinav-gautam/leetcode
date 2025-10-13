# https://leetcode.com/problems/sum-of-elements-with-frequency-divisible-by-k/description/

from typing import List
from collections import Counter


class Solution:
    def sumDivisibleByK(self, nums: List[int], k: int) -> int:
        freq = Counter(nums)
        sum = 0
        for key, value in freq.items():
            if value % k == 0:
                sum += key * value
        return sum


print(Solution().sumDivisibleByK(nums=[1, 2, 2, 3, 3, 3, 3, 4], k=2))
print(Solution().sumDivisibleByK(nums=[1, 2, 3, 4, 5], k=2))
print(Solution().sumDivisibleByK(nums=[4, 4, 4, 1, 2, 3], k=3))
