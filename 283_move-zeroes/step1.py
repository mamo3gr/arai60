class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        nonzero_index = 0
        zero_index = 0

        while nonzero_index < len(nums) and zero_index < len(nums):
            while zero_index < len(nums) and nums[zero_index] != 0:
                zero_index += 1
            if zero_index >= len(nums):
                return

            while nonzero_index < len(nums) and nums[nonzero_index] == 0:
                nonzero_index += 1
            if nonzero_index >= len(nums):
                return

            if zero_index < nonzero_index:
                nums[zero_index], nums[nonzero_index] = (
                    nums[nonzero_index],
                    nums[zero_index],
                )
            else:
                nonzero_index = zero_index
