class Solution:
    def search(self, nums: list[int], target: int) -> int:
        # 不変条件：
        # * leftとそれより左にはtargetが存在しない。
        # * rightより右には、最も左のtargetが存在しない。
        left = -1
        right = len(nums)

        while right - left > 1:
            mid = left + (right - left) // 2

            left_sorted = nums[0] <= nums[mid]
            if left_sorted:
                if nums[0] <= target <= nums[mid]:
                    right = mid
                else:
                    left = mid
            else:  # right half sorted
                if nums[mid] < target <= nums[-1]:
                    left = mid
                else:
                    right = mid

        if right < len(nums) and nums[right] == target:
            return right
        return -1
