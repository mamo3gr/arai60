class Solution:
    def rob(self, nums: list[int]) -> int:
        if not nums:
            raise ValueError("nums must not be empty")
        if len(nums) <= 2:
            return max(nums)

        robbed_last = 0
        skipped_last = 0
        for num in nums:
            next_robbed_last = num + skipped_last
            next_skipped_last = max(robbed_last, skipped_last)

            robbed_last = next_robbed_last
            skipped_last = next_skipped_last

        return max(robbed_last, skipped_last)
