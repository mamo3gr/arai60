# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(
        self, root1: Optional[TreeNode], root2: Optional[TreeNode]
    ) -> Optional[TreeNode]:
        def get_val_left_right_safe(
            node: Optional[TreeNode],
        ) -> tuple[int, Optional[TreeNode], Optional[TreeNode]]:
            if node is None:
                return 0, None, None
            return node.val, node.left, node.right

        if root1 is None and root2 is None:
            return None

        val1, left1, right1 = get_val_left_right_safe(root1)
        val2, left2, right2 = get_val_left_right_safe(root2)
        return TreeNode(
            val=val1 + val2,
            left=self.mergeTrees(left1, left2),
            right=self.mergeTrees(right1, right2),
        )
