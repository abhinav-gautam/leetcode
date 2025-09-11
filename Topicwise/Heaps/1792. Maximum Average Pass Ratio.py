# https://leetcode.com/problems/maximum-average-pass-ratio/?envType=daily-question&envId=2025-09-01

import heapq


class Solution(object):
    def maxAverageRatio(self, classes, extraStudents):
        """
        :type classes: List[List[int]]
        :type extraStudents: int
        :rtype: float
        """

        maxHeap = []
        ratioSum = 0
        for [passed, total] in classes:
            ratio = passed / total
            ratioSum += ratio
            ratioIncrement = (passed + 1) / (total + 1) - ratio
            heapq.heappush(maxHeap, (-ratioIncrement, (passed + 1, total + 1)))

        for i in range(extraStudents):
            increment, (passed, total) = heapq.heappop(maxHeap)
            ratioSum += -increment

            ratio = passed / total
            ratioIncrement = (passed + 1) / (total + 1) - ratio
            heapq.heappush(maxHeap, (-ratioIncrement, (passed + 1, total + 1)))

        return ratioSum / len(classes)


print(Solution().maxAverageRatio(classes=[[1, 2], [3, 5], [2, 2]], extraStudents=2))
print(
    Solution().maxAverageRatio(
        classes=[[2, 4], [3, 9], [4, 5], [2, 10]], extraStudents=4
    )
)
