class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: list[list[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])

        unique_paths = [None] * n
        unique_paths[0] = 1 if obstacleGrid[0][0] == 0 else 0
        for col in range(1, n):
            if obstacleGrid[0][col] == 1:
                unique_paths[col] = 0
            else:
                unique_paths[col] = unique_paths[col - 1]

        for row in range(1, m):
            for col in range(0, n):
                if obstacleGrid[row][col] == 1:
                    unique_paths[col] = 0
                    continue

                upper_cell = unique_paths[col]
                left_cell = unique_paths[col - 1] if col > 0 else 0
                unique_paths[col] = upper_cell + left_cell

        return unique_paths[-1]
