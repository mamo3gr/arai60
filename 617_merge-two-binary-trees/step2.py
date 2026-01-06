import collections


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    @staticmethod
    def get_val_left_right_safe(
        node: Optional[TreeNode],
    ) -> tuple[int, Optional[TreeNode], Optional[TreeNode]]:
        if node is None:
            return 0, None, None
        return node.val, node.left, node.right

    def mergeTrees(
        self, root1: Optional[TreeNode], root2: Optional[TreeNode]
    ) -> Optional[TreeNode]:
        if root1 is None and root2 is None:
            return None

        to_merge = collections.deque()
        merged_root = TreeNode()
        to_merge.append((root1, root2, merged_root))

        while to_merge:
            node1, node2, merged = to_merge.popleft()
            val1, left1, right1 = self.get_val_left_right_safe(node1)
            val2, left2, right2 = self.get_val_left_right_safe(node2)

            merged_left = None
            if left1 is not None or left2 is not None:
                merged_left = TreeNode()
                to_merge.append((left1, left2, merged_left))

            merged_right = None
            if right1 is not None or right2 is not None:
                merged_right = TreeNode()
                to_merge.append((right1, right2, merged_right))

            merged.val = val1 + val2
            merged.left = merged_left
            merged.right = merged_right

        return merged_root
