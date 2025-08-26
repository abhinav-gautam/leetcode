# https://leetcode.com/problems/two-best-non-overlapping-events/?envType=daily-question&envId=2024-12-05


class Solution(object):
    def maxTwoEvents(self, events):
        """
        :type events: List[List[int]]
        :rtype: int
        """

        sortedEvents = sorted(events, key=lambda x: x[2])

        print(sortedEvents)
        # valuePerDuration = []
        # for i in range(len(events)):
        #     start = events[i][0]
        #     end = events[i][1]
        #     value = events[i][2]

        #     value


obj = Solution()
print(obj.maxTwoEvents([[1, 3, 2], [4, 5, 2], [2, 4, 3]]))
