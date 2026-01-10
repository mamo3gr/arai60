# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        def is_leaf(node: TreeNode) -> bool:
            return node.left is None and node.right is None

        if root is None:
            return 0

        to_visit = [root]
        depth = 1
        while to_visit:
            next_to_visit = []

            for node in to_visit:
                if is_leaf(node):
                    return depth
                for child in (node.left, node.right):
                    if child is None:
                        continue
                    next_to_visit.append(child)

            to_visit = next_to_visit
            depth += 1

        raise RuntimeError(
            "You can not reach here. There is something wrong in implementation."
        )

    def minDepthRecursion(self, root: Optional[TreeNode]) -> int:
        """再帰バージョン"""
        if root is None:
            return 0

        if root.left is None and root.right is None:  # root is leaf
            return 1

        child_depths = []
        for child in (root.left, root.right):
            if child is None:
                continue
            depth = self.minDepth(child)
            child_depths.append(depth)
        return min(child_depths) + 1

    def minDepthRecursion2(self, root: Optional[TreeNode]) -> int:
        """再帰はこんな書き方もできそう"""
        if root is None:
            return 0

        children = [node for node in (root.left, root.right) if node is not None]
        if not children:
            return 1

        child_depths = [self.minDepth(child) for child in children]
        return min(child_depths) + 1
