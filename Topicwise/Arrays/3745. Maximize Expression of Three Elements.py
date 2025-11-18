# https://leetcode.com/problems/maximize-expression-of-three-elements/description/

from typing import List


class Solution:
    def maximizeExpressionOfThree(self, nums: List[int]) -> int:
        ans = float("-inf")
        n = len(nums)
        for a in range(n):
            for b in range(n):
                for c in range(n):
                    if a != b and b != c:
                        value = nums[a] + nums[b] - nums[c]
                        ans = max(ans, value)
        return ans


print(Solution().maximizeExpressionOfThree([1, 4, 2, 5]))
