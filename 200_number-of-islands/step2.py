from collections import deque


class Solution:
    @staticmethod
    def _mark_connecting_islands_visited(grid, visited, i, j) -> set[tuple[int, int]]:
        queue = deque()
        queue.append((i, j))
        while queue:
            i, j = queue.popleft()
            visited.add((i, j))

            # top
            if i - 1 >= 0 and grid[i - 1][j] == "1" and (i - 1, j) not in visited:
                queue.append((i - 1, j))
                visited.add((i - 1, j))
            # down
            if (
                i + 1 < len(grid)
                and grid[i + 1][j] == "1"
                and (i + 1, j) not in visited
            ):
                queue.append((i + 1, j))
                visited.add((i + 1, j))
            # left
            if j - 1 >= 0 and grid[i][j - 1] == "1" and (i, j - 1) not in visited:
                queue.append((i, j - 1))
                visited.add((i, j - 1))
            # right
            if (
                j + 1 < len(grid[i])
                and grid[i][j + 1] == "1"
                and (i, j + 1) not in visited
            ):
                queue.append((i, j + 1))
                visited.add((i, j + 1))

        return visited

    def numIslands(self, grid: List[List[str]]) -> int:
        num_islands = 0
        visited: set[tuple[int, int]] = set()
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == "0":
                    continue

                if (i, j) in visited:
                    continue

                num_islands += 1
                visited = self._mark_connecting_islands_visited(grid, visited, i, j)

        return num_islands
