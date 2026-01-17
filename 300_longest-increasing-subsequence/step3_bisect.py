import bisect
import math


class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:
        # minimum tail number of increasing sequence whose length is i
        sentinel = -math.inf
        min_tail_by_length = [sentinel]

        for num in nums:
            index = bisect.bisect_left(min_tail_by_length, num)
            if index >= len(min_tail_by_length):
                min_tail_by_length.append(num)
            else:
                min_tail_by_length[index] = min(min_tail_by_length[index], num)

        return len(min_tail_by_length) - 1
