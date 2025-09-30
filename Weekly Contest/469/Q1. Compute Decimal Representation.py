# https://leetcode.com/contest/weekly-contest-469/problems/compute-decimal-representation/

from typing import List


class Solution:
    def decimalRepresentation(self, n: int) -> List[int]:
        result = []
        d = 10
        while n > 0:
            r = n % d
            if r > 0:
                result.insert(0, r)
            n -= r
            d *= 10
        return result


print(Solution().decimalRepresentation(537))
print(Solution().decimalRepresentation(102))
print(Solution().decimalRepresentation(6))
