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
        """
        https://github.com/Shoichifunyu/shofun/pull/17 の解法を自分なりに整理したバージョン。
        root1, root2が非対称になっていて面白い。
        """
        if root1 is None and root2 is None:
            return None

        if root1 is None:
            return self.mergeTrees(root2, root1)

        merged = TreeNode(val=root1.val)

        # root1 is not None
        if root2 is None:
            merged.left = root1.left
            merged.right = root1.right
            return merged

        # both is not None
        merged.val += root2.val
        merged.left = self.mergeTrees(root1.left, root2.left)
        merged.right = self.mergeTrees(root1.right, root2.right)
        return merged
