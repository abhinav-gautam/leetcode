# https://leetcode.com/problems/subarray-sum-equals-k/description/


class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        count = 0
        cumSum = 0
        sumFreq = {0: 1}

        for num in nums:
            cumSum += num
            if cumSum - k in sumFreq:
                count += sumFreq[cumSum - k]
            if cumSum in sumFreq:
                sumFreq[cumSum] += 1
            else:
                sumFreq[cumSum] = 1
        return count


print(Solution().subarraySum([1, 1, 1], 2))
print(Solution().subarraySum([1, 2, 3], 3))
