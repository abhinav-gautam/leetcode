# https://leetcode.com/problems/container-with-most-water/description/


class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        maxArea = 0
        n = len(height)
        i = 0
        j = n - 1
        while i < j:
            area = (j - i) * min(height[i], height[j])
            maxArea = max(maxArea, area)
            if height[j] > height[i]:
                i += 1
            else:
                j -= 1
        return maxArea


print(Solution().maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))
print(Solution().maxArea([1, 1]))
print(Solution().maxArea([1, 2, 1]))
