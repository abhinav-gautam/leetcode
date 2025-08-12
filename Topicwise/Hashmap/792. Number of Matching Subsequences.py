# https://leetcode.com/problems/number-of-matching-subsequences/description/


# Naive Solution
class Solution1(object):
    def numMatchingSubseq(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: int
        """
        count = 0
        subseq = {}
        for word in words:
            if word in subseq:
                isSeq = True
            else:
                isSeq = self.isSubsequence(s, word)
                subseq[word] = True
            if isSeq:
                count += 1
        return count

    def isSubsequence(self, s, word):
        if not word:
            return True
        i = 0
        j = 0
        while i < len(s) and j < len(word):
            if s[i] == word[j]:
                j += 1
            i += 1
        return j == len(word)


class Solution(object):
    def numMatchingSubseq(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: int
        """
        count = 0
        self.chars = {}
        for i in range(len(s)):
            if s[i] in self.chars:
                self.chars[s[i]].append(i)
            else:
                self.chars[s[i]] = [i]
        print(self.chars)

        for word in words:
            if self.isSubsequence(word):
                count += 1
        return count

    def isSubsequence(self, word):
        prevIndex = -1
        for char in word:
            if char not in self.chars:
                return False
            indices = self.chars[char]
            index = self.binarySearch(indices, prevIndex + 1)
            if index == len(indices):
                return False
            prevIndex = indices[index]
        return True

    def binarySearch(self, indices, target):
        low = 0
        high = len(indices)

        while low < high:
            mid = low + (high - low) // 2

            if indices[mid] < target:
                low = mid + 1
            else:
                high = mid
        return low


print(Solution().numMatchingSubseq("abcde", ["a", "bb", "acd", "ace"]))
print(
    Solution().numMatchingSubseq(
        "qlhxagxdqh", ["qlhxagxdq", "qlhxagxdq", "lhyiftwtut", "yfzwraahab"]
    )
)
print(
    Solution().numMatchingSubseq(
        "dsahjpjauf", ["ahjpjau", "ja", "ahbwzgqnuk", "tnmlanowax"]
    )
)
