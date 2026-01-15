# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: list[int], inorder: list[int]) -> TreeNode | None:
        if len(preorder) != len(inorder):
            raise ValueError("Length of two inputs must be the same")

        dummy = TreeNode(val=None)
        potential_parents = [dummy]
        inorder_i = 0
        for preorder_value in preorder:
            new_node = TreeNode(val=preorder_value)

            reach_leftmost = potential_parents[-1].val == inorder[inorder_i]
            if not reach_leftmost:
                potential_parents[-1].left = new_node
                potential_parents.append(new_node)
                continue

            parent_of_right_child = None
            while potential_parents:
                parent_of_right_child = potential_parents.pop()
                inorder_i += 1
                if potential_parents[-1].val != inorder[inorder_i]:
                    break

            assert parent_of_right_child is not None
            parent_of_right_child.right = new_node
            potential_parents.append(new_node)

        return dummy.left
