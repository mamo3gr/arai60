# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        dummy = ListNode()

        last_fixed = dummy
        n1 = l1
        n2 = l2
        carry = 0
        while n1 or n2:
            if n1 and n2 is None:
                total = n1.val + carry
                if total >= 10:
                    total -= 10
                    carry = 1
                else:
                    carry = 0
                last_fixed.next = ListNode(val=total)
                last_fixed = last_fixed.next
                n1 = n1.next
            elif n1 is None and n2:
                total = n2.val + carry
                if total >= 10:
                    total -= 10
                    carry = 1
                else:
                    carry = 0
                last_fixed.next = ListNode(val=total)
                last_fixed = last_fixed.next
                n2 = n2.next
            else:
                total = n1.val + n2.val + carry
                if total >= 10:
                    total -= 10
                    carry = 1
                else:
                    carry = 0
                last_fixed.next = ListNode(val=total)
                last_fixed = last_fixed.next
                n1 = n1.next
                n2 = n2.next
        
        if carry == 1:
            last_fixed.next = ListNode(val=1)

        return dummy.next
