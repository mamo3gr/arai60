import bisect
import itertools
import math


class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        """
        累積和と二分探索による実装。
        """
        prefix_sum = list(itertools.accumulate(nums))
        min_length = math.inf

        for start, start_num in enumerate(nums):
            complement = target - start_num
            last = bisect.bisect_left(
                prefix_sum,
                complement,
                lo=start,
                key=lambda p: p - prefix_sum[start],
            )
            if last < len(prefix_sum):
                length = last - start + 1
                min_length = min(min_length, length)

        if min_length == math.inf:
            return 0
        return min_length
