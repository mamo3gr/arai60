import functools


class Solution:
    def rob(self, nums: list[int]) -> int:
        if not nums:
            raise ValueError("nums must not be empty")
        if len(nums) == 1:
            return nums[0]

        return max(
            self.compute_max_amount_linearly(nums[:-1]),
            self.compute_max_amount_linearly(nums[1:]),
        )

    @staticmethod
    def compute_max_amount_linearly(nums: list[int]) -> int:
        @functools.cache
        def compute_max_amount_partially(i: int) -> int:
            """solve for nums[:i+1]"""
            if i < 0:
                return 0
            if i == 0:
                return nums[0]

            return max(
                compute_max_amount_partially(i - 2) + nums[i],
                compute_max_amount_partially(i - 1),
            )

        return compute_max_amount_partially(len(nums) - 1)
