class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        next_non_zero_placed_at = 0
        for i, num in enumerate(nums):
            if num != 0:
                nums[i], nums[next_non_zero_placed_at] = nums[next_non_zero_placed_at], nums[i]
                next_non_zero_placed_at += 1
