# https://leetcode.com/problems/longest-balanced-substring-i/description/


class Solution:
    def longestBalanced(self, s: str) -> int:
        max_len = 0
        n = len(s)

        for left in range(n):
            freq = {}
            for right in range(left, n):
                freq[s[right]] = freq.get(s[right], 0) + 1
                if len(set(list(freq.values()))) == 1:
                    max_len = max(max_len, right - left + 1)
        return max_len
