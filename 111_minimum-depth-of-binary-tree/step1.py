# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        def is_leaf(node) -> bool:
            return node.left is None and node.right is None

        if not root:
            return 0

        depth = 1
        to_visit = [root]
        while to_visit:
            next_to_visit = []

            for node in to_visit:
                if is_leaf(node):
                    return depth
                if node.left:
                    next_to_visit.append(node.left)
                if node.right:
                    next_to_visit.append(node.right)

            to_visit = next_to_visit
            depth += 1

        raise RuntimeError(
            "You can not reach here. There is something wrong in the implementation"
        )
