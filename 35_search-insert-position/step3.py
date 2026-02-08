class Solution:
    def searchInsertCloseOpenedInterval(self, nums: list[int], target: int) -> int:
        """半開区間で開始するバージョン"""
        begin = 0
        end = len(nums)
        while begin < end:
            mid = (begin + end) // 2
            if nums[mid] < target:
                begin = mid + 1
            else:
                end = mid

        return begin

    def searchInsertClosedInterval(self, nums: list[int], target: int) -> int:
        """閉区間から開始するバージョン"""
        first = 0
        last = len(nums) - 1
        while first <= last:
            mid = (first + last) // 2
            if nums[mid] < target:
                first = mid + 1
            else:
                # target <= nums[mid] だから、midまでしか詰められなくない？と思ってしまう
                last = mid - 1

        return first

