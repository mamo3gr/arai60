class Solution:
    def myPow(self, x: float, n: int) -> float:
        negative = n < 0
        if negative:
            n *= -1

        power = self._helper(x, n)
        if negative:
            return 1 / power
        else:
            return power

    def _helper(self, x: float, n: int) -> float:
        if n == 0:
            return 1

        half = self._helper(x, n // 2)
        if n % 2 == 0:
            return half * half
        else:
            return half * half * x
