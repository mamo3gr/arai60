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

        child_depths = []
        for child in (root.left, root.right):
            if child is None:
                continue
            depth = self.maxDepth(child)
            child_depths.append(depth)

        return max(child_depths) + 1
