# https://leetcode.com/problems/maximum-level-sum-of-a-binary-tree/description/

from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        queue = [root]
        maxLevel = 1
        maxSum = root.val

        level = 1
        while len(queue):
            sum = 0
            for i in range(len(queue)):
                node = queue.pop(0)
                sum += node.val

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            if sum > maxSum:
                maxLevel = level
                maxSum = sum

            level += 1
        return maxLevel
