import collections


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequent = collections.Counter(nums)
        return [n for n, _ in frequent.most_common(k)]
