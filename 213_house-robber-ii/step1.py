import functools


class Solution:
    def rob(self, nums: list[int]) -> int:
        if len(nums) <= 3:
            # You choose only nums[0] or nums[1] or nums[2]
            return max(nums)

        return max(
            self.rob_sub(nums[:-1]),
            self.rob_sub(nums[1:]),
        )

    def rob_sub(self, nums: list[int]) -> int:

        @functools.cache
        def compute_max_amount(i: int) -> int:
            """max amount for nums[:i+1]"""
            if i < 0:
                return 0
            if i == 0:
                return nums[0]

            return max(
                compute_max_amount(i-2) + nums[i],
                compute_max_amount(i-1),
            )

        return compute_max_amount(len(nums)-1)
