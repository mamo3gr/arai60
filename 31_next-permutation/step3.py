class Solution:
    def nextPermutation(self, nums: list[int]) -> None:
        def find_descending_start(nums: list[int]) -> int:
            i = len(nums) - 1
            while i > 0:
                if not nums[i - 1] >= nums[i]:
                    break
                i -= 1
            return i

        def reverse_interval(nums: list[int], left: int, right: int) -> None:
            while left < right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1

        pivot = find_descending_start(nums) - 1
        if pivot >= 0:
            j = len(nums) - 1
            while nums[j] <= nums[pivot]:
                j -= 1
            nums[pivot], nums[j] = nums[j], nums[pivot]
        reverse_interval(nums, pivot + 1, len(nums) - 1)
