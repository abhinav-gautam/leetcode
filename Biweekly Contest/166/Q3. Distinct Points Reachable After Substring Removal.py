# https://leetcode.com/contest/biweekly-contest-166/problems/distinct-points-reachable-after-substring-removal/


class Solution:
    def distinctPoints(self, s: str, k: int) -> int:
        n = len(s)

        move = {"U": (0, 1), "D": (0, -1), "L": (-1, 0), "R": (1, 0)}

        prefix = [(0, 0)]
        for ch in s:
            dx, dy = move[ch]
            px, py = prefix[-1]
            prefix.append((px + dx, py + dy))

        final_positions = set()

        for l in range(n - k + 1):
            skipx = prefix[l + k][0] - prefix[l][0]
            skipy = prefix[l + k][1] - prefix[l][1]

            finalx = prefix[n][0] - skipx
            finaly = prefix[n][1] - skipy

            final_positions.add((finalx, finaly))

        return len(final_positions)
