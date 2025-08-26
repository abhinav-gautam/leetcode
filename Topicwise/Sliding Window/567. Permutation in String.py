# https://leetcode.com/problems/permutation-in-string/description/


class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        s1Dict = {}
        permutation = {}

        for char in s1:
            if char in s1Dict:
                s1Dict[char] += 1
            else:
                s1Dict[char] = 1
        i = j = 0

        while i < len(s2) and j < len(s2):
            if s2[j] in s1Dict:
                if s2[j] in permutation:
                    permutation[s2[j]] += 1
                else:
                    permutation[s2[j]] = 1
            else:
                permutation = {}
                i = j + 1
            if j - i == len(s1) - 1:
                if permutation == s1Dict:
                    return True
                permutation[s2[i]] -= 1
                i += 1
            j += 1
        return False


print(Solution().checkInclusion(s1="ab", s2="eidbaooo"))
print(Solution().checkInclusion(s1="ab", s2="eidboaoo"))
