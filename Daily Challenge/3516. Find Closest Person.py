# https://leetcode.com/problems/find-closest-person/description/?envType=daily-question&envId=2025-09-04


class Solution:
    def findClosest(self, x: int, y: int, z: int) -> int:

        if abs(z - x) < abs(z - y):
            return 1
        if abs(z - x) > abs(z - y):
            return 2

        return 0
