import functools


class Solution:
    def rob(self, nums: list[int]) -> int:
        if not nums:
            raise ValueError("nums must not be empty")

        @functools.cache
        def compute_total(i: int) -> int:
            """solve subproblem where nums = nums[:i+1]"""
            if i < 0:
                return 0

            if i == 0:
                return nums[0]

            return max(
                nums[i] + compute_total(i - 2),
                compute_total(i - 1),
            )

        return compute_total(len(nums) - 1)
