# https://leetcode.com/problems/find-most-frequent-vowel-and-consonant/?envType=daily-question&envId=2025-09-13


class Solution:
    def maxFreqSum(self, s: str) -> int:
        vowels = ["a", "e", "i", "o", "u"]
        maxVowels = max(
            s.count("a"), s.count("e"), s.count("i"), s.count("o"), s.count("u")
        )
        consonants = {}
        for char in s:
            if char not in vowels:
                if char not in consonants:
                    consonants[char] = 1
                else:
                    consonants[char] += 1

        maxConsonants = max(consonants.values(), default=0)

        return maxVowels + maxConsonants


print(Solution().maxFreqSum("successes"))
