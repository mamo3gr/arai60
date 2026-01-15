# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: list[int], inorder: list[int]) -> TreeNode | None:
        if not preorder:
            return None

        root_val = preorder[0]

        root_index = inorder.index(root_val)
        inorder_left = inorder[:root_index]
        inorder_right = inorder[root_index + 1 :]

        preorder_left = preorder[1 : len(inorder_left) + 1]
        preorder_right = preorder[len(inorder_left) + 1 :]

        return TreeNode(
            val=root_val,
            left=self.buildTree(preorder_left, inorder_left),
            right=self.buildTree(preorder_right, inorder_right),
        )
