# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # 行きがけの再帰（前から逆順にしていく）
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def reverse_and_prepend(node_to_reverse, base_list):
            if not node_to_reverse:
                return base_list

            to_be_delegated = node_to_reverse.next
            node_to_reverse.next = base_list
            return reverse_and_prepend(to_be_delegated, node_to_reverse)

        if not head:
            return None

        return reverse_and_prepend(head, None)

    # 帰りがけの再帰（後ろから逆順にしていく）
    def reverseList2(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None

        if not head.next:
            return node

        reversed_head = self.reverseList(head.next)
        head.next.next = node
        head.next = None
        return reversed_head
