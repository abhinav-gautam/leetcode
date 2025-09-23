# https://leetcode.com/problems/compare-version-numbers/description/?envType=daily-question&envId=2025-09-23


class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        version1 = [int(num) for num in version1.split(".")]
        version2 = [int(num) for num in version2.split(".")]
        v1Len = len(version1)
        v2Len = len(version2)

        for i in range(v1Len - 1, -1, -1):
            if version1[i] == 0:
                version1.pop(i)
            else:
                break

        for i in range(v2Len - 1, -1, -1):
            if version2[i] == 0:
                version2.pop(i)
            else:
                break

        minLen = min(len(version1), len(version2))

        for i in range(minLen):
            if version1[i] > version2[i]:
                return 1
            elif version1[i] < version2[i]:
                return -1

        if len(version1) > len(version2):
            return 1
        elif len(version1) < len(version2):
            return -1

        return 0


print(Solution().compareVersion(version1="1.2", version2="1.10"))
print(Solution().compareVersion(version1="1.01", version2="1.001"))
print(Solution().compareVersion(version1="1.0", version2="1.0.0.0"))
print(Solution().compareVersion(version1="1.0.1", version2="1"))
print(Solution().compareVersion(version1="0.1", version2="1.0"))
