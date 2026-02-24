class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        for i in range(len(nums)):
            if nums[i] > 0:
                continue

            j = i
            while j < len(nums) and nums[j] == 0:
                j += 1

            if j == len(nums):  # no more positive numbers
                return

            nums[i], nums[j] = nums[j], nums[i]
