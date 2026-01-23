class Solution:
    def rob(self, nums: list[int]) -> int:
        if not nums:
            raise ValueError("nums must not be empty")
        if len(nums) == 1:
            return nums[0]

        def compute_max_amount_linearly(begin: int, end: int) -> int:
            """solve for nums[begin:end+1] without circle constraint"""
            robbed_last = 0
            skipped_last = 0
            for i in range(begin, end + 1):
                robbed_last, skipped_last = (
                    skipped_last + nums[i],
                    max(robbed_last, skipped_last),
                )

            return max(robbed_last, skipped_last)

        return max(
            compute_max_amount_linearly(0, len(nums) - 2),
            compute_max_amount_linearly(1, len(nums) - 1),
        )
