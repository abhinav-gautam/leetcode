# https://leetcode.com/problems/adding-spaces-to-a-string/?envType=daily-question&envId=2024-12-03


class Solution(object):
    def addSpaces(self, s, spaces):
        """
        :type s: str
        :type spaces: List[int]
        :rtype: str
        """
        segments = [0] + spaces + [len(s)]
        substrings = []

        for i in range(len(segments) - 1):
            substrings.append(s[segments[i] : segments[i + 1]])

        return " ".join(substrings)
