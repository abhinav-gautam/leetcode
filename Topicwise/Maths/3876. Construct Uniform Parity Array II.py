# https://leetcode.com/problems/construct-uniform-parity-array-ii/description/


class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        odds = [x for x in nums1 if x % 2 == 1]
        evens = [x for x in nums1 if x % 2 == 0]

        if not odds:
            return True

        min_odd = min(odds)

        count_min_odd = odds.count(min_odd)

        can_make_odd = all(min_odd < x for x in evens)

        can_make_even = count_min_odd >= 2

        return can_make_odd or can_make_even
