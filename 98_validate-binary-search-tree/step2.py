import math


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode | None) -> bool:
        """
        iterative, top-down
        これが一番しっくり来た
        """
        if root is None:
            return True

        frontiers = [(root, -math.inf, math.inf)]
        while frontiers:
            node, lower_limit, upper_limit = frontiers.pop()

            if not (lower_limit < node.val < upper_limit):
                return False

            if node.left is not None:
                frontiers.append((node.left, lower_limit, node.val))

            if node.right is not None:
                frontiers.append((node.right, node.val, upper_limit))

        return True

    def isValidBSTRecursiveTopdown(self, root: TreeNode | None) -> bool:
        def is_valid(
            node: TreeNode, lower_limit: int | float, upper_limit: int | float
        ) -> bool:
            if node is None:
                return True

            if not (lower_limit < node.val < upper_limit):
                return False

            left_valid = is_valid(node.left, lower_limit, node.val)
            right_valid = is_valid(node.right, node.val, upper_limit)
            return left_valid and right_valid

        return is_valid(root, -math.inf, math.inf)

    def isValidBSTGenerator(self, root: TreeNode | None) -> bool:
        if root is None:
            return True

        def traverse_inorder(node: TreeNode) -> Generator[int]:
            if node.left is not None:
                yield from traverse_inorder(node.left)
            yield node.val
            if node.right is not None:
                yield from traverse_inorder(node.right)

        previous_value = -math.inf
        for current_value in traverse_inorder(root):
            if not previous_value < current_value:
                return False
            previous_value = current_value

        return True

    def isValidBSTInorderIterative(self, root: TreeNode | None) -> bool:
        nodes_to_check = []
        lower_bound = -math.inf

        def push_it_and_left_children(node):
            while node:
                nodes_to_check.append(node)
                node = node.left

        push_it_and_left_children(root)
        while nodes_to_check:
            node = nodes_to_check.pop()
            if node.val <= lower_bound:
                return False

            lower_bound = node.val

            if node.right is not None:
                push_it_and_left_children(node.right)

        return True

    @dataclasses.dataclass
    class Bound:
        lower: int | float
        upper: int | float

    def isValidBSTBottomupIterative(self, root: TreeNode | None) -> bool:
        """
        以下のbottom-up, iterative実装を自分なりに整理したバージョン
        https://github.com/naoto-iwase/leetcode/pull/33/changes/BASE..2404c21c24a749b6f871d9030b7df0096beb856d#r2479195403
        """
        if root is None:
            return True

        frontiers = [root]
        subtree_to_bound: dict[TreeNode, Bound] = {}
        while frontiers:
            node = frontiers.pop()

            is_leaf = node.left is None and node.right is None
            if is_leaf:
                subtree_to_bound[node] = self.Bound(lower=node.val, upper=node.val)
                continue

            if node.left is not None:
                left_subtree_checked = node.left in subtree_to_bound
                if not left_subtree_checked:
                    frontiers.append(node)  # 左の部分木を処理した後で再訪問する
                    frontiers.append(node.left)
                    continue
                if not (subtree_to_bound[node.left].upper < node.val):
                    return False
            if node.right is not None:
                right_subtree_checked = node.right in subtree_to_bound
                if not right_subtree_checked:
                    frontiers.append(node)  # 右の部分木を処理した後で再訪問する
                    frontiers.append(node.right)
                    continue
                if not (node.val < subtree_to_bound[node.right].lower):
                    return False

            lower = node.val
            if node.left is not None:
                lower = subtree_to_bound[node.left].lower
                del subtree_to_bound[node.left]
            upper = node.val
            if node.right is not None:
                upper = subtree_to_bound[node.right].upper
                del subtree_to_bound[node.right]
            subtree_to_bound[node] = self.Bound(lower, upper)

        return True
