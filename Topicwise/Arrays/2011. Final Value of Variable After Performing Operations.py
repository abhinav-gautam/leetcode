# https://leetcode.com/problems/final-value-of-variable-after-performing-operations/description/?envType=daily-question&envId=2025-10-20

from typing import List


class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        x = 0

        for op in operations:
            if op == "X++" or op == "++X":
                x += 1
            if op == "X--" or op == "--X":
                x -= 1
        return x
