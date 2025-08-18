# https://leetcode.com/problems/3sum/description/


class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        numsDict = {}
        n = len(nums)
        nums = sorted(nums)
        for i in range(n):
            numsDict[nums[i]] = i
        result = []
        i = 0
        while i < n - 2:
            if nums[i] > 0:
                break
            j = i + 1
            while j < n - 1:
                complement = 0 - (nums[i] + nums[j])
                if complement in numsDict and numsDict[complement] > j:
                    result.append([nums[i], nums[j], complement])
                j = numsDict[nums[j]] + 1
            i = numsDict[nums[i]] + 1
        return result


print(Solution().threeSum([-1, 0, 1, 2, -1, -4]))
print(Solution().threeSum([2, -3, 0, -2, -5, -5, -4, 1, 2, -2, 2, 0, 2, -4, 5, 5, -10]))
