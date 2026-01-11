import collections


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

        nodes_to_traverse = [root]
        level = 0
        values = []
        while nodes_to_traverse:
            next_to_traverse = []
            values_for_level = []

            for node in nodes_to_traverse:
                values_for_level.append(node.val)
                if node.left:
                    next_to_traverse.append(node.left)
                if node.right:
                    next_to_traverse.append(node.right)

            values.append(values_for_level)
            level += 1
            nodes_to_traverse = next_to_traverse

        return values

    def levelOrderQueue(self, root: TreeNode | None) -> list[list[int]]:
        """キューに (ノード, 深さ) を入れる別解"""
        if root is None:
            return []

        node_and_level = collections.deque([(root, 0)])
        values = []
        while node_and_level:
            node, level = node_and_level.popleft()
            if level >= len(values):
                values.append([])
            values[level].append(node.val)

            if node.left:
                node_and_level.append((node.left, level + 1))
            if node.right:
                node_and_level.append((node.right, level + 1))

        return values
