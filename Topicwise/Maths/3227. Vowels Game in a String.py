# https://leetcode.com/problems/vowels-game-in-a-string/?envType=daily-question&envId=2025-09-12


class Solution:
    def doesAliceWin(self, s: str) -> bool:
        if s.count("a") or s.count("e") or s.count("i") or s.count("o") or s.count("u"):
            return True

        return False
