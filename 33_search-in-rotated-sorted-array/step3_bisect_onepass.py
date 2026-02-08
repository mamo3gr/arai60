import bisect


class Solution:
    def search(self, nums: list[int], target: int) -> int:
        def priority(x: int) -> tuple[bool, int]:
            return (x <= nums[-1], x)

        index = bisect.bisect_left(nums, priority(target), key=priority)
        if index < len(nums) and nums[index] == target:
            return index
        return -1
