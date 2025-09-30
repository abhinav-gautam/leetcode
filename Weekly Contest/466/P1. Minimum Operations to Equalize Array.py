# https://leetcode.com/contest/weekly-contest-466/problems/minimum-operations-to-equalize-array/description/

from typing import List


class Solution:
    def minOperations(self, nums: List[int]) -> int:
        if all([x == nums[0] for x in nums]):
            return 0
        else:
            return 1


print(Solution().minOperations([1, 2]))
print(Solution().minOperations([109, 14, 19, 32, 89]))
