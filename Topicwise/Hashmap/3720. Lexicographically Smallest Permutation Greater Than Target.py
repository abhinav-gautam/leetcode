# https://leetcode.com/problems/lexicographically-smallest-permutation-greater-than-target/description/

from collections import Counter


class Solution:
    def lexGreaterPermutation(self, s: str, target: str) -> str:
        n = len(s)
        s = sorted(s)
        count = Counter(s)
        result = []

        def dfs(idx, greater):
            if idx == n:
                return "".join(result) if greater else ""

            for ch in sorted(count.keys()):
                if count[ch] == 0:
                    continue
                if not greater:
                    if ch < target[idx]:
                        continue
                    if ch == target[idx]:
                        count[ch] -= 1
                        result.append(ch)
                        ans = dfs(idx + 1, False)
                        if ans:
                            return ans
                        result.pop()
                        count[ch] += 1
                        continue
                count[ch] -= 1
                result.append(ch)
                ans = dfs(idx + 1, True)
                if ans:
                    return ans
                result.pop()
                count[ch] += 1
            return ""

        return dfs(0, False)


print(Solution().lexGreaterPermutation(s="abc", target="bba"))
print(Solution().lexGreaterPermutation(s="leet", target="code"))
