import collections


class Solution:
    WATER = 0
    LAND = 1

    def _mark_connecting_islands_and_compute_area(
        self, grid: List[List[int]], visited: List[List[int]], r: int, c: int
    ) -> tuple[List[List[int]], int]:
        NUM_ROWS = len(grid)
        NUM_COLUMNS = len(grid[0])

        def is_land(r, c) -> bool:
            return (
                0 <= r < NUM_ROWS and 0 <= c < NUM_COLUMNS and grid[r][c] == self.LAND
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
        NUM_ROWS = len(grid)
        NUM_COLUMNS = len(grid[0])
        visited = [[False] * NUM_COLUMNS for _ in range(NUM_ROWS)]
        max_area = 0
        for r in range(NUM_ROWS):
            for c in range(NUM_COLUMNS):
                if grid[r][c] == self.WATER:
                    continue

                if visited[r][c]:
                    continue

                visited, area = self._mark_connecting_islands_and_compute_area(
                    grid, visited, r, c
                )
                max_area = max(max_area, area)

        return max_area
