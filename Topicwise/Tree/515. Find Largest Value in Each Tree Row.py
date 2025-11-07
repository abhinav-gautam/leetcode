# https://leetcode.com/problems/find-largest-value-in-each-tree-row/description/

from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        queue = [root]

        if not root:
            return []

        result = []

        while len(queue):
            size = len(queue)
            maxValue = float("-inf")

            for i in range(size):
                current = queue.pop(0)
                maxValue = max(maxValue, current.val)

                if current.left:
                    queue.append(current.left)

                if current.right:
                    queue.append(current.right)

            result.append(maxValue)

        return result
