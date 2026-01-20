import functools


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        @functools.lru_cache(maxsize=None)
        def helper(m: int, n: int) -> int:
            if m == 1 or n == 1:
                return 1

            return helper(m - 1, n) + helper(m, n - 1)

        return helper(m, n)
