class Solution:
    def findMin(self, nums: list[int]) -> int:
        # invariant:
        # * for 0 <= i <= left,         nums[i] > nums[-1]
        # * for right <= i < len(nums), nums[i] <= nums[-1]
        left = -1
        right = len(nums)
        while right - left > 1:
            mid = left + (right - left) // 2
            if nums[mid] <= nums[-1]:
                right = mid
            else:
                left = mid

        return nums[right]
