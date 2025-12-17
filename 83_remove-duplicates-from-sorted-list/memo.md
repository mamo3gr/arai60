## step 1

- 現在のノードを辿っていき、現在のノードと値が違うものに出会ったら、nextの参照をそこに向ければ良い。

## step 2

`node.next` とか `node.next.next` が出てくる上に、`node.next` に `node.next.next` を代入しておりややこしい。「値が異なる次のノードを探す」処理を切り出すと、次のようになる。

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def find_first_different_node(head: Optional[ListNode]) -> Optional[ListNode]:
            node = head
            while node and node.val == head.val:
                node = node.next
            return node

        node = head
        while node:
            node.next = find_first_different_node(node)
            node = node.next

        return head
```

メインルーチンはとてもシンプルになった（英語のように読める）のがメリット。デメリットはやや冗長か。`node = head` みたいな似ている行が複数回登場するので。

関数にするほどでもなく、次につなぐべきノードへの参照を探しているよ、ということがわかれば良さそう。

```python
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
```
