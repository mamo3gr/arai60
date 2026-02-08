class Solution:
    def search(self, nums: list[int], target: int) -> int:
        # leftとそれより左にはない
        # rightより右にはない
        left = -1
        right = len(nums)

        while right - left > 1:
            mid = left + (right - left) // 2
            if nums[mid] > nums[-1] and target <= nums[-1]:
                left = mid
                continue
            if nums[mid] <= nums[-1] and target > nums[-1]:
                right = mid
                continue

            if nums[mid] < target:
                left = mid
            else:
                right = mid

        if right < len(nums) and nums[right] == target:
            return right
        return -1
