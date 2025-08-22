# https://leetcode.com/problems/continuous-subarray-sum/description/


class Solution(object):
    def checkSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        sum = 0
        remDict = {0: -1}
        for index, num in enumerate(nums):
            sum += num
            mod = sum % k
            if mod in remDict:
                length = index - remDict[mod]
                if length > 1:
                    return True
            else:
                remDict[mod] = index
        return False


print(Solution().checkSubarraySum(nums=[23, 2, 4, 6, 7], k=6))
print(Solution().checkSubarraySum(nums=[23, 2, 6, 4, 7], k=6))
print(Solution().checkSubarraySum(nums=[23, 2, 6, 4, 7], k=13))
print(Solution().checkSubarraySum(nums=[5, 0, 0, 0], k=3))
print(Solution().checkSubarraySum(nums=[2, 4, 3], k=6))
print(Solution().checkSubarraySum(nums=[0, 0], k=6))
print(Solution().checkSubarraySum(nums=[1, 1], k=1))
print(Solution().checkSubarraySum(nums=[1, 0, 1, 0, 1], k=4))
