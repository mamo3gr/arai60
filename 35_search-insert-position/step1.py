class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        def search_interval(start: int, last: int) -> int:
            has_single_number = start >= last
            if has_single_number:
                if nums[start] < target:
                    return start + 1
                else:
                    return start

            mid = (last + start) // 2
            if nums[mid] == target:
                return mid
            if target < nums[mid]:
                return search_interval(start, mid - 1)
            if nums[mid] < target:
                return search_interval(mid + 1, last)

        return search_interval(start=0, last=len(nums) - 1)
