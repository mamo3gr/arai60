import dataclasses


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
@dataclasses.dataclass
class Span:
    begin: int
    end: int

    def length(self) -> int:
        return self.end - self.begin

    def is_empty(self) -> bool:
        return self.length() <= 0


class Solution:
    def buildTree(self, preorder: list[int], inorder: list[int]) -> TreeNode | None:
        if not preorder or not inorder:
            raise ValueError("Arrays must not be empty")

        if len(preorder) != len(inorder):
            raise ValueError("Length of arrays must be the same")

        num_to_index = {num: i for i, num in enumerate(inorder)}
        root = TreeNode()
        frontier = [
            (
                root,
                Span(0, len(preorder)),
                Span(0, len(inorder)),
            )
        ]

        while frontier:
            node, preorder_span, inorder_span = frontier.pop()
            node.val = preorder[preorder_span.begin]

            index = num_to_index[node.val]
            inorder_left = Span(inorder_span.begin, index)
            inorder_right = Span(index + 1, inorder_span.end)

            left_size = inorder_left.length()
            preorder_left = Span(
                preorder_span.begin + 1, preorder_span.begin + 1 + left_size
            )
            right_size = inorder_right.length()
            preorder_right = Span(preorder_span.end - right_size, preorder_span.end)

            if left_size > 0:
                node.left = TreeNode()
                frontier.append((node.left, preorder_left, inorder_left))
            if right_size > 0:
                node.right = TreeNode()
                frontier.append((node.right, preorder_right, inorder_right))

        return root
