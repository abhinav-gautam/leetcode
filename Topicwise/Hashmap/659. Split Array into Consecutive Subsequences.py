# https://leetcode.com/problems/split-array-into-consecutive-subsequences/description/


class Solution:
    def isPossible(self, nums: list[int]) -> bool:
        freq = dict()
        vac = dict()

        for num in nums:
            if num not in freq:
                freq[num] = 1
            else:
                freq[num] += 1
        for num in nums:
            if freq[num] == 0:
                continue
            if num in vac and vac[num] > 0:
                vac[num] -= 1
                freq[num] -= 1
                if num + 1 in vac:
                    vac[num + 1] += 1
                else:
                    vac[num + 1] = 1
            elif (
                num + 1 in freq
                and freq[num + 1] > 0
                and num + 2 in freq
                and freq[num + 2] > 0
            ):
                freq[num] -= 1
                freq[num + 1] -= 1
                freq[num + 2] -= 1
                if num + 3 in vac:
                    vac[num + 3] += 1
                else:
                    vac[num + 3] = 1

            else:
                return False

        return True


print(Solution().isPossible([1, 2, 3, 3, 4, 5]))
print(Solution().isPossible([1, 2, 3, 3, 4, 4, 5, 5]))
print(Solution().isPossible([1, 2, 3, 4, 5, 5, 6, 7]))
