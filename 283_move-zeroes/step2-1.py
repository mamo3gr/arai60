class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        nonzero_index = 0

        for i, num in enumerate(nums):
            if num != 0:
                continue

            if nonzero_index < i:
                nonzero_index = i + 1

            while nonzero_index < len(nums) and nums[nonzero_index] == 0:
                nonzero_index += 1
            if nonzero_index >= len(nums):
                break  # no more non-zero elements remained

            nums[i], nums[nonzero_index] = nums[nonzero_index], nums[i]
