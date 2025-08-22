# https://leetcode.com/problems/maximum-average-subarray-i/description/


class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        sum = 0
        maxAvg = float("-inf")
        for i, num in enumerate(nums):
            if i < k - 1:
                sum += num
            else:
                sum += num
                avg = sum / k
                maxAvg = max(maxAvg, avg)
                sum -= nums[i - k + 1]
        return maxAvg


print(Solution().findMaxAverage(nums=[1, 12, -5, -6, 50, 3], k=4))
print(Solution().findMaxAverage(nums=[5], k=1))
