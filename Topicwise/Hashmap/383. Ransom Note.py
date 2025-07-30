# https://leetcode.com/problems/ransom-note/description/


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransomDict = {}
        magazineDict = {}

        for char in ransomNote:
            if char in ransomDict:
                ransomDict[char] += 1
            else:
                ransomDict[char] = 1
        for char in magazine:
            if char in magazineDict:
                magazineDict[char] += 1
            else:
                magazineDict[char] = 1
        for key in ransomDict.keys():
            if key not in magazineDict:
                return False
            if magazineDict[key] < ransomDict[key]:
                return False
        return True


print(Solution().canConstruct("aa", "aab"))
print(Solution().canConstruct("aa", "ab"))
