from typing import List, Optional


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums:
            return None

        if len(nums) == 1:
            return TreeNode(val=nums[0])

        center_index = len(nums) // 2
        return TreeNode(
            val=nums[center_index],
            left=self.sortedArrayToBST(nums[:center_index]),
            right=self.sortedArrayToBST(nums[center_index + 1 :]),
        )
