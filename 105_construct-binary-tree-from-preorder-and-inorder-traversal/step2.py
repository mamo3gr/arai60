import dataclasses


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
@dataclasses.dataclass(frozen=True)
class Span:
    begin: int
    end: int

    def length(self) -> int:
        return self.end - self.begin

    def is_empty(self) -> bool:
        return self.length() <= 0


class Solution:
    def buildTree(self, preorder: list[int], inorder: list[int]) -> TreeNode | None:
        # O(1) to find index for a number
        num_to_index = {num: i for i, num in enumerate(inorder)}

        def helper(preorder_span: Span, inorder_span: Span) -> TreeNode | None:
            if preorder_span.is_empty():
                return None

            root_val = preorder[preorder_span.begin]
            root_index = num_to_index[root_val]

            inorder_left = Span(inorder_span.begin, root_index)
            inorder_right = Span(root_index + 1, inorder_span.end)

            left_size = root_index - inorder_span.begin
            right_size = inorder_span.length() - left_size - 1
            preorder_left = Span(
                preorder_span.begin + 1, preorder_span.begin + 1 + left_size
            )
            preorder_right = Span(preorder_span.end - right_size, preorder_span.end)

            return TreeNode(
                val=root_val,
                left=helper(preorder_left, inorder_left),
                right=helper(preorder_right, inorder_right),
            )

        return helper(
            Span(0, len(preorder)),
            Span(0, len(inorder)),
        )

    def buildTreeIterative(
        self, preorder: list[int], inorder: list[int]
    ) -> TreeNode | None:
        """Iterativeにも書き換えてみたパターン"""

        # O(1) to find index for a number
        num_to_index = {num: i for i, num in enumerate(inorder)}

        root = TreeNode()
        frontier = [
            (
                root,
                Span(0, len(preorder)),
                Span(0, len(inorder)),
            ),
        ]

        while frontier:
            node, preorder_span, inorder_span = frontier.pop()

            node.val = preorder[preorder_span.begin]
            node_index = num_to_index[node.val]

            inorder_left = Span(inorder_span.begin, node_index)
            inorder_right = Span(node_index + 1, inorder_span.end)

            left_size = node_index - inorder_span.begin
            right_size = inorder_span.length() - left_size - 1
            preorder_left = Span(
                preorder_span.begin + 1, preorder_span.begin + 1 + left_size
            )
            preorder_right = Span(preorder_span.end - right_size, preorder_span.end)

            if not preorder_left.is_empty():
                node.left = TreeNode()
                frontier.append((node.left, preorder_left, inorder_left))
            if not preorder_right.is_empty():
                node.right = TreeNode()
                frontier.append((node.right, preorder_right, inorder_right))

        return root
