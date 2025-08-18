# https://leetcode.com/problems/range-sum-query-immutable/description/


class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums = nums
        self.sumArr = []
        sum = 0
        for num in nums:
            sum += num
            self.sumArr.append(sum)

    def sumRange(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: int
        """
        return self.sumArr[right] - self.sumArr[left] + self.nums[left]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)
