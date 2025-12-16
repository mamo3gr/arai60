# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def find_confluent_node(head) -> Optional[ListNode]:
            fast = head
            slow = head
            while fast and fast.next:
                fast = fast.next.next
                slow = slow.next
                if fast == slow:
                    return fast
            return None

        fast = find_confluent_node(head)
        if fast is None:
            return None

        slow = head
        while fast != slow:
            fast = fast.next
            slow = slow.next

        return slow
