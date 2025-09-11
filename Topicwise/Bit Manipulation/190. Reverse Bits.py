# https://leetcode.com/problems/reverse-bits/


class Solution:
    def reverseBits(self, n: int) -> int:
        binary = bin(n)
        binary_32 = binary[2:].zfill(32)
        reverse = binary_32[::-1]
        return int(reverse, 2)
