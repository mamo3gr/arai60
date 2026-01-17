import bisect
import math


class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:
        # t[i] is tail number of LIS whose length is i
        tails_by_lis_length = [-math.inf]
        for n in nums:
            length_tail_n = bisect.bisect_left(tails_by_lis_length, n)
            if length_tail_n < len(tails_by_lis_length):
                tails_by_lis_length[length_tail_n] = n
            else:
                tails_by_lis_length.append(n)

        return len(tails_by_lis_length) - 1
