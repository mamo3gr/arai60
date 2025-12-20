class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node = head
        previous = None
        while node:
            forward = node.next

            node.next = previous

            previous = node
            node = forward

        return previous
