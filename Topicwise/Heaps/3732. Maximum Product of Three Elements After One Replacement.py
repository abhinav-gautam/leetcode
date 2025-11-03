# https://leetcode.com/problems/maximum-product-of-three-elements-after-one-replacement/description/
from typing import List
import heapq


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxHeap = []

        for num in nums:
            heapq.heappush(maxHeap, -abs(num))

        first = -heapq.heappop(maxHeap)
        second = -heapq.heappop(maxHeap)

        return first * second * 100000


print(Solution().maxProduct([-5, 7, 0]))
print(Solution().maxProduct([-4, -2, -1, -3]))
print(Solution().maxProduct([0, 10, 0]))
