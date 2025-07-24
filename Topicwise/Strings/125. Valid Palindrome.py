# https://leetcode.com/problems/valid-palindrome/description/


class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """

        s = "".join(c for c in s if c.isalnum())
        if len(s) < 2:
            return True
        n = len(s) // 2
        i = 0
        while i <= n:
            if s[i].lower() != s[len(s) - i - 1].lower():
                return False
            i += 1
        return True


print(Solution().isPalindrome("A man, a plan, a canal: Panama"))
print(Solution().isPalindrome("race a car"))
