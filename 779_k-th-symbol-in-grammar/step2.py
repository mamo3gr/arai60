class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        if n < 1:
            raise ValueError("n must be >= 1")
        if not 1 <= k <= 2 ** (n - 1):
            raise ValueError("k must be 1 <= k <= 2**(n-1)")

        def compute_symbol(n: int, k: int) -> int:
            if n == 1:
                return 0
            parent_k = (k + 1) // 2
            parent = compute_symbol(n - 1, parent_k)
            is_left_child = k % 2 == 1
            return parent if is_left_child else parent ^ 1

        return compute_symbol(n, k)
