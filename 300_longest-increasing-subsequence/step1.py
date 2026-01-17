import math


class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:
        n = len(nums)
        # length of increasing length with starting nums[i]
        sequence_length = {n - 1: 1}
        max_length = sequence_length[n - 1]

        for i in reversed(range(0, n - 1)):
            sequence_length_i = 1

            for j in range(i + 1, n):
                if nums[i] < nums[j]:
                    sequence_length_i = max(
                        sequence_length_i,
                        sequence_length[j] + 1,
                    )

            sequence_length[i] = sequence_length_i
            max_length = max(max_length, sequence_length_i)

        return max_length
