# https://leetcode.com/problems/sort-vowels-in-a-string/description/?envType=daily-question&envId=2025-09-11


class Solution:
    def sortVowels(self, s: str) -> str:
        vowels = ["a", "e", "i", "o", "u"]
        s_vowels = sorted([char for char in s if char.lower() in vowels])
        result = []
        i = 0
        for char in s:
            if char.lower() in vowels:
                result.append(s_vowels[i])
                i += 1
            else:
                result.append(char)
        return "".join(result)


print(Solution().sortVowels("lEetcOde"))
