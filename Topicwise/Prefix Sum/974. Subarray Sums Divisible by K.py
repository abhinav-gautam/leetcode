# https://leetcode.com/problems/subarray-sums-divisible-by-k/description/


class Solution(object):
    def subarraysDivByK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        cumSum = 0
        count = 0
        remCount = {0: 1}

        for num in nums:
            cumSum += num

            if cumSum % k in remCount:
                count += remCount[cumSum % k]
                remCount[cumSum % k] += 1
            else:
                remCount[cumSum % k] = 1
        return count


print(Solution().subarraysDivByK(nums=[4, 5, 0, -2, -3, 1], k=5))
