# https://leetcode.com/problems/avoid-flood-in-the-city/description/?envType=daily-question&envId=2025-10-07

from typing import List
from sortedcontainers import SortedList


class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:
        res, full, dry = [-1] * len(rains), {}, SortedList()
        for i, lake in enumerate(rains):
            if lake == 0:
                dry.add(i)
                res[i] = 1
            elif lake in full:
                j = dry.bisect_right(full[lake])
                if j == len(dry):
                    return []
                res[dry[j]] = lake
                dry.pop(j)
                full[lake] = i
            else:
                full[lake] = i
        return res


print(Solution().avoidFlood([1, 2, 3, 4]))
print(Solution().avoidFlood([1, 2, 0, 0, 2, 1]))
print(Solution().avoidFlood([1, 2, 0, 1, 2]))
