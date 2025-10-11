# https://leetcode.com/problems/find-x-sum-of-all-k-long-subarrays-i/description/

from typing import List


class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        n = len(nums)
        answer = []

        i = j = 0
        countMap = {}

        while i < n - k + 1:
            while j <= i + k - 1:
                # Add nums[j] to countMap
                if nums[j] in countMap:
                    countMap[nums[j]] += 1
                else:
                    countMap[nums[j]] = 1
                j += 1
            # Calculate x-sum
            countArr = sorted(list(countMap.items()), key=lambda x: (-x[1], -x[0]))
            xSum = 0
            for m in range(min(x, len(countArr))):
                xSum += countArr[m][0] * countArr[m][1]
            answer.append(xSum)

            countMap[nums[i]] -= 1
            i += 1

        return answer


print(Solution().findXSum(nums=[1, 1, 2, 2, 3, 4, 2, 3], k=6, x=2))
