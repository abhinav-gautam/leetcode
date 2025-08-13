# https://leetcode.com/problems/merge-sorted-array/


class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        end = len(nums1) - 1
        while n > 0 and m > 0:
            if nums2[n - 1] >= nums1[m - 1]:
                nums1[end] = nums2[n - 1]
                n -= 1
            else:
                nums1[end] = nums1[m - 1]
                m -= 1
            end -= 1
        while n > 0:
            nums1[end] = nums2[n - 1]
            n -= 1
            end -= 1
        print(nums1)


Solution().merge([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3)
