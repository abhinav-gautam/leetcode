# https://leetcode.com/problems/longest-balanced-subarray-i/description/

from typing import List


class Solution:
    def longestBalanced(self, nums: List[int]) -> int:
        n = len(nums)
        seen = set()  # track numbers seen so far
        distinct_even = set()
        distinct_odd = set()
        counter = 0  # len(distinct_even) - len(distinct_odd)
        maxLength = 0
        hashTable = {0: -1}  # prefix balance -> earliest index

        for i, num in enumerate(nums):
            if num not in seen:
                seen.add(num)
                if num % 2 == 0:
                    distinct_even.add(num)
                else:
                    distinct_odd.add(num)

            counter = len(distinct_even) - len(distinct_odd)

            if counter in hashTable:
                start = hashTable[counter]
                # Only consider if both sets have at least one element
                if len(distinct_even) > 0 and len(distinct_odd) > 0:
                    maxLength = max(maxLength, i - start)
            else:
                hashTable[counter] = i

        return maxLength


print(Solution().longestBalanced(nums=[2, 5, 4, 3]))
print(Solution().longestBalanced(nums=[3, 2, 2, 5, 4]))
print(Solution().longestBalanced(nums=[1, 2, 3, 2]))
print(Solution().longestBalanced(nums=[6, 6]))
print(Solution().longestBalanced(nums=[22, 36, 22]))
print(Solution().longestBalanced(nums=[3, 2, 2, 5, 4]))
print(Solution().longestBalanced(nums=[10, 6, 10, 7]))
