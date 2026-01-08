class PriorityQueue:
    def __init__(self):
        self.heap = []

    def push(self, val):
        self.heap.append(val)
        self._up_heap(len(self.heap) - 1)

    def pop(self):
        if self.is_empty():
            raise ValueError("Heap is empty")

        root_value = self.heap[0]
        last_value = self.heap.pop()
        if not self.is_empty():
            self.heap[0] = last_value
            self._down_heap(0)

        return root_value

    def is_empty(self):
        return len(self.heap) == 0

    def peek(self):
        if self.is_empty():
            raise ValueError("Heap is empty")
        return self.heap[0]

    def __len__(self):
        return len(self.heap)

    def _up_heap(self, index: int):
        """指定した位置の要素を、親と比較しながら正しい位置まで「浮上」させる。"""
        while index > 0:
            parent_index = (index - 1) // 2
            if self.heap[parent_index] > self.heap[index]:
                self.heap[parent_index], self.heap[index] = (
                    self.heap[index],
                    self.heap[parent_index],
                )
                index = parent_index
            else:
                break

    def _down_heap(self, index):
        """根に持ってきた要素を、子と比較しながら正しい位置まで「下降」させる。"""
        while index < len(self.heap):
            left_index = 2 * index + 1
            right_index = 2 * index + 2

            smallest_index = index
            if (
                left_index < len(self.heap)
                and self.heap[left_index] < self.heap[smallest_index]
            ):
                smallest_index = left_index
            if (
                right_index < len(self.heap)
                and self.heap[right_index] < self.heap[smallest_index]
            ):
                smallest_index = right_index

            if smallest_index == index:
                break
            else:
                self.heap[index], self.heap[smallest_index] = (
                    self.heap[smallest_index],
                    self.heap[index],
                )
                index = smallest_index


class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.top_k_heap = PriorityQueue()
        for n in nums:
            self.add(n)

    def add(self, val: int) -> int:
        self.top_k_heap.push(val)
        while len(self.top_k_heap) > self.k:
            self.top_k_heap.pop()
        return self.top_k_heap.peek()


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
