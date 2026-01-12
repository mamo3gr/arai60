# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    INF = 2**32  # NOTE: -2**31 <= node.val <= 2**31 - 1

    def isValidBST(self, root: TreeNode | None) -> bool:
        def validate_and_get_min_max(node: TreeNode | None) -> tuple[bool, int, int]:
            if node is None:
                return True, self.INF, -self.INF

            is_leaf = node.left is None and node.right is None
            if is_leaf:
                return True, node.val, node.val

            left_is_bst, left_min, left_max = validate_and_get_min_max(node.left)
            right_is_bst, right_min, right_max = validate_and_get_min_max(node.right)
            return (
                left_is_bst and right_is_bst and left_max < node.val < right_min,
                min(left_min, node.val),
                max(right_max, node.val),
            )

        is_valid_bst, _, _ = validate_and_get_min_max(root)
        return is_valid_bst
