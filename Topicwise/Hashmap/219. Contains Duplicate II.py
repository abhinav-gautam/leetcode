# https://leetcode.com/problems/contains-duplicate-ii/


class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        posDict = {}
        for i in range(len(nums)):
            if nums[i] in posDict:
                diff = i - posDict[nums[i]][len(posDict[nums[i]]) - 1]
                if diff <= k:
                    return True
                posDict[nums[i]].append(i)
            else:
                posDict[nums[i]] = [i]
        print(posDict)
        return False


print(Solution().containsNearbyDuplicate([1, 2, 3, 1, 2, 3], 2))
print(Solution().containsNearbyDuplicate([1, 0, 1, 1], 1))
print(Solution().containsNearbyDuplicate([0, 2, 1, 3, 4, 1, 1], 1))
