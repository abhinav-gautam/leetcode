# https://leetcode.com/problems/max-consecutive-ones-iii/description/


class Solution:
    def longestOnes(self, nums: list[int], k: int) -> int:
        maxCount = maxLength = oneCount = left = 0

        for right in range(len(nums)):
            if nums[right]:
                oneCount += 1

            maxCount = max(maxCount, oneCount)

            if right - left + 1 - maxCount > k:
                if nums[left]:
                    oneCount -= 1
                left += 1

            windowSize = right - left + 1
            maxLength = max(maxLength, windowSize)
        return maxLength


print(
    Solution().longestOnes(
        nums=[0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1], k=3
    )
)
