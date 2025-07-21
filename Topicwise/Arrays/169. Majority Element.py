# https://leetcode.com/problems/majority-element/description/


class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums_dict = {}
        majority_element_count = 0
        majority_element = 0
        for num in nums:
            if num in nums_dict:
                nums_dict[num] += 1
            else:
                nums_dict[num] = 1

        for key in nums_dict:
            if nums_dict[key] > majority_element_count:
                majority_element_count = max(nums_dict[key], majority_element_count)
                majority_element = key

        return majority_element


print(Solution().majorityElement([3, 2, 3]))
