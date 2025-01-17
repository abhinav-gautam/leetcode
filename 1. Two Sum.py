# https://leetcode.com/problems/two-sum/description/

# Brute Force
# class Solution(object):
#     def twoSum(self, nums, target):
#         """
#         :type nums: List[int]
#         :type target: int
#         :rtype: List[int]
#         """

#         n = len(nums)
#         for i in range(n):
#             for j in range(n):
#                 if i != j and nums[i] + nums[j] == target:
#                     return [i, j]


class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        n = len(nums)
        hashMap = {}

        for i in range(n):
            hashMap[nums[i]] = i

        for i in range(n):
            complement = target - nums[i]
            if complement in hashMap and hashMap[complement] != i:
                return [i, hashMap[complement]]


obj = Solution()
print(obj.twoSum([3, 3], 6))
