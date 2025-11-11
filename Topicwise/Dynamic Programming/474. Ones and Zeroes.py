# https://leetcode.com/problems/ones-and-zeroes/description/?envType=daily-question&envId=2025-11-11

from typing import List


class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        dp = {(0, 0): 0}

        for str in strs:
            zero = str.count("0")
            one = str.count("1")
            newDp = {}
            for key, value in dp.items():
                prevZero, prevOne = key
                newZero, newOne = prevZero + zero, prevOne + one

                if newZero <= m and newOne <= n:
                    if (newZero, newOne) not in dp or dp[(newZero, newOne)] < value + 1:
                        newDp[(newZero, newOne)] = value + 1

            dp.update(newDp)
        return max(dp.values())


print(Solution().findMaxForm(strs=["10", "0001", "111001", "1", "0"], m=5, n=3))
print(Solution().findMaxForm(strs=["10", "0", "1"], m=1, n=1))
print(Solution().findMaxForm(strs=["00011", "00001", "00001", "0011", "111"], m=8, n=5))
