# https://leetcode.com/problems/reorganize-string/description/


class Solution(object):
    def reorganizeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        sDict = {}
        for char in s:
            if char in sDict:
                sDict[char] += 1
            else:
                sDict[char] = 1
        result = ""
        i = 0
        sDict = dict(sorted(sDict.items(), key=lambda item: item[1], reverse=True))
        while len(sDict.keys()):
            char = list(sDict.keys())[0]
            if (
                len(result) > 0
                and result[len(result) - 1] == char
                and len(list(sDict.keys())) > 1
            ):
                char = list(sDict.keys())[1]
            if len(result) > 0 and result[len(result) - 1] == char:
                return ""
            result += char
            i += 1
            if sDict[char] > 1:
                sDict[char] -= 1
            else:
                del sDict[char]
            sDict = dict(sorted(sDict.items(), key=lambda item: item[1], reverse=True))
        return result


print(Solution().reorganizeString("aab"))
print(Solution().reorganizeString("aaab"))
print(Solution().reorganizeString("vvvlo"))
print(Solution().reorganizeString("baaba"))
print(Solution().reorganizeString("blflxll"))
print(Solution().reorganizeString("aaabbbccc"))
