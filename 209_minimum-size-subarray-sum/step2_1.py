import math


class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        start = 0
        total = 0
        min_length = math.inf
        for last in range(len(nums)):
            total += nums[last]

            while start <= last:
                if total >= target:
                    length = last - start + 1
                    min_length = min(min_length, length)
                    total -= nums[start]
                    start += 1
                else:
                    break

        if min_length == math.inf:
            return 0
        return min_length
