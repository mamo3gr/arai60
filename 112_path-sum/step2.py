# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: TreeNode | None, targetSum: int) -> bool:
        if root is None:
            return False

        to_visit = [(root, 0)]
        while to_visit:
            node, total = to_visit.pop()
            total += node.val

            is_leaf = node.left is None and node.right is None
            if is_leaf and total == targetSum:
                return True

            if node.left is not None:
                to_visit.append((node.left, total))
            if node.right is not None:
                to_visit.append((node.right, total))

        return False
