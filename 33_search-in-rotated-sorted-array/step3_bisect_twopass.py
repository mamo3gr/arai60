import bisect


class Solution:
    def search(self, nums: list[int], target: int) -> int:
        min_index = bisect.bisect_left(nums, True, key=lambda x: x <= nums[-1])
        if target <= nums[-1]:
            lo, hi = min_index, len(nums)
        else:
            lo, hi = 0, min_index

        index = bisect.bisect_left(nums, target, lo=lo, hi=hi)
        if index < len(nums) and nums[index] == target:
            return index
        return -1
