from collections import defaultdict


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        number2frequency = defaultdict(int)
        for n in nums:
            number2frequency[n] += 1

        numbers_frequent_order = sorted(
            number2frequency, key=number2frequency.get, reverse=True
        )
        return numbers_frequent_order[:k]
