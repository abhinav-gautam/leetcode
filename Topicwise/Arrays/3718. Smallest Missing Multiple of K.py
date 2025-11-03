# https://leetcode.com/problems/smallest-missing-multiple-of-k/description/

from typing import List


class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        missing = k

        while True:
            if missing in nums:
                missing += k
            else:
                return missing


print(Solution().missingMultiple(nums=[8, 2, 3, 4, 6], k=2))
print(Solution().missingMultiple(nums=[1, 4, 7, 10, 15], k=5))
