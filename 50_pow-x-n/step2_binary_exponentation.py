class Solution:
    def myPow(self, x: float, n: int) -> float:
        """
        right to left binary exponentation

        inspired from:
        https://github.com/hayashi-ay/leetcode/pull/41
        """
        if n == 0:
            return 1
        if n < 0:
            x = 1 / x
            n = -n

        powered = 1
        cumulated_product = x
        while n > 0:
            if n % 2 == 1:
                powered *= cumulated_product
            cumulated_product *= cumulated_product
            n >>= 1

        return powered

    def myPowLeftToRightBinaryExponentation(self, x: float, n: int) -> float:
        """
        left to right binary exponentation

        inspired from:
        https://github.com/hayashi-ay/leetcode/pull/41
        """
        if n < 0:
            x = 1 / x
            n = -n

        powered = 1
        for bit_i in reversed(range(n.bit_length())):
            powered = powered * powered
            if (n >> bit_i) & 1 == 1:
                powered = x * powered

        return powered
