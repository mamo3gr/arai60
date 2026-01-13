# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: TreeNode | None) -> list[list[int]]:
        """
        悪い例。
        選択肢の幅出しのために深さごとの再帰で書いてみたが、特にメリットは感じなかった
        （iterativeな実装で差し支えない）。
        また、ノードの走査そのものを逆順にしてみたが、何箇所かで分岐処理が必要で煩雑。
        """
        if root is None:
            return []

        values_by_level = []

        def collect_level_values(nodes: list[TreeNode], reverse: bool) -> None:
            if reverse:
                nodes = reversed(nodes)

            values = []
            next_level = []
            for node in nodes:
                values.append(node.val)

                children = (node.left, node.right)
                if reverse:
                    children = reversed(children)
                for child in children:
                    if child is None:
                        continue
                    next_level.append(child)

            values_by_level.append(values)

            if reverse:
                next_level = list(reversed(next_level))
            if next_level:
                collect_level_values(next_level, not reverse)

        collect_level_values([root], reverse=False)
        return values_by_level

    def zigzagLevelOrderReverseOrderValue(
        self, root: TreeNode | None
    ) -> list[list[int]]:
        """値のリストアップにて、アクセスするインデックス順を変えるパターン"""
        if root is None:
            return []

        nodes = [root]
        values_by_level = []
        left_to_right = True
        while nodes:
            values = [0] * len(nodes)
            next_level = []

            for i, node in enumerate(nodes):
                value_i = i if left_to_right else -1 - i
                values[value_i] = node.val

                if node.left is not None:
                    next_level.append(node.left)
                if node.right is not None:
                    next_level.append(node.right)

            values_by_level.append(values)
            nodes = next_level
            left_to_right = not left_to_right

        return values_by_level
