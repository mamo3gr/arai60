from typing import List, Optional, Tuple


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        root = TreeNode()
        to_build: List[Tuple[TreeNode, List[int]]] = []
        to_build.append((root, nums))
        while to_build:
            node, array = to_build.pop()
            center_index = len(array) // 2
            node.val = array[center_index]

            left_array = array[:center_index]
            if left_array:
                node.left = TreeNode()
                to_build.append((node.left, left_array))

            right_array = array[center_index + 1 :]
            if right_array:
                node.right = TreeNode()
                to_build.append((node.right, right_array))

        return root

    def sortedArrayToBSTByIndex(self, nums: List[int]) -> Optional[TreeNode]:
        """配列そのものではなく範囲のインデックスを使うバージョン"""
        root = TreeNode()
        to_build: List[Tuple[TreeNode, int, int]] = []
        to_build.append((root, 0, len(nums) - 1))
        while to_build:
            node, start_index, last_index = to_build.pop()
            center_index = (start_index + last_index) // 2
            node.val = nums[center_index]

            left_array_exists = start_index <= center_index - 1
            if left_array_exists:
                node.left = TreeNode()
                to_build.append((node.left, start_index, center_index - 1))

            right_array_exists = center_index + 1 <= last_index
            if right_array_exists:
                node.right = TreeNode()
                to_build.append((node.right, center_index + 1, last_index))

        return root
