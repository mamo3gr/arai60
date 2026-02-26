class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        non_zero_placed_at = 0

        for i in range(len(nums)):
            if nums[i] != 0:
                nums[i], nums[non_zero_placed_at] = nums[non_zero_placed_at], nums[i]
                non_zero_placed_at += 1
