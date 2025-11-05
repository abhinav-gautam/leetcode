# https://leetcode.com/problems/binary-tree-level-order-traversal/description/

from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue = [root]
        if not root:
            return []

        result = [[root.val]]

        while len(queue):
            size = len(queue)
            level = []
            for i in range(0, size):
                current = queue.pop(0)
                if current.left:
                    queue.append(current.left)
                    level.append(current.left.val)
                if current.right:
                    queue.append(current.right)
                    level.append(current.right.val)
            if len(level):
                result.append(level)
        return result
