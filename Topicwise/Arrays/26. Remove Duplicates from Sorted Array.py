# https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        i, j, k = 0, 1, 1
        while i < len(nums) and j < len(nums):
            if nums[i] != nums[j]:
                i += 1
                nums[i] = nums[j]
                k += 1
            j += 1
        print(nums)
        return k


print(Solution().removeDuplicates([1, 1, 2]))
print(Solution().removeDuplicates([0, 0, 1, 1, 1, 1, 2, 2, 3, 4]))
