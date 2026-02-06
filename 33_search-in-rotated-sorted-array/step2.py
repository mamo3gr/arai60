import bisect


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        min_index = bisect.bisect_left(nums, True, key=lambda x: x <= nums[-1])
        if target <= nums[-1]:
            index = bisect.bisect_left(nums, target, lo=min_index)
            if index < len(nums) and nums[index] == target:
                return index
            else:
                return -1

        index = bisect.bisect_left(nums, target, hi=min_index)
        if index < min_index and nums[index] == target:
            return index
        else:
            return -1
