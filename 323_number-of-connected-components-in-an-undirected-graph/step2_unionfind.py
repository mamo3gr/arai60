class UnionFind:
    def __init__(self, n: int):
        self.parent = [i for i in range(n)]
        self.group_size = [1] * n
        self.num_groups = n

    def count(self) -> int:
        return self.num_groups

    def find(self, x: int) -> int:
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x: int, y: int) -> bool:
        parent_x = self.find(x)
        parent_y = self.find(y)
        if parent_x == parent_y:
            return False

        if self.group_size[parent_x] < self.group_size[parent_y]:
            parent_x, parent_y = parent_y, parent_x

        self.parent[parent_y] = parent_x
        self.group_size[parent_x] += self.group_size[parent_y]
        self.num_groups -= 1
        return True


class Solution:
    def countComponents(self, n: int, edges: list[list[int]]) -> int:
        uf = UnionFind(n)
        for a, b in edges:
            uf.union(a, b)
        return uf.count()
