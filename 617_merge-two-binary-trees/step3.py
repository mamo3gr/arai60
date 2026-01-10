import copy


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTreesRecursive(
        self, root1: Optional[TreeNode], root2: Optional[TreeNode]
    ) -> Optional[TreeNode]:
        """再帰による実装。どちらかというとこっち方がしっくりくる"""
        if root1 is None and root2 is None:
            return None

        if root1 is not None and root2 is None:
            return copy.deepcopy(root1)

        if root1 is None and root2 is not None:
            return copy.deepcopy(root2)

        return TreeNode(
            val=root1.val + root2.val,
            left=self.mergeTrees(root1.left, root2.left),
            right=self.mergeTrees(root1.right, root2.right),
        )

    """
    ここから別解
    """

    @staticmethod
    def _get_val_left_right_safe(node: Optional[TreeNode]):
        if node is None:
            return 0, None, None
        return node.val, node.left, node.right

    def mergeTreesWithStack(
        self, root1: Optional[TreeNode], root2: Optional[TreeNode]
    ) -> Optional[TreeNode]:
        """スタックを用いた実装"""
        if root1 is None and root2 is None:
            return None

        merged_root = TreeNode()
        to_merge = [(root1, root2, merged_root)]

        while to_merge:
            node1, node2, merged = to_merge.pop()
            val1, left1, right1 = self._get_val_left_right_safe(node1)
            val2, left2, right2 = self._get_val_left_right_safe(node2)

            merged.val = val1 + val2

            if left1 is not None or left2 is not None:
                merged.left = TreeNode()
                to_merge.append((left1, left2, merged.left))
            if right1 is not None or right2 is not None:
                merged.right = TreeNode()
                to_merge.append((right1, right2, merged.right))

        return merged_root
