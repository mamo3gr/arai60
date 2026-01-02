class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.area = [0] * n

    def find(self, x):
        if self.parent[x] == x:
            return x
        return self.find(self.parent[x])

    def union(self, x, y):
        x_parent = self.find(x)
        y_parent = self.find(y)
        if x_parent == y_parent:
            return

        if self.area[x_parent] < self.area[y_parent]:
            x_parent, y_parent = y_parent, x_parent

        self.parent[y_parent] = x_parent
        self.area[x_parent] += self.area[y_parent]


class Solution:
    WATER = 0
    LAND = 1

    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        num_rows = len(grid)
        num_columns = len(grid[0])

        def is_land(r, c) -> bool:
            return (
                0 <= r < num_rows and 0 <= c < num_columns and grid[r][c] == self.LAND
            )

        uf = UnionFind(num_rows * num_columns)
        for r in range(num_rows):
            for c in range(num_columns):
                if grid[r][c] == self.LAND:
                    uf.area[r * num_columns + c] = 1

        for r in range(num_rows):
            for c in range(num_columns):
                if grid[r][c] == self.WATER:
                    continue
                assert grid[r][c] == self.LAND
                for direction_r, direction_c in ((1, 0), (0, 1)):
                    neighbor_r = r + direction_r
                    neighbor_c = c + direction_c
                    if not is_land(neighbor_r, neighbor_c):
                        continue
                    uf.union(
                        r * num_columns + c,
                        neighbor_r * num_columns + neighbor_c,
                    )

        return max(uf.area)
