class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        if n < 1:
            raise ValueError("n must be >= 1")
        if not 1 <= k <= 2 ** (n - 1):
            raise ValueError("k must be 1 <= k <= 2**(n-1)")

        k_zero_indexed = k - 1
        num_bin_flips = k_zero_indexed.bit_count()
        root_symbol = 0
        return root_symbol ^ (num_bin_flips % 2)
