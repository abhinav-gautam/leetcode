# https://leetcode.com/problems/shortest-distance-to-target-string-in-a-circular-array/?envType=daily-question&envId=2026-04-15

from typing import List


class Solution:
    def closestTarget(self, words: List[str], target: str, startIndex: int) -> int:
        if target not in words:
            return -1

        if words[startIndex] == target:
            return 0

        clockwiseShortest = 0
        antiClockwiseShortest = 0

        n = len(words)

        i = (startIndex + 1) % n

        while i != startIndex:
            clockwiseShortest += 1

            if words[i] == target:
                break

            i = (i + 1) % n

        i = (startIndex - 1 + n) % n

        while i != startIndex:
            antiClockwiseShortest += 1

            if words[i] == target:
                break

            i = (i - 1 + n) % n

        return min(clockwiseShortest, antiClockwiseShortest)


print(
    Solution().closestTarget(
        words=["hello", "i", "am", "leetcode", "hello"], target="hello", startIndex=1
    )
)
print(
    Solution().closestTarget(
        words=["a", "b", "leetcode"], target="leetcode", startIndex=0
    )
)
print(
    Solution().closestTarget(words=["i", "eat", "leetcode"], target="ate", startIndex=0)
)
