# https://leetcode.com/problems/check-if-all-1s-are-at-least-length-k-places-away/description/?envType=daily-question&envId=2025-11-17

from typing import List


class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        prev = -1

        for index, num in enumerate(nums):
            if num == 1:
                if prev != -1 and index - prev - 1 < k:
                    return False
                prev = index
        return True


print(Solution().kLengthApart(nums=[1, 0, 0, 0, 1, 0, 0, 1], k=2))
print(Solution().kLengthApart(nums=[1, 0, 0, 1, 0, 1], k=2))
