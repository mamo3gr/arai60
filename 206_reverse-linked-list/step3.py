# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None

        working = head
        reversed_to = None

        while True:
            upcoming_working = working.next

            working.next = reversed_to

            if not upcoming_working:
                break
            else:
                reversed_to = working
                working = upcoming_working

        return working
