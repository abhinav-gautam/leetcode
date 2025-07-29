# https://leetcode.com/problems/number-of-good-pairs/description/
class Solution:
    def numIdenticalPairs(self, nums):
        numsPos = dict()
        n = len(nums)
        for i in range(n):
            if nums[i] in numsPos:
                numsPos[nums[i]].append(i)
            else:
                numsPos[nums[i]] = [i]
        goodPairs = 0
        for key in numsPos.keys():
            n = len(numsPos[key])
            goodPairs += n * (n - 1) // 2
        return goodPairs


print(Solution().numIdenticalPairs([1, 2, 3, 1, 1, 3]))
