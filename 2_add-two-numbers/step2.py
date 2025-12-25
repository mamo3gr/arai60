# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    @staticmethod
    def _add_digit(n1: Optional[ListNode], n2: Optional[ListNode], carry: int) -> tuple[int, int]:
        val1 = n1.val if n1 else 0
        val2 = n2.val if n2 else 0
        total = val1 + val2 + carry
        if total >= 10:
            total -= 10
            carry_new = 1
        else:
            carry_new = 0
        return total, carry_new
    
    @staticmethod
    def _move_to_next(node: Optional[ListNode]) -> Optional[ListNode]:
        if node:
            return node.next
        else:
            return None

    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        dummy = ListNode()

        last_fixed = dummy
        n1 = l1
        n2 = l2
        carry = 0
        while n1 or n2:
            total, carry = self._add_digit(n1, n2, carry)

            last_fixed.next = ListNode(val=total)
            last_fixed = last_fixed.next

            n1 = self._move_to_next(n1)
            n2 = self._move_to_next(n2)
        
        if carry == 1:
            last_fixed.next = ListNode(val=1)

        return dummy.next
