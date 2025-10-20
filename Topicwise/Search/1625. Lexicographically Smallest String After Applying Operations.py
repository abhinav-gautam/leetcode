# https://leetcode.com/problems/lexicographically-smallest-string-after-applying-operations/description/?envType=daily-question&envId=2025-10-19


class Solution:
    def findLexSmallestString(self, s: str, a: int, b: int) -> str:
        def rotateStringRight(s, d):
            n = len(s)
            d %= n
            return s[-d:] + s[:-d]

        def addOddIndices(s, d):
            return "".join(
                [
                    str((int(char) + d) % 10) if i % 2 == 1 else char
                    for i, char in enumerate(list(s))
                ]
            )

        seen = set()
        queue = [rotateStringRight(s, b), addOddIndices(s, a)]
        mini = "9" * len(s)

        while len(queue):
            current = queue.pop(0)
            added = addOddIndices(current, a)
            rotated = rotateStringRight(current, b)
            mini = min(mini, current)

            if added not in seen:
                seen.add(added)
                queue.append(added)
            if rotated not in seen:
                seen.add(rotated)
                queue.append(rotated)

        return mini


print(Solution().findLexSmallestString(s="5525", a=9, b=2))
print(Solution().findLexSmallestString(s="74", a=5, b=1))
