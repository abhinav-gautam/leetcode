# https://leetcode.com/problems/number-of-zero-filled-subarrays/description/


class Solution(object):
    def zeroFilledSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        subarrays = 0
        i, j = 0, 0
        n = len(nums)

        while i < n and j < n:
            if nums[j] == 0:
                subarrays += 1 + (j - i)
                j += 1
            else:
                j += 1
                i = j
        return subarrays


print(Solution().zeroFilledSubarray([1, 3, 0, 0, 2, 0, 0, 4]))
print(Solution().zeroFilledSubarray([0, 0, 0, 2, 0, 0]))
print(Solution().zeroFilledSubarray([2, 10, 2019]))
