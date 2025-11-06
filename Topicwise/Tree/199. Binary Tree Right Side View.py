# https://leetcode.com/problems/binary-tree-right-side-view/description/
from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        q = [root]

        if not root:
            return []

        result = []

        while q:
            size = len(q)
            for i in range(size):
                current = q.pop(0)
                if i == size - 1:
                    result.append(current.val)
                if current.left:
                    q.append(current.left)
                if current.right:
                    q.append(current.right)
        return result
