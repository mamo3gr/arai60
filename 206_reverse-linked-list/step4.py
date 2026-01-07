from typing import Optional


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """帰りがけの再帰"""
        if head is None:
            return head

        if head.next is None:
            return head

        reversed_head = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return reversed_head

    def reverseList2(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """行きがけの再帰"""
        if head is None:
            return None

        def reverse_and_prepend(nodes_to_reverse, base_list):
            if nodes_to_reverse is None:
                return base_list

            delegate_to = nodes_to_reverse.next
            nodes_to_reverse.next = base_list
            return reverse_and_prepend(delegate_to, nodes_to_reverse)

        return reverse_and_prepend(head, None)
