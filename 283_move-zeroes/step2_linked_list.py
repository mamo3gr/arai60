class Node:
    def __init__(self, val: int, next: Node | None = None):
        self.val = val
        self.next = next


class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Linked Listを利用した実装。
        補助空間計算量が O(N) 必要なので題意には沿わない。練習用。

        inspired from:
        https://github.com/hroc135/leetcode/pull/51#discussion_r2052911267
        """
        sentinel = Node(val=-1)
        node = sentinel
        for num in nums:
            node.next = Node(val=num)
            node = node.next

        tail = node
        node = sentinel
        for _ in range(len(nums) - 1):
            if node.next.val != 0:
                node = node.next
                continue

            node_next = node.next
            node.next = node.next.next
            tail.next = node_next
            tail = node_next
            tail.next = None

        node = sentinel.next
        for i in range(len(nums)):
            nums[i] = node.val
            node = node.next
