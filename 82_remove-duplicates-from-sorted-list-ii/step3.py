# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(next=head)
        last_fixed = dummy
        while last_fixed.next and last_fixed.next.next:
            if last_fixed.next.val != last_fixed.next.next.val:
                last_fixed = last_fixed.next
                continue
            
            val_to_delete = last_fixed.next.val
            skip_to = last_fixed.next
            while skip_to and skip_to.val == val_to_delete:
                skip_to = skip_to.next
            last_fixed.next = skip_to
                        
        return dummy.next
