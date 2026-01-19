class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        cumulated = 0
        max_sum = -math.inf
        for num in nums:
            cumulated += num
            max_sum = max(max_sum, cumulated)
            if cumulated < 0:
                cumulated = 0

        return max_sum
