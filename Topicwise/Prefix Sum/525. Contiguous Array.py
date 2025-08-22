# https://leetcode.com/problems/contiguous-array/


class Solution(object):
    def findMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        sum = 0
        sumIndex = {0: -1}
        length = 0
        for i, num in enumerate(nums):
            if num == 0:
                sum += -1
            else:
                sum += 1
            if sum in sumIndex:
                prev = sumIndex[sum]
                length = max(length, i - prev)
            else:
                sumIndex[sum] = i
        return length


print(Solution().findMaxLength([0, 1]))
print(Solution().findMaxLength([0, 1, 0]))
print(Solution().findMaxLength([0, 1, 1, 1, 1, 1, 0, 0, 0]))
print(Solution().findMaxLength([0, 1, 1]))
