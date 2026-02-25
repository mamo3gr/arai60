class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        総当りなアプローチ。時間計算量は O(N^2) だがギリギリTLEしない。
        """
        for i in range(len(nums)):
            if nums[i] > 0:
                continue

            j = i
            while j < len(nums) and nums[j] == 0:
                j += 1

            if j == len(nums):  # no more non-zero numbers
                break

            nums[i], nums[j] = nums[j], nums[i]
