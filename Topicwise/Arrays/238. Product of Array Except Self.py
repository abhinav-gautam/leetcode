class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        pre_prod = 1
        output = [1] * len(nums)
        for i in range(1, len(nums)):
            pre_prod *= nums[i - 1]
            output[i] = pre_prod
        pre_prod = 1
        for i in range(len(nums) - 2, -1, -1):
            pre_prod *= nums[i + 1]
            output[i] *= pre_prod

        return output


print(Solution().productExceptSelf([4, 3, 2, 1, 2]))
