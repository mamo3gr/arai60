# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: TreeNode | None) -> list[list[int]]:
        if root is None:
            return []

        frontiers = [root]
        right_to_left = False
        values_by_level = []
        while frontiers:
            values = [node.val for node in frontiers]
            if right_to_left:
                values = list(reversed(values))

            next_frontiers = []
            for node in frontiers:
                if node.left is not None:
                    next_frontiers.append(node.left)
                if node.right is not None:
                    next_frontiers.append(node.right)

            values_by_level.append(values)
            frontiers = next_frontiers
            right_to_left = not right_to_left

        return values_by_level
