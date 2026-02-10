class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        if n <= 0:
            raise ValueError("n must be >= 1")
        if not 1 <= k <= 2 ** (n - 1):
            raise ValueError("k must be [1, 2^(n-1)]")

        num_bit_flips = self.compute_number_to_go_right(n, k)
        root_symbol = 0
        return root_symbol ^ (num_bit_flips % 2)

    @staticmethod
    def compute_number_to_go_right(n: int, k: int) -> int:
        count = 0
        while n > 1:
            if k % 2 == 0:
                count += 1
            n -= 1
            k = (k + 1) // 2
        return count
