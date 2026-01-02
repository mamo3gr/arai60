import collections


class Solution:
    WATER = 0
    LAND = 1

    def _measure_area_and_mark_connecting_land_visited(
        self, grid: List[List[int]], visited: List[List[bool]], r: int, c: int
    ) -> tuple[int, List[List[bool]]]:
        num_rows = len(grid)
        num_columns = len(grid[0])

        def is_land(r: int, c: int) -> bool:
            return (
                0 <= r < num_rows and 0 <= c < num_columns and grid[r][c] == self.LAND
            )

        to_be_visited = collections.deque()
        to_be_visited.append((r, c))
        visited[r][c] = True
        area = 0
        directions = ((-1, 0), (1, 0), (0, -1), (0, 1))
        while to_be_visited:
            r, c = to_be_visited.popleft()
            area += 1
            for direction_r, direction_c in directions:
                neighbor_r = r + direction_r
                neighbor_c = c + direction_c
                if not is_land(neighbor_r, neighbor_c):
                    continue
                if visited[neighbor_r][neighbor_c]:
                    continue
                to_be_visited.append((neighbor_r, neighbor_c))
                visited[neighbor_r][neighbor_c] = True

        return area, visited

    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        num_rows = len(grid)
        num_columns = len(grid[0])
        visited = [[False] * num_columns for _ in range(num_rows)]
        max_area = 0
        for r in range(num_rows):
            for c in range(num_columns):
                cell = grid[r][c]
                if cell == self.WATER:
                    continue
                if cell != self.LAND:
                    raise ValueError(f"Invalid cell value: {cell}")
                if visited[r][c]:
                    continue
                area, visited = self._measure_area_and_mark_connecting_land_visited(
                    grid, visited, r, c
                )
                max_area = max(max_area, area)

        return max_area
