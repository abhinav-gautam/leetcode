# https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/description/

from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        queue = [root]
        level = 1
        result = [[root.val]]

        while len(queue):
            nodes = []
            level += 1

            for _ in range(len(queue)):
                node = queue.pop(0)

                if node.left:
                    queue.append(node.left)
                    nodes.append(node.left.val)

                if node.right:
                    queue.append(node.right)
                    nodes.append(node.right.val)
            if len(nodes):
                if level % 2:
                    result.append(nodes)
                else:
                    result.append(nodes[::-1])

        return result
