class Solution:
    def findMin(self, nums: list[int]) -> int:
        """
        両方とも開区間を考えて、それを狭めていくイメージ。
        回転数n（回転なし）のときにも対応できる。
        inspired from
        https://github.com/garunitule/coding_practice/pull/42/changes#r2633235874
        """
        if not nums:
            raise ValueError('nums must not be empty')

        left = -1
        right = len(nums)
        while right - left > 1:
            mid = (left + right) // 2
            if nums[left] < nums[mid]:
                left = mid
            else:
                right = mid

        return nums[right]
