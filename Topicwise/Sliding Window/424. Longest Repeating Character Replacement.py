# https://leetcode.com/problems/longest-repeating-character-replacement/description/


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        charCount = [0] * 26
        left = maxLength = maxCount = 0
        n = len(s)
        for right in range(n):
            charIndex = ord(s[right]) - ord("A")
            charCount[charIndex] += 1
            windowSize = right - left + 1

            maxCount = max(charCount[charIndex], maxCount)

            if windowSize - maxCount > k:
                charCount[ord(s[left]) - ord("A")] -= 1
                left += 1

            windowSize = right - left + 1
            maxLength = max(windowSize, maxLength)

        return maxLength


print(Solution().characterReplacement(s="AAAA", k=2))
print(Solution().characterReplacement(s="ABAB", k=2))
print(Solution().characterReplacement(s="AABABBA", k=1))
