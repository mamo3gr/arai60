import heapq


class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = nums
        heapq.heapify(self.nums)
        self._cap_at_k()

    def add(self, val: int) -> int:
        heapq.heappush(self.nums, val)
        self._cap_at_k()
        return self.nums[0]

    def _cap_at_k(self):
        while len(self.nums) > self.k:
            heapq.heappop(self.nums)
