from collections import deque


class Solution:
    @staticmethod
    def _can_reach_visited(grid, visited, i, j) -> bool:
        queue = deque()
        queue.append((i, j))
        queued = set((i, j))
        while queue:
            i, j = queue.popleft()
            if (i, j) in visited:
                return True

            # top
            if i - 1 >= 0 and grid[i - 1][j] == "1" and (i - 1, j) not in queued:
                queue.append((i - 1, j))
                queued.add((i - 1, j))
            # down
            if i + 1 < len(grid) and grid[i + 1][j] == "1" and (i + 1, j) not in queued:
                queue.append((i + 1, j))
                queued.add((i + 1, j))
            # left
            if j - 1 >= 0 and grid[i][j - 1] == "1" and (i, j - 1) not in queued:
                queue.append((i, j - 1))
                queued.add((i, j - 1))
            # right
            if (
                j + 1 < len(grid[i])
                and grid[i][j + 1] == "1"
                and (i, j + 1) not in queued
            ):
                queue.append((i, j + 1))
                queued.add((i, j + 1))

        return False

    def numIslands(self, grid: List[List[str]]) -> int:
        num_islands = 0
        visited: set[tuple[int, int]] = set()
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == "0":
                    continue

                if not self._can_reach_visited(grid, visited, i, j):
                    num_islands += 1

                visited.add((i, j))

        return num_islands
