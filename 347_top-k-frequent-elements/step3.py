from collections import defaultdict


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_count = defaultdict(int)
        for n in nums:
            num_count[n] += 1

        nums_frequent_order = sorted(num_count, key=num_count.get, reverse=True)
        return nums_frequent_order[:k]
