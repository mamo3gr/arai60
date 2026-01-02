import collections


class Solution:
    WATER = 0
    LAND = 1

    def _mark_connecting_islands_and_compute_area(
        self, grid: List[List[int]], visited: List[List[int]], r: int, c: int
    ) -> tuple[List[List[int]], int]:
        num_rows = len(grid)
        num_columns = len(grid[0])

        def is_land(r, c) -> bool:
            return (
                0 <= r < num_rows and 0 <= c < num_columns and grid[r][c] == self.LAND
            )

        connecting_islands = collections.deque()
        connecting_islands.append((r, c))
        visited[r][c] = True
        area = 0
        while connecting_islands:
            r, c = connecting_islands.popleft()
            area += 1
            for dr, dc in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                neighbor_r = r + dr
                neighbor_c = c + dc
                if (
                    is_land(neighbor_r, neighbor_c)
                    and not visited[neighbor_r][neighbor_c]
                ):
                    connecting_islands.append((neighbor_r, neighbor_c))
                    visited[neighbor_r][neighbor_c] = True

        return visited, area

    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        num_rows = len(grid)
        num_columns = len(grid[0])
        visited = [[False] * num_columns for _ in range(num_rows)]
        max_area = 0
        for r in range(num_rows):
            for c in range(num_columns):
                if grid[r][c] == self.WATER:
                    continue

                if visited[r][c]:
                    continue

                visited, area = self._mark_connecting_islands_and_compute_area(
                    grid, visited, r, c
                )
                max_area = max(max_area, area)

        return max_area
