import dataclasses


class Solution:
    @dataclasses.dataclass
    class IncreasingSequence:
        tail: int
        length: int

    def lengthOfLIS(self, nums: list[int]) -> int:
        sequences = []
        max_length = 0
        for n in nums:
            length_tail_n = 1
            for s in sequences:
                if s.tail < n:
                    length_tail_n = max(length_tail_n, s.length + 1)
            sequences.append(self.IncreasingSequence(tail=n, length=length_tail_n))
            max_length = max(max_length, length_tail_n)

        return max_length
