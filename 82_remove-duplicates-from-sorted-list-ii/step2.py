class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(next=head)
        last_fixed = dummy
        while last_fixed.next and last_fixed.next.next:
            if last_fixed.next.val != last_fixed.next.next.val:
                last_fixed = last_fixed.next
                continue
            
            connect_to = last_fixed.next
            while connect_to.next and connect_to.val == connect_to.next:
                connect_to = connect_to.next
            last_fixed.next = connect_to

        return dummy.next

