import math


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        start = last = 0
        total = nums[0]
        min_length = math.inf
        while start < len(nums):
            while total < target and last < len(nums) - 1:
                last += 1
                total += nums[last]

            if total >= target:
                length = last - start + 1
                min_length = min(min_length, length)
            else:
                break

            while total >= target and start <= last:
                total -= nums[start]
                start += 1
                if total >= target:
                    length = last - start + 1
                    min_length = min(min_length, length)

        if min_length == math.inf:
            return 0
        return min_length
