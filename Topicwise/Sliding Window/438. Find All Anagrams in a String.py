# https://leetcode.com/problems/find-all-anagrams-in-a-string/description/


class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """

        isAnagram = False
        result = []
        pDict = {}
        anagram = {}

        for char in p:
            if char in pDict:
                pDict[char] += 1
            else:
                pDict[char] = 1

        i = j = 0
        while i < len(s) and j < len(s):
            if s[j] in pDict:
                if s[j] in anagram:
                    anagram[s[j]] += 1
                else:
                    anagram[s[j]] = 1
            else:
                anagram = {}
                i = j + 1
            if j - i == len(p) - 1:
                if anagram == pDict:
                    result.append(i)
                anagram[s[i]] -= 1
                i += 1
            j += 1
        return result


print(Solution().findAnagrams(s="cbaebabacd", p="abc"))
print(Solution().findAnagrams(s="abab", p="ab"))
print(Solution().findAnagrams(s="abaacbabc", p="abc"))
