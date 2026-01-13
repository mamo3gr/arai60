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

        nodes = [root]
        right_to_left = False
        values_by_level = []
        while nodes:
            values = [node.val for node in nodes]
            if right_to_left:
                values.reverse()
            values_by_level.append(values)

            next_level = []
            for node in nodes:
                if node.left is not None:
                    next_level.append(node.left)
                if node.right is not None:
                    next_level.append(node.right)

            nodes = next_level
            right_to_left = not right_to_left

        return values_by_level
