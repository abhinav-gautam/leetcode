# https://leetcode.com/problems/maximum-bitwise-xor-after-rearrangement/description/


class Solution:
    def maximumXor(self, s: str, t: str) -> str:
        count0 = t.count("0")
        count1 = t.count("1")

        result = []

        for ch in s:
            if ch == "0":
                if count1 > 0:
                    result.append("1")
                    count1 -= 1
                else:
                    result.append("0")
                    count0 -= 1
            else:
                if count0 > 0:
                    result.append("1")
                    count0 -= 1
                else:
                    result.append("0")
                    count1 -= 1

        return "".join(result)
