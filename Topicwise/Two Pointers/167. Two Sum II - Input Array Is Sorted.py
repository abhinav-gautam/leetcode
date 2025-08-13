# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/description/


class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """

        low = 0
        high = len(numbers) - 1

        while low < high:
            sum = numbers[low] + numbers[high]
            if sum == target:
                return [low + 1, high + 1]
            elif sum > target:
                high = high - 1
            else:
                low = low + 1


print(Solution().twoSum(numbers=[2, 7, 11, 15], target=9))
print(Solution().twoSum(numbers=[3, 24, 50, 79, 88, 150, 345], target=200))
