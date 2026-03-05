class UnionFind:
    def __init__(self, n: int):
        self.parent = list(range(n))
        self.group_size = [1] * n
        self.num_groups = n

    def count(self) -> int:
        return self.num_groups

    def find(self, x: int) -> int:
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x: int, y: int) -> bool:
        x_parent = self.find(x)
        y_parent = self.find(y)
        if x_parent == y_parent:
            return False

        if self.group_size[x_parent] < self.group_size[y_parent]:
            x_parent, y_parent = y_parent, x_parent
        self.parent[y_parent] = x_parent
        self.group_size[x_parent] += self.group_size[y_parent]
        self.num_groups -= 1
        return True


class Solution:
    def countComponents(self, n: int, edges: list[list[int]]) -> int:
        uf = UnionFind(n)
        for x, y in edges:
            uf.union(x, y)
        return uf.count()
