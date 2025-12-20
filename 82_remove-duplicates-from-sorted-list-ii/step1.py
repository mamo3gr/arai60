# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(next=head)
        node = dummy
        while node.next and node.next.next:
            if node.next.val != node.next.next.val:
                node = node.next
                continue
            
            duplicate_end = node.next
            while duplicate_end.next and duplicate_end.val == duplicate_end.next.val:
                duplicate_end = duplicate_end.next
            node.next = duplicate_end.next

        return dummy.next
