import math


class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        cumulative_sum = 0
        max_cumulative_sum = -math.inf
        min_cumulative_sum = math.inf

        for num in nums:
            cumulative_sum += num  # c[i]

            max_cumulative_sum = max(
                max_cumulative_sum,
                cumulative_sum,
                cumulative_sum - min_cumulative_sum,  # c[i] - min(c[j])
            )

            # update min(c[j])
            min_cumulative_sum = min(min_cumulative_sum, cumulative_sum)

        return max_cumulative_sum
