import math


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode | None) -> bool:
        if root is None:
            return True

        frontiers = [(root, -math.inf, math.inf)]
        while frontiers:
            node, lower, upper = frontiers.pop()

            if not (lower < node.val < upper):
                return False

            if node.left is not None:
                frontiers.append((node.left, lower, node.val))
            if node.right is not None:
                frontiers.append((node.right, node.val, upper))

        return True
