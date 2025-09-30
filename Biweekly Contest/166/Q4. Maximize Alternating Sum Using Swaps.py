# https://leetcode.com/contest/biweekly-contest-166/problems/maximize-alternating-sum-using-swaps/
from collections import defaultdict, deque
from typing import List


class Solution:
    def maxAlternatingSum(self, nums: List[int], swaps: List[List[int]]) -> int:
        n = len(nums)
        graph = defaultdict(list)
        for p, q in swaps:
            graph[p].append(q)
            graph[q].append(p)

        visited = [False] * n

        def bfs(start):
            q = deque([start])
            comp = []
            visited[start] = True
            while q:
                u = q.popleft()
                comp.append(u)
                for v in graph[u]:
                    if not visited[v]:
                        visited[v] = True
                        q.append(v)
            return comp

        arr = [0] * n
        for i in range(n):
            if not visited[i]:
                comp = bfs(i)
                values = [nums[j] for j in comp]

                comp.sort()
                values.sort(reverse=True)

                # evens first
                even_idx = [j for j in comp if j % 2 == 0]
                odd_idx = [j for j in comp if j % 2 == 1]
                even_idx.sort()
                odd_idx.sort()

                ptr = 0
                for j in even_idx:
                    arr[j] = values[ptr]
                    ptr += 1
                for j in odd_idx:
                    arr[j] = values[ptr]
                    ptr += 1

        ans = 0
        for i, v in enumerate(arr):
            if i % 2 == 0:
                ans += v
            else:
                ans -= v
        return ans
