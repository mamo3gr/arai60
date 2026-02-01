class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        start = 0
        last = len(nums) - 1
        while start <= last:
            mid = (start + last) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] < target:
                start = mid + 1
            if target < nums[mid]:
                last = mid - 1

        return start
