import dataclasses


class Solution:
    @dataclasses.dataclass(frozen=True)
    class IncreasingSequence:
        tail: int
        length: int

    def lengthOfLIS(self, nums: list[int]) -> int:
        if not nums:
            raise ValueError("Array must not be empty")

        sequences = [
            self.IncreasingSequence(tail=nums[0], length=1),
        ]
        for n in nums:
            length_tail_n = 1

            for s in sequences:
                if s.tail < n:
                    length_tail_n = max(s.length + 1, length_tail_n)

            sequences.append(
                self.IncreasingSequence(
                    tail=n,
                    length=length_tail_n,
                )
            )

        return max(s.length for s in sequences)
