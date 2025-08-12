# https://leetcode.com/problems/number-of-good-ways-to-split-a-string/


class Solution(object):
    def numSplits(self, s):
        """
        :type s: str
        :rtype: int
        """
        charsCount = {}
        for char in s:
            if char in charsCount:
                charsCount[char] += 1
            else:
                charsCount[char] = 1

        count = 0
        leftChars = {}
        leftCount = 0
        rightCount = len(charsCount.keys())
        for i in range(len(s)):
            if s[i] not in leftChars:
                leftChars[s[i]] = 1
                leftCount += 1
            else:
                leftChars[s[i]] += 1
            if charsCount[s[i]] > 1:
                charsCount[s[i]] -= 1
            else:
                del charsCount[s[i]]
                rightCount -= 1
            if leftCount == rightCount:
                count += 1
        return count


print(Solution().numSplits("aacaba"))
