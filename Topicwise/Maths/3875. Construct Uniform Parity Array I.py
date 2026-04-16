# https://leetcode.com/problems/construct-uniform-parity-array-i/description/


class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        nums1.sort()

        has_odd = any(x % 2 for x in nums1)

        if not has_odd:
            return True

        mn = nums1[0]

        for x in nums1:
            if x % 2 == 0 and x < mn:
                return False

        return True
