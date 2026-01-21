class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: list[list[int]]) -> int:
        OBSTACLE = 1

        if not obstacleGrid:
            raise ValueError("Obstacle grid must not be empty")
        if not obstacleGrid[0]:
            raise ValueError("Obstacle grid must be 2D array")
        if obstacleGrid[0][0] == OBSTACLE:
            return 0  # all grids are unreachable

        m = len(obstacleGrid)
        n = len(obstacleGrid[0])

        unique_paths = [None] * n
        unique_paths[0] = 1
        for col in range(1, n):
            if obstacleGrid[0][col] == OBSTACLE:
                unique_paths[col] = 0
            else:
                unique_paths[col] = unique_paths[col - 1]

        for row in range(1, m):
            for col in range(n):
                if obstacleGrid[row][col] == OBSTACLE:
                    unique_paths[col] = 0
                    continue

                from_upper = unique_paths[col]
                from_left = unique_paths[col - 1] if 0 < col else 0
                unique_paths[col] = from_upper + from_left

        return unique_paths[-1]
