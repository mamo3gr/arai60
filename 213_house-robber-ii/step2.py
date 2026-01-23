class Solution:
    def rob(self, nums: list[int]) -> int:
        if not nums:
            raise ValueError("nums must not be empty")

        if len(nums) <= 3:
            # You choose only nums[0] or nums[1] or nums[2]
            return max(nums)

        def rob_partial(begin: int, end: int) -> int:
            """solve for subarray nums[begin:end]"""
            robbed_last = 0
            skipped_last = 0

            for i in range(begin, end):
                next_robbed_last = skipped_last + nums[i]
                next_skipped_last = max(robbed_last, skipped_last)

                robbed_last = next_robbed_last
                skipped_last = next_skipped_last

            return max(robbed_last, skipped_last)

        return max(
            rob_partial(0, len(nums) - 1),
            rob_partial(1, len(nums)),
        )
