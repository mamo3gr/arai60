# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        if root.left is None and root.right is None:
            return 1

        child_depth = []
        for child in (root.left, root.right):
            depth = self.maxDepth(child)
            child_depth.append(depth)
        return max(child_depth) + 1
