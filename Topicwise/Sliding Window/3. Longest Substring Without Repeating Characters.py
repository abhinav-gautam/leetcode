# https://leetcode.com/problems/longest-substring-without-repeating-characters/description/


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        count = 0
        charSet = set()
        left = right = 0
        n = len(s)
        maxCount = 0

        while right < n:
            while s[right] in charSet:
                charSet.remove(s[left])
                count -= 1
                left += 1
            if s[right] not in charSet:
                charSet.add(s[right])
                count += 1
                maxCount = max(count, maxCount)
            right += 1

        return maxCount


print(Solution().lengthOfLongestSubstring("abcabcbb"))
