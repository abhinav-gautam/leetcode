# https://leetcode.com/contest/biweekly-contest-166/problems/majority-frequency-characters/


class Solution:
    def majorityFrequencyGroup(self, s: str) -> str:
        s_set = set(s)
        freq_map = {}
        max_freq_group = 0
        max_freq_group_size = 0
        for char in s_set:
            count = s.count(char)
            freq_map.setdefault(count, []).append(char)

            if max_freq_group_size < len(freq_map[count]):
                max_freq_group_size = len(freq_map[count])
                max_freq_group = count

            if max_freq_group_size == len(freq_map[count]) and count > max_freq_group:
                max_freq_group_size = len(freq_map[count])
                max_freq_group = count

        return "".join(freq_map[max_freq_group])


print(Solution().majorityFrequencyGroup(s="aaabbbccdddde"))
print(Solution().majorityFrequencyGroup(s="pfpfgi"))
