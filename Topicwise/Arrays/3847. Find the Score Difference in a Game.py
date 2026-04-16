# https://leetcode.com/problems/find-the-score-difference-in-a-game/description/

from typing import List


class Solution:
    def scoreDifference(self, nums: List[int]) -> int:
        scores = [0, 0]
        active = 0

        def swap(active):
            if active:
                active -= 1
            else:
                active += 1
            return active

        for i, score in enumerate(nums):
            if (i + 1) % 6 == 0:
                active = swap(active)

            if score % 2 == 1:
                active = swap(active)

            scores[active] += score

        return scores[0] - scores[1]


print(Solution().scoreDifference([1, 2, 3]))
print(Solution().scoreDifference([2, 4, 2, 1, 2, 1]))
