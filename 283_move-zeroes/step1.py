import collections


class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        zero_indices = collections.deque()
        for i, num in enumerate(nums):
            if num == 0:
                zero_indices.append(i)
                continue

            if zero_indices:
                zero_index = zero_indices.popleft()
                nums[i], nums[zero_index] = nums[zero_index], nums[i]
                zero_indices.append(i)
