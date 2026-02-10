class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        if n < 1:
            raise ValueError("n must be >= 1")
        if not 1 <= k <= 2 ** (n - 1):
            raise ValueError("k must be 1 <= k <= 2**(n-1)")

        num_bit_flips = 0
        while n > 1:
            is_right_child = k % 2 == 0
            if is_right_child:
                num_bit_flips += 1
            n -= 1
            k = (k + 1) // 2

        root_symbol = 0
        return root_symbol ^ (num_bit_flips % 2)
