class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        start = 0
        total = 0
        min_length = len(nums) + 1
        for last, num in enumerate(nums):
            total += num

            while total >= target:
                length = last - start + 1
                min_length = min(min_length, length)
                total -= nums[start]
                start += 1

        return min_length if min_length <= len(nums) else 0
