# https://leetcode.com/problems/maximum-sum-of-distinct-subarrays-with-length-k/description/


class Solution(object):
    def maximumSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        subArray = set()
        maxSum = 0
        i = j = 0
        n = len(nums)
        sum = 0
        while j < n:
            while nums[j] in subArray:
                subArray.remove(nums[i])
                sum -= nums[i]
                i += 1
            subArray.add(nums[j])
            sum += nums[j]
            j += 1

            if j - i == k:
                maxSum = max(sum, maxSum)
                subArray.remove(nums[i])
                sum -= nums[i]
                i += 1
        return maxSum


print(Solution().maximumSubarraySum(nums=[1, 5, 4, 2, 9, 9, 9], k=3))
print(Solution().maximumSubarraySum(nums=[1, 1, 1, 7, 8, 9], k=3))
print(Solution().maximumSubarraySum(nums=[1, 2, 2], k=2))
print(Solution().maximumSubarraySum(nums=[1, 1, 2], k=2))
print(Solution().maximumSubarraySum(nums=[9, 9, 9, 1, 2, 3], k=3))
print(Solution().maximumSubarraySum(nums=[11, 11, 7, 2, 9, 4, 17, 1], k=1))
