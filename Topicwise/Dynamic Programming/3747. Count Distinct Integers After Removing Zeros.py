# https://leetcode.com/problems/count-distinct-integers-after-removing-zeros/description/


class Solution:
    def countDistinct(self, n: int) -> int:
        s = str(n)
        L = len(s)

        count = 0
        pow9 = 1
        for k in range(1, L):
            pow9 *= 9
            count += pow9

        for i, ch in enumerate(s):
            d = int(ch)
            smaller = max(0, d - 1)
            rem = L - i - 1
            count += smaller * (9**rem)
            if d == 0:
                break
        else:
            count += 1

        return count


print(Solution().countDistinct(10))
