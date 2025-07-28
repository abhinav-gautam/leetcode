# https://leetcode.com/problems/reverse-words-in-a-string/description/


class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        return " ".join(word for word in list(reversed(s.split())))


print(Solution().reverseWords("a good   example"))
