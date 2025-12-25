import heapq


class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.top_k_ascending = []
        heapq.heapify(self.top_k_ascending)
        for n in nums:
            self.add(n)

    def add(self, val: int) -> int:
        heapq.heappush(self.top_k_ascending, val)
        while len(self.top_k_ascending) > self.k:
            heapq.heappop(self.top_k_ascending)
        return self.top_k_ascending[0]

