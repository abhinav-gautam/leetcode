# https://leetcode.com/problems/count-good-subarrays/description/


class Solution:
    def countGoodSubarrays(self, nums: list[int]) -> int:
        n = len(nums)

        prevGreater = [-1] * n
        stack = []
        for i in range(n):
            while stack and nums[stack[-1]] <= nums[i]:
                stack.pop()
            prevGreater[i] = stack[-1] if stack else -1
            stack.append(i)

        nextGreater = [n] * n
        stack = []
        for i in range(n - 1, -1, -1):
            while stack and nums[stack[-1]] < nums[i]:
                stack.pop()
            nextGreater[i] = stack[-1] if stack else n
            stack.append(i)

        bit_pos = defaultdict(list)
        for i, num in enumerate(nums):
            for b in range(31):
                if num & (1 << b):
                    bit_pos[b].append(i)

        def get_prev_bad(i):
            res = -1
            for b in range(31):
                if not (nums[i] & (1 << b)):
                    lst = bit_pos[b]
                    idx = bisect_left(lst, i) - 1
                    if idx >= 0:
                        res = max(res, lst[idx])
            return res

        def get_next_bad(i):
            res = n
            for b in range(31):
                if not (nums[i] & (1 << b)):
                    lst = bit_pos[b]
                    idx = bisect_right(lst, i)
                    if idx < len(lst):
                        res = min(res, lst[idx])
            return res

        ans = 0
        for i in range(n):
            left_bad = get_prev_bad(i)
            right_bad = get_next_bad(i)

            left = max(prevGreater[i], left_bad)
            right = min(nextGreater[i], right_bad)

            ans += (i - left) * (right - i)

        return ans
