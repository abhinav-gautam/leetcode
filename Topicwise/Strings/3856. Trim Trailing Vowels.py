# https://leetcode.com/problems/trim-trailing-vowels/description/


class Solution:
    def trimTrailingVowels(self, s: str) -> str:
        lastConsonant = len(s) - 1
        vowels = ["a", "e", "i", "o", "u"]

        for i in range(len(s) - 1, -1, -1):
            if s[i] in vowels:
                lastConsonant -= 1
            else:
                break
        return s[: lastConsonant + 1]


print(Solution().trimTrailingVowels("idea"))
print(Solution().trimTrailingVowels("day"))
