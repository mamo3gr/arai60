import bisect


class Solution:
    def search(self, nums: list[int], target: int) -> int:
        min_index = bisect.bisect_left(nums, True, key=lambda x: x <= nums[-1])
        # search in nums[:min_index]
        index = bisect.bisect_left(nums, target, lo=0, hi=min_index)
        if index < min_index and nums[index] == target:
            return index
        # search in nums[min_index:]
        index = bisect.bisect_left(nums, target, lo=min_index)
        if index < len(nums) and nums[index] == target:
            return index

        return -1
