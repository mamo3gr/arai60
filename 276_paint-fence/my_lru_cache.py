from typing import Any, Hashable, Self


class Node:
    def __init__(
        self,
        key: Hashable,
        value: Any,
        prev: Self | None = None,
        next: Self | None = None,
    ):
        self.key = key
        self.value = value
        self.prev = prev
        self.next = next


class MyLRUCache:
    def __init__(self, capacity: int):
        if capacity <= 0:
            raise ValueError("capacity must be positive")
        self.capacity = capacity
        self.key_to_node = dict()
        self.dummy_head = Node(key=None, value=None)
        self.dummy_tail = Node(key=None, value=None, prev=self.dummy_head)
        self.dummy_head.next = self.dummy_tail

    def get(self, key: Hashable) -> Any:
        if key not in self.key_to_node:
            raise KeyError(f"key={key} not cached")

        node = self.key_to_node[key]
        self._move_to_head(node)
        return node.value

    def put(self, key: Hashable, value: Any) -> None:
        if key in self.key_to_node:
            node = self.key_to_node[key]
            node.value = value
            self._move_to_head(node)
            return

        new_node = Node(key=key, value=value)
        self.key_to_node[key] = new_node
        self._insert(new_node, self.dummy_head)

        while len(self.key_to_node) > self.capacity:
            node_to_delete = self.dummy_tail.prev
            self._delete(node_to_delete)
            del self.key_to_node[node_to_delete.key]
            del node_to_delete

    @staticmethod
    def _insert(x: Node, a: Node) -> None:
        """Insert node x right after node a."""
        x.next = a.next
        a.next.prev = x

        a.next = x
        x.prev = a

    @staticmethod
    def _delete(x: Node) -> None:
        x.next.prev = x.prev
        x.prev.next = x.next

    def _move_to_head(self, x: Node) -> None:
        self._delete(x)
        self._insert(x, self.dummy_head)
