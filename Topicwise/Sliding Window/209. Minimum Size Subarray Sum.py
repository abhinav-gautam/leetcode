# https://leetcode.com/problems/minimum-size-subarray-sum/description/


class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        preSum = []
        n = len(nums)
        sum = 0
        for num in nums:
            sum += num
            preSum.append(sum)
        left = 0
        right = 0
        windowSum = 0
        windowSize = float("inf")
        while right < n and left < n:
            if preSum[right] < target:
                right += 1
                continue
            windowSum = preSum[right] - preSum[left] + nums[left]

            if windowSum >= target:
                windowSize = min(right - left + 1, windowSize)
                left += 1
            else:
                right += 1
        if windowSize == float("inf"):
            return 0
        return windowSize


print(Solution().minSubArrayLen(target=7, nums=[2, 3, 1, 2, 4, 3]))
print(Solution().minSubArrayLen(target=4, nums=[1, 4, 4]))
print(Solution().minSubArrayLen(target=11, nums=[1, 1, 1, 1, 1, 1, 1, 1]))
