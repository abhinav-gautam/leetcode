# https://leetcode.com/problems/isomorphic-strings/description/


class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        sDict = {}
        tDict = {}
        for i in range(len(s)):
            if s[i] in sDict:
                sDict[s[i]].append(i)
            else:
                sDict[s[i]] = [i]
        for i in range(len(t)):
            if t[i] in tDict:
                tDict[t[i]].append(i)
            else:
                tDict[t[i]] = [i]
        return list(sDict.values()) == list(tDict.values())


print(Solution().isIsomorphic("egg", "add"))
print(Solution().isIsomorphic("paper", "title"))
print(Solution().isIsomorphic("bbbaaaba", "aaabbbba"))
