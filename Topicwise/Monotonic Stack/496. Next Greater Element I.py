# https://leetcode.com/problems/next-greater-element-i/description/

from typing import List


# Brute force
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        positions = {x: i for i, x in enumerate(nums2)}
        ans = []

        for num in nums1:
            pos = positions[num]
            nextGreater = -1
            if pos != len(nums2) - 1:
                for i in range(pos + 1, len(nums2)):
                    if nums2[i] > num:
                        nextGreater = nums2[i]
                        break
            ans.append(nextGreater)

        return ans


print(Solution().nextGreaterElement(nums1=[4, 1, 2], nums2=[1, 3, 4, 2]))
print(Solution().nextGreaterElement(nums1=[2, 4], nums2=[1, 2, 3, 4]))


# Monotonic stack
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        next_greater = {}
        stack = []

        for num in nums2:
            while stack and num > stack[-1]:
                top = stack.pop()
                next_greater[top] = num
            stack.append(num)

        while stack:
            top = stack.pop()
            next_greater[top] = -1

        result = [next_greater[num] for num in nums1]

        return result


print(Solution().nextGreaterElement(nums1=[4, 1, 2], nums2=[1, 3, 4, 2]))
print(Solution().nextGreaterElement(nums1=[2, 4], nums2=[1, 2, 3, 4]))
