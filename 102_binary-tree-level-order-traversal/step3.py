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

        values_by_level = []
        current_level = [root]
        while current_level:
            values = []
            next_level = []

            for node in current_level:
                values.append(node.val)
                if node.left is not None:
                    next_level.append(node.left)
                if node.right is not None:
                    next_level.append(node.right)

            values_by_level.append(values)
            current_level = next_level

        return values_by_level

    def levelOrderRecursiveByNode(self, root: Optional[TreeNode]) -> List[List[int]]:
        """
        ノードごとに再帰するパターン。
        個人的に、while文の意図が分かりにくいこと、この再帰でlevel orderになるか
        考えてしまうことから、幅として書いてみたが実際には選ばないと思う。
        """
        if root is None:
            return []

        values_by_level = []

        def traverse(node: TreeNode, level: int) -> None:
            while len(values_by_level) <= level:
                values_by_level.append([])
            values_by_level[level].append(node.val)

            if node.left is not None:
                traverse(node.left, level + 1)
            if node.right is not None:
                traverse(node.right, level + 1)

        traverse(root, level=0)
        return values_by_level

    def levelOrderRecursiveByLevel(self, root: TreeNode | None) -> list[list[int]]:
        """深さごとに再帰するパターン。冒頭のBFSに対応する"""
        if root is None:
            return []

        values_by_level = []

        def collect_level_values(nodes: list[TreeNode]) -> None:
            values = []
            next_level = []
            for node in nodes:
                values.append(node.val)
                if node.left is not None:
                    next_level.append(node.left)
                if node.right is not None:
                    next_level.append(node.right)
            values_by_level.append(values)

            if next_level:
                collect_level_values(next_level)

        collect_level_values([root])
        return values_by_level
