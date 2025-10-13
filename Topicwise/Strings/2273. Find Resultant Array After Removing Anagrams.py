# https://leetcode.com/problems/find-resultant-array-after-removing-anagrams/description/?envType=daily-question&envId=2025-10-13

from typing import List


class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        for i in range(len(words) - 1, 0, -1):
            if sorted(words[i]) == sorted(words[i - 1]):
                words.pop(i)
        return words


print(Solution().removeAnagrams(["abba", "baba", "bbaa", "cd", "cd"]))
print(Solution().removeAnagrams(["z", "z", "z", "gsw", "wsg", "gsw", "krptu"]))
