# https://leetcode.com/problems/find-minimum-operations-to-make-all-elements-divisible-by-three/description/?envType=daily-question&envId=2025-11-22

from typing import List


class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        count = 0

        for num in nums:
            count += min(num % 3, 3 - num % 3)

        return count
