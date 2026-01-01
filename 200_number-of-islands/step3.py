import collections


class Solution:
    WATER = "0"
    LAND = "1"

    def _is_land(self, grid: List[List[int]], i: int, j: int) -> bool:
        NUM_ROWS = len(grid)
        NUM_COLUMNS = len(grid[0])
        if i < 0 or i >= NUM_ROWS:
            return False
        if j < 0 or j >= NUM_COLUMNS:
            return False
        return grid[i][j] == self.LAND

    def _mark_connecting_lands_visited(
        self, grid: List[List[str]], visited: List[List[bool]], i: int, j: int
    ) -> List[List[bool]]:
        to_be_traversed = collections.deque()
        to_be_traversed.append((i, j))
        visited[i][j] = True
        while to_be_traversed:
            i, j = to_be_traversed.popleft()
            for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                neighbor_i = i + di
                neighbor_j = j + dj
                if not self._is_land(grid, neighbor_i, neighbor_j):
                    continue
                if visited[neighbor_i][neighbor_j]:
                    continue
                to_be_traversed.append((neighbor_i, neighbor_j))
                visited[neighbor_i][neighbor_j] = True

        return visited

    def numIslands(self, grid: List[List[str]]) -> int:
        NUM_ROWS = len(grid)
        NUM_COLUMNS = len(grid[0])
        visited = [[False] * NUM_COLUMNS for _ in range(NUM_ROWS)]
        num_islands = 0
        for i in range(NUM_ROWS):
            for j in range(NUM_COLUMNS):
                if grid[i][j] == self.WATER:
                    continue

                assert grid[i][j] == self.LAND
                if visited[i][j]:
                    continue

                num_islands += 1
                visited = self._mark_connecting_lands_visited(grid, visited, i, j)

        return num_islands
