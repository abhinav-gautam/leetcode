# https://leetcode.com/problems/group-anagrams/description/


class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        strs_dict = {}

        for item in strs:
            sortedItem = "".join(sorted(item))
            if sortedItem in strs_dict:
                strs_dict[sortedItem].append(item)
            else:
                strs_dict[sortedItem] = [item]
        return list(strs_dict.values())


print(Solution().groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
print(Solution().groupAnagrams([""]))
print(Solution().groupAnagrams(["a"]))
