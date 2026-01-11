# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: TreeNode | None) -> list[list[int]]:
        if root is None:
            return []

        values = []

        def traverse(node: TreeNode, level: int) -> None:
            if level >= len(values):
                values.append([])
            values[level].append(node.val)

            if node.left is not None:
                traverse(node.left, level + 1)
            if node.right is not None:
                traverse(node.right, level + 1)

        traverse(root, 0)
        return values
