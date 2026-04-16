# https://leetcode.com/problems/count-monobit-integers/description/


class Solution:
    def countMonobit(self, n: int) -> int:
        count = 0
        for i in range(n + 1):
            bits = bin(i)
            unique = set(list(bits[2:]))
            if len(unique) == 1:
                count += 1
        return count


print(Solution().countMonobit(1))
print(Solution().countMonobit(4))
