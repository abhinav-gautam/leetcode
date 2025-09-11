# https://leetcode.com/problems/special-array-ii/?envType=daily-question&envId=2024-12-09


class Solution(object):
    def isArraySpecial(self, nums, queries):
        """
        :type nums: List[int]
        :type queries: List[List[int]]
        :rtype: List[bool]
        """

        n = len(nums)
        prefix_arr = [0] * n

        for i in range(1, n):
            prefix_arr[i] = prefix_arr[i - 1]

            if (nums[i - 1] % 2 == 0 and nums[i] % 2 != 0) or (
                nums[i - 1] % 2 != 0 and nums[i] % 2 == 0
            ):
                prefix_arr[i] += 1

        isSpecial = [False] * len(queries)
        for i in range(len(queries)):
            left = queries[i][0]
            right = queries[i][1]

            if right - left <= prefix_arr[right] - prefix_arr[left]:
                isSpecial[i] = True

        return isSpecial


obj = Solution()
print(obj.isArraySpecial([4, 3, 1, 6], [[0, 2], [2, 3]]))
