# https://leetcode.com/problems/increasing-triplet-subsequence/description/
class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        isPresent = False
        n = len(nums)
        num_i, num_j = float("inf"), float("inf")
        for i in range(n):
            if nums[i] <= num_i:
                num_i = nums[i]
            elif nums[i] <= num_j:
                num_j = nums[i]
            else:
                isPresent = True
                break
        return isPresent


# print(Solution().increasingTriplet([1, 2, 3, 4, 5]))
# print(Solution().increasingTriplet([5, 4, 3, 2, 1]))
# print(Solution().increasingTriplet([2, 1, 5, 0, 4, 6]))
# print(Solution().increasingTriplet([20, 100, 10, 12, 5, 13]))
print(Solution().increasingTriplet([2, 4, -2, -3]))
