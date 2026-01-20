class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # store the result of uniquePaths(1, n) to [0, n-1]
        unique_paths = [1] * n

        for row in range(1, m):
            for col in range(1, n):
                # uniquePaths(row, col) = uniquePaths(row-1, col) + uniquePaths(row, col-1)
                unique_paths[col] = unique_paths[col] + unique_paths[col - 1]

        return unique_paths[-1]
