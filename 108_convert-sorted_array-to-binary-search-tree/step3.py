from typing import List, Optional


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def build_tree(start_index: int, last_index: int) -> Optional[TreeNode]:
            if last_index < start_index:
                return None

            middle_index = (start_index + last_index) // 2
            if start_index == last_index:
                return TreeNode(val=nums[middle_index])

            return TreeNode(
                val=nums[middle_index],
                left=build_tree(start_index, middle_index - 1),
                right=build_tree(middle_index + 1, last_index),
            )

        return build_tree(0, len(nums) - 1)

    def sortedArrayToBSTWithStack(self, nums: List[int]) -> Optional[TreeNode]:
        """スタックを使った実装"""
        root = TreeNode()
        to_configure = [(root, 0, len(nums) - 1)]
        while to_configure:
            node, start_index, last_index = to_configure.pop()

            middle_index = (start_index + last_index) // 2
            node.val = nums[middle_index]

            left_child_exists = start_index <= middle_index - 1
            if left_child_exists:
                node.left = TreeNode()
                to_configure.append((node.left, start_index, middle_index - 1))

            right_child_exists = middle_index + 1 <= last_index
            if right_child_exists:
                node.right = TreeNode()
                to_configure.append((node.right, middle_index + 1, last_index))

        return root
