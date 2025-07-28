# https://leetcode.com/problems/longest-common-prefix/description/
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """

        prefix = ""
        i = 0

        while i < len(strs[0]):
            char = strs[0][i]
            isSame = True
            for word in strs:
                if i == len(word):
                    isSame = False
                    break
                if word[i] != char:
                    isSame = False
            if isSame:
                i += 1
                prefix += char
            else:
                break

        return prefix


print(Solution().longestCommonPrefix(["flower", "flow", "flight"]))
print(Solution().longestCommonPrefix(["dog", "racecar", "car"]))
