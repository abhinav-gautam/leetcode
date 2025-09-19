# https://leetcode.com/problems/maximum-number-of-words-you-can-type/?envType=daily-question&envId=2025-09-15


class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        words = text.split()
        count = 0
        for word in words:
            for char in brokenLetters:
                if char in word:
                    break
            else:
                count += 1
        return count


print(Solution().canBeTypedWords(text="hello world", brokenLetters="ad"))
