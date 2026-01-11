# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root is None:
            return False

        is_leaf = root.left is None and root.right is None
        if is_leaf:
            return root.val == targetSum

        child_target_sum = targetSum - root.val
        return self.hasPathSum(root.left, child_target_sum) or self.hasPathSum(
            root.right, child_target_sum
        )
