# https://leetcode.com/problems/find-the-duplicate-number/description/

from typing import List


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = nums[0]
        fast = nums[0]
        n = len(nums)

        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]

            if slow == fast:
                break

        slow = nums[0]
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
        return slow


print(Solution().findDuplicate([1, 3, 4, 2, 2]))
print(Solution().findDuplicate([3, 1, 3, 4, 2]))
print(Solution().findDuplicate([3, 3, 3, 3, 3]))
print(
    Solution().findDuplicate(
        [18, 13, 14, 17, 9, 19, 7, 17, 4, 6, 17, 5, 11, 10, 2, 15, 8, 12, 16, 17]
    )
)
