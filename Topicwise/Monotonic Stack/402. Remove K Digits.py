# https://leetcode.com/problems/remove-k-digits/description/


class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []

        for char in num:
            while stack and k > 0 and char < stack[-1]:
                stack.pop()
                k -= 1
            stack.append(char)
        if k > 0:
            stack = stack[:-k]
        ans = "".join(stack).lstrip("0")
        return ans or "0"


print(Solution().removeKdigits(num="1432219", k=3))
print(Solution().removeKdigits(num="10200", k=1))
print(Solution().removeKdigits(num="10", k=2))
