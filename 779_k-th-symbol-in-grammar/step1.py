import math


class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        if n < 1:
            raise ValueError("n must be >= 1")
        if n == 1:
            return 0

        parent_n = n - 1
        parent_k = math.ceil(k / 2)
        parent_symbol = self.kthGrammar(parent_n, parent_k)
        is_left_child = k % 2 == 1
        if parent_symbol == 0:
            if is_left_child:
                return 0
            else:
                return 1
        else:
            if is_left_child:
                return 1
            else:
                return 0
