class Solution:
    # 行きがけの再帰（前から逆順にしていく）
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def reverse_list_helper(working_head, reversed_tail):
            if working_head is None:
                return reversed_tail

            to_be_delegated = working_head.next
            working_head.next = reversed_tail
            return reverse_list_helper(to_be_delegated, working_head)

        return reverse_list_helper(head, None)

    # 帰りがけの再帰（後ろから逆順にしていく）
    def reverseList2(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def reverse_list_helper(node) -> tuple[Optional[ListNode], Optional[ListNode]]:
            if node.next is None:
                return node, node
            reversed_head, reversed_tail = reverse_list_helper(node.next)
            node.next = None
            reversed_tail.next = node
            reversed_tail = reversed_tail.next
            return reversed_head, reversed_tail

        if not head:
            return None

        reversed_head, _ = reverse_list_helper(head)
        return reversed_head
