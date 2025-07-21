# https://leetcode.com/problems/rotate-array/description/


class Solution1(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        if len(nums) > 1 and k > 0:
            nums[:] = nums[-k:] + nums[0 : len(nums) - k]
        # print(nums)


Solution1().rotate([1, 2], 2)


class Solution2(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        if len(nums) > 1 and k > 0:
            nums.reverse()
            nums[:k] = reversed(nums[:k])
            nums[k:] = reversed(nums[k:])
        print(nums)


Solution2().rotate([1, 2, 3, 4, 5, 6, 7], 2)
