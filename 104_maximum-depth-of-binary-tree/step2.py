# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def get_children(node: TreeNode) -> list[TreeNode]:
            children = (node.left, node.right)
            return [child for child in children if child is not None]

        if root is None:
            return 0

        to_visit = [root]
        depth = 1
        while True:
            next_to_visit = []
            for node in to_visit:
                next_to_visit.extend(get_children(node))

            if not next_to_visit:
                break

            to_visit = next_to_visit
            depth += 1

        return depth
