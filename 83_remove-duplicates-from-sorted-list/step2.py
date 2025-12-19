# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node = head
        while node:
            next_distinct = node
            while next_distinct and next_distinct.val == node.val:
                next_distinct = next_distinct.next
            node.next = next_distinct
            node = node.next

        return head
