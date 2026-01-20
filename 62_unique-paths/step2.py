class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        """二次元配列での反復法"""

        # the result of uniquePaths(m, n) is stored to unique_paths[m-1][n-1]
        unique_paths = [[None] * n for _ in range(m)]
        for row in range(m):
            unique_paths[row][0] = 1
        for col in range(n):
            unique_paths[0][col] = 1

        for row in range(1, m):
            for col in range(1, n):
                unique_paths[row][col] = (
                    unique_paths[row][col - 1] + unique_paths[row - 1][col]
                )

        return unique_paths[m - 1][n - 1]

    def uniquePathsMemory2xN(self, m: int, n: int) -> int:
        """二次元配列での反復法で、メモリをm x n -> 2 x nに抑えたバージョン"""

        # the result of uniquePaths(1, col) for col in range(n)
        unique_paths = [1] * n

        for row in range(1, m):
            unique_paths_next_row = [1] * n

            for col in range(1, n):
                unique_paths_next_row[col] = (
                    unique_paths[col] + unique_paths_next_row[col - 1]
                )

            unique_paths = unique_paths_next_row

        return unique_paths[-1]

    def uniquePathsMemory1xN(self, m: int, n: int) -> int:
        """二次元配列での反復法で、メモリを1 x nに抑えたバージョン"""

        # the result of uniquePaths(1, col) for col in range(n)
        unique_paths = [1] * n

        for row in range(1, m):
            for col in range(1, n):
                unique_paths[col] = unique_paths[col] + unique_paths[col - 1]

        return unique_paths[-1]
