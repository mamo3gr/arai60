import functools


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: list[list[int]]) -> int:
        OBSTACLE = 1

        if not obstacleGrid:
            raise ValueError("Obstacle grid must not be empty")
        if not obstacleGrid[0]:
            raise ValueError("Obstacle grid must be 2D array")
        if obstacleGrid[0][0] == OBSTACLE:
            return 0  # no grid reachable

        m = len(obstacleGrid)
        n = len(obstacleGrid[0])

        @functools.cache
        def unique_paths(row: int, col: int) -> int:
            if obstacleGrid[row][col] == OBSTACLE:
                return 0

            if row == 0 and col == 0:
                return 1

            num_unique_paths = 0
            if 0 < row:
                num_unique_paths += unique_paths(row - 1, col)
            if 0 < col:
                num_unique_paths += unique_paths(row, col - 1)

            return num_unique_paths

        return unique_paths(m - 1, n - 1)
