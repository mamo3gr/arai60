class Solution:
    def findMin(self, nums: list[int]) -> int:
        if not nums:
            raise ValueError('nums must not be empty')

        no_rotation = nums[0] < nums[-1]
        if no_rotation:
            return nums[0]

        # invariant:
        # * for all 0 <= i <= first, nums[i] monotonically increases
        # * for all last <= i <= len(nums)-1, nums[i] monotonically increases
        first = 0
        last = len(nums) - 1
        while last - first > 1:
            mid = (first + last) // 2
            if nums[first] < nums[mid]:
                first = mid
            if nums[mid] < nums[last]:
                last = mid

        return nums[last]
